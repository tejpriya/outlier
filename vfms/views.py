from django.shortcuts import render,redirect
from .models import *
from .forms import *
from django.core.files.storage import FileSystemStorage
from django.views import View 
from django.views.generic.edit import UpdateView
# from accounts.views import *
import requests,json
from django.db.models import Q
from django.http import JsonResponse
from django.http import HttpResponse
import time
from .filters import *
from pathlib import Path
from django.views.decorators.csrf import csrf_exempt

import shutil,sys
import numpy as np
from PIL import Image
from sklearn.cluster import KMeans
from sklearn.neighbors import LocalOutlierFactor
import imagehash

##########
import os,cv2
from django.conf import settings
from django.templatetags import static
####
# from .filters import*
from django.forms import inlineformset_factory
from django.http import JsonResponse
from xml.etree import ElementTree as ET



### dashboard information
def dashboarddata(request):
  if request.method =="GET":
    total_company=Company.objects.all().count()
    total_projects=Project.objects.all().count()
    total_locations=Location.objects.all().count()
    total_videos=VideoFiles.objects.all().count()
    
    context={'total_company':total_company,'total_projects':total_projects,'total_locations':total_locations,'total_videos':total_videos}
    return render(request, "templates/dms/Dashboard.html", context)
  else:
    return redirect('Error_url')


### aduit log for all the actions performed
def auditdata(form_name,action_performed,acted_by):
    acted_by='Admin' ## temporary set as admin
    auditlog = AuditLog(form_name=form_name, action_performed=action_performed,acted_by=acted_by) # create new model instance
    auditlog.save() #save to db

### loading media files images
def WorkInProgress(request):
    path = settings.MEDIA_ROOT
    print(path)
    img_list = os.listdir(path + '/images')
    print(img_list)
    context = {'images' : img_list}
    return render(request, "templates/dms/WorkInProgress.html", context)

## to add new company information entered by user
def my_form(request):
    # user = get_current_user(request)
    # user_id = user.id
  if request.method == "POST":
    form = MyForm(request.POST)
    if form.is_valid():
      form.save()
      ###adding to the auditlog ###
      auditdata('Company','ADD','Admin')
      # auditlog = AuditLog(form_name='AddCompany', action_performed='ADD',acted_by='Admin') # create new model instance
      # auditlog.save() #seve to db
      ###end##
      return redirect('success_url')
  else:
      form = MyForm()
      return render(request, 'templates/dms/AddCompany.html', {'form': form})


# to update specific company information modified by user
class CompanyUpdate(UpdateView):
  
  def render(self,request,pk_id):
    get_company=Company.objects.get(id=pk_id)
    form=MyForm(instance=get_company)
    context={'form':form}
    return render(request,'templates/dms/CompanyUpdate.html',context)

  def get(self,request,pk_id):
    get_company=Company.objects.get(id=pk_id)
    form=MyForm(instance=get_company)
    context={'form':form}

    return render(request,'templates/dms/CompanyUpdate.html', context)

  def post(self,request,pk_id):
    update_company=Company.objects.get(id=pk_id)
    self.form=MyForm(request.POST,instance=update_company)
    if self.form.is_valid():
      self.form.save()
      ###adding to the auditlog ###
      auditdata('Company','Update','Admin')
      return redirect('success_url')
    else:
      return self.render(request)


## listing company details

class ListCompany(View):
    def get(self,request,*args,**kwargs):
        form = MyForm()
        all_companies=Company.objects.all()
        context={'all_companies':all_companies,'form':form}
      
        return render (request,'templates/dms/ListCompany.html',context=context)

## new method ## Modify company ## list generation

def edit_form(request):
  if request.method == "POST":
    form = MyForm(request.POST)
    if form.is_valid():
      form.save()
      ###adding to the auditlog ###
      auditdata('Company','Update','Admin')
      return redirect('success_url')
    else:
        form = MyForm()
        return render(request, 'templates/dms/ModifyCompany.html', {'form': form})
  else:
    all_companies=Company.objects.all()
    context={'all_companies':all_companies}

    return render(request,'templates/dms/ModifyCompany.html', context)


###### Project relevant classes########


class ListProject(View):
    def get(self,request,*args,**kwargs):
        form = ProjForm()
        all_projects=Project.objects.all()
        context={'all_projects':all_projects,'form':form}
       
        return render (request,'templates/dms/ListProject.html',context=context)

## to add new project information entered by user
def project_form(request):
  if request.method == "POST":
    form = ProjForm(request.POST)
    print(form)
    print('PROJECT FORM IS VALID OR NOT :' ,form.is_valid())
    if form.is_valid():
      form.save()
      ###adding to the auditlog ###
      auditdata('Project','Add','Admin')
      return redirect('success_url')
  else:
      form = ProjForm()
      return render(request, 'templates/dms/AddProject.html', {'form': form})

# to update station information 
def editproj_form(request):
  if request.method == "POST":
    form = ProjForm(request.POST)
    if form.is_valid():
      form.save()
      ###adding to the auditlog ###
      auditdata('Project','update','Admin')
      return redirect('success_url')
    else:
        form = ProjForm()
        return render(request, 'templates/dms/ModifyProject.html', {'form': form})
  else:
    all_projects=Project.objects.all()
    context={'all_projects':all_projects}

    return render(request,'templates/dms/ModifyProject.html', context)


# to update specific project information edited by user
class ProjectUpdate(UpdateView):
  
  def render(self,request,pk_id):
    get_project=Project.objects.get(id=pk_id)
    form=ProjForm(instance=get_project)
    context={'form':form}
    return render(request,'templates/dms/ProjectUpdate.html',context)

  def get(self,request,pk_id):
    get_project=Project.objects.get(id=pk_id)
    form=ProjForm(instance=get_project)
    context={'form':form}

    return render(request,'templates/dms/ProjectUpdate.html', context)

  def post(self,request,pk_id):
    update_Project=Project.objects.get(id=pk_id)
    self.form=ProjForm(request.POST,instance=update_Project)
    if self.form.is_valid():
      self.form.save()
      ###adding to the auditlog ###
      auditdata('Project','update','Admin')
      return redirect('success_url')
    else:
      return self.render(request)




########## Station/Location class ##############
## station List
class ListStation(View):
    def get(self,request,*args,**kwargs):
        form = LocationForm()
        all_locations=Location.objects.all()
         
        context={'all_locations':all_locations,'form':form}
       
        return render (request,'templates/dms/ListStation.html',context=context)

## to add new station information entered by user
def station_form(request):
    if request.method == "POST":
      form = LocationForm(request.POST)
      if form.is_valid():
        form.save()
        ###adding to the auditlog ###
        auditdata('Station','Add','Admin')
      return redirect('success_url')
    else:
      form = LocationForm()
      return render(request, 'templates/dms/AddStation.html', {'form': form})

# to update station information - listing for user
def editstn_form(request):
  if request.method == "POST":
    form = LocationForm(request.POST)
    if form.is_valid():
      form.save()
      ###adding to the auditlog ###
      auditdata('station','update','Admin')
      return redirect('success_url')
    else:
        form = LocationForm()
        return render(request, 'templates/dms/ModifyStation.html', {'form': form})
  else:
    all_locations=Location.objects.all()
    context={'all_locations':all_locations}

    return render(request,'templates/dms/ModifyStation.html', context)

# to update specific station information edited by user
class StationUpdate(UpdateView):
  
  def render(self,request,pk_id):
    get_station=Location.objects.get(id=pk_id)
    form=LocationForm(instance=get_station)
    context={'form':form}
    return render(request,'templates/dms/StationUpdate.html',context)

  def get(self,request,pk_id):
    get_station=Location.objects.get(id=pk_id)
    form=LocationForm(instance=get_station)
    context={'form':form}

    return render(request,'templates/dms/StationUpdate.html', context)

  def post(self,request,pk_id):
    update_station=Location.objects.get(id=pk_id)
    self.form=LocationForm(request.POST,instance=update_station)
    if self.form.is_valid():
      self.form.save()
      auditdata('station','update','Admin')  ###adding to the auditlog ###
      return redirect('success_url')
    else:
      return self.render(request)


############## camera Model #############
## list camera models

class ListcModel(View):
  
    def get(self,request, *args,**kwargs):
        form = CModelForm()
        all_cModels=CameraModel.objects.all()
        context={'all_cModels':all_cModels,'form':form}
        
        return render(request,'templates/dms/ListCameraModel.html',context=context)

## to add new camera model information entered by user
def Cmodel_form(request):
  if request.method == "POST":
    form = CModelForm(request.POST)
    if form.is_valid():
      form.save()
      auditdata('cameraModel','Add','Admin')  ###adding to the auditlog ###
      return redirect('success_url')
  else:
      form = CModelForm()
      return render(request, 'templates/dms/AddCameraModel.html', {'form': form})

# to update Camera Model information modified by user
def editcModel_form(request):
  if request.method == "POST":
    form = CModelForm(request.POST)
    if form.is_valid():
      form.save()
      auditdata('cameraModel','Update','Admin')  ###adding to the auditlog ###
      return redirect('success_url')
    else:
        form = CModelForm()
        return render(request, 'templates/dms/ModifyCameraModel.html', {'form': form})
  else:
    all_cModels=CameraModel.objects.all()
    context={'all_cModels':all_cModels}

    return render(request,'templates/dms/ModifyCameraModel.html', context)

# to update specific camera model information edited by user
class CModelUpdate(UpdateView):
  
  def render(self,request,pk_id):
    get_cModel=CameraModel.objects.get(id=pk_id)
    form=CModelForm(instance=get_cModel)
    context={'form':form}
    return render(request,'templates/dms/CModelUpdate.html',context)

  def get(self,request,pk_id):
    get_cModel=CameraModel.objects.get(id=pk_id)
    form=CModelForm(instance=get_cModel)
    context={'form':form}

    return render(request,'templates/dms/CModelUpdate.html', context)

  def post(self,request,pk_id):
    update_cModel=CameraModel.objects.get(id=pk_id)
    self.form=CModelForm(request.POST,instance=update_cModel)
    if self.form.is_valid():
      self.form.save()
      auditdata('cameraModel','Update','Admin')  ###adding to the auditlog ###
      return redirect('success_url')
    else:
      return self.render(request)




### Camera Position ########
class ListcPosition(View):
    def get(self,request,*args,**kwargs):
        form = CPositionForm()
        all_cpositions=CameraPosition.objects.all()
        context={'all_cpositions':all_cpositions,'form':form}
      
        return render (request,'templates/dms/ListCameraPosition.html',context=context)



## to add new camera position  information entered by user
def CPosition_form(request):
  if request.method == "POST":
    form = CPositionForm(request.POST)
    if form.is_valid():
      form.save()
      auditdata('cameraPosition','Add','Admin')  ###adding to the auditlog ###
      return redirect('success_url')
  else:
      form = CPositionForm()
      return render(request, 'templates/dms/AddCameraPosition.html', {'form': form})


# to update station information modified by user
def editcPosition_form(request):
  if request.method == "POST":
    form = CPositionForm(request.POST)
    if form.is_valid():
      form.save()
      auditdata('cameraPosition','Update','Admin')  ###adding to the auditlog ###
      return redirect('success_url')
    else:
        form = CPositionForm()
        return render(request, 'templates/dms/ModifyCameraPosition.html', {'form': form})
  else:
    all_cpositions=CameraPosition.objects.all()
    context={'all_cpositions':all_cpositions}

    return render(request,'templates/dms/ModifyCameraPosition.html', context)

# to update specific camera Position information edited by user
class CPositionUpdate(UpdateView):
  
  def render(self,request,pk_id):
    get_cpos=CameraPosition.objects.get(id=pk_id)
    form=CPositionForm(instance=get_cpos)
    context={'form':form}
    return render(request,'templates/dms/CModelUpdate.html',context)

  def get(self,request,pk_id):
    get_cpos=CameraPosition.objects.get(id=pk_id)
    form=CPositionForm(instance=get_cpos)
    context={'form':form}

    return render(request,'templates/dms/CModelUpdate.html', context)

  def post(self,request,pk_id):
    update_cPos=CameraPosition.objects.get(id=pk_id)
    self.form=CPositionForm(request.POST,instance=update_cPos)
    if self.form.is_valid():
      self.form.save()
      auditdata('cameraPosition','Update','Admin')  ###adding to the auditlog ###
      return redirect('success_url')
    else:
      return self.render(request)


############3 USER PROFILE ##############

## to add new company information entered by user
def add_user(request):
  if request.method == "POST":
    form = UserForm(request.POST)
    if form.is_valid():
      form.save()
      auditdata('User','Add','Admin')  ###adding to the auditlog ###
      return redirect('success_url')
  else:
      form = UserForm()
      return render(request, 'templates/dms/AddUser.html', {'form': form})


# to update specific company information modified by user
class UserProfileUpdate(UpdateView):
  
  def render(self,request,pk_id):
    get_user=User.objects.get(id=pk_id)
    form=UserForm(instance=get_user)
    context={'form':form}
    return render(request,'templates/dms/ProfileUpdate.html',context)

  def get(self,request,pk_id):
    get_user=User.objects.get(id=pk_id)
    form=UserForm(instance=get_user)
    context={'form':form}

    return render(request,'templates/dms/ProfileUpdate.html', context)

  def post(self,request,pk_id):
    update_user=User.objects.get(id=pk_id)
    self.form=UserForm(request.POST,instance=update_user)
    if self.form.is_valid():
      self.form.save()
      auditdata('User','Update','Admin')  ###adding to the auditlog ###
      return redirect('success_url')
    else:
      return self.render(request)


## listing company details

class ListUser(View):
    def get(self,request,*args,**kwargs):
        form = UserForm()
        all_users=User.objects.all()
        context={'all_users':all_users,'form':form}
      
        return render (request,'templates/dms/ListUser.html',context=context)

## list userprofile information for editing
def edit_user(request):
  if request.method == "POST":
    form = UserForm(request.POST)
    if form.is_valid():
      form.save()
      auditdata('User','Update','Admin')  ###adding to the auditlog ###
      return redirect('success_url')
    else:
        form = UserForm()
        return render(request, 'templates/dms/ModifyUser.html', {'form': form})
  else:
    all_users=User.objects.all()
    context={'all_users':all_users}

    return render(request,'templates/dms/ModifyUser.html', context)


############ ROLEs ##############

## to add new role  information entered by user
def add_role(request):
  if request.method == "POST":
    form = RoleForm(request.POST)
    if form.is_valid():
      form.save()
      auditdata('Role','Add','Admin')  ###adding to the auditlog ###
      return redirect('success_url')
  else:
      form = RoleForm()
      return render(request, 'templates/dms/AddRole.html', {'form': form})


# to update specific  role modified by user
class RoleUpdate(UpdateView):
  
  def render(self,request,pk_id):
    get_role=Role.objects.get(id=pk_id)
    form=RoleForm(instance=get_role)
    context={'form':form}
    return render(request,'templates/dms/RoleUpdate.html',context)

  def get(self,request,pk_id):
    get_role=Role.objects.get(id=pk_id)
    form=RoleForm(instance=get_role)
    context={'form':form}

    return render(request,'templates/dms/RoleUpdate.html', context)

  def post(self,request,pk_id):
    update_role=Role.objects.get(id=pk_id)
    self.form=RoleForm(request.POST,instance=update_role)
    if self.form.is_valid():
      self.form.save()
      auditdata('Role','Update','Admin')  ###adding to the auditlog ###
      return redirect('success_url')
    else:
      return self.render(request)


## listing role details

class ListRole(View):
    def get(self,request,*args,**kwargs):
        form = RoleForm()
        all_roles=Role.objects.all()
        context={'all_roles':all_roles,'form':form}
      
        return render (request,'templates/dms/ListRole.html',context=context)

## list role information for editing
def edit_role(request):
  if request.method == "POST":
    form = RoleForm(request.POST)
    if form.is_valid():
      form.save()
      auditdata('Role','Update','Admin')  ###adding to the auditlog ###
      return redirect('success_url')
    else:
        form = RoleForm()
        return render(request, 'templates/dms/ModifyRole.html', {'form': form})
  else:
    all_roles=Role.objects.all()
    context={'all_roles':all_roles}

    return render(request,'templates/dms/ModifyRole.html', context)

############ Video Files ##############

## to add new video File format  information entered by user
def add_vff(request):
  if request.method == "POST":
    form = VideoFileForm(request.POST)
    if form.is_valid():
      form.save()
      auditdata('VideoFileFormat','Add','Admin')  ###adding to the auditlog ###
      return redirect('success_url')
  else:
      form = VideoFileForm()
      return render(request, 'templates/dms/AddVFF.html', {'form': form})


# to update specific  video File format modified by user
class VFFUpdate(UpdateView):
  
  def render(self,request,pk_id):
    get_vff=VideoFF.objects.get(id=pk_id)
    form=VideoFileForm(instance=get_vff)
    context={'form':form}
    return render(request,'templates/dms/VFFUpdate.html',context)

  def get(self,request,pk_id):
    get_vff=VideoFF.objects.get(id=pk_id)
    form=VideoFileForm(instance=get_vff)
    context={'form':form}

    return render(request,'templates/dms/VFFUpdate.html', context)

  def post(self,request,pk_id):
    update_vff=VideoFF.objects.get(id=pk_id)
    self.form=VideoFileForm(request.POST,instance=update_vff)
    if self.form.is_valid():
      self.form.save()
      auditdata('VideoFileFormat','Update','Admin')  ###adding to the auditlog ###
      return redirect('success_url')
    else:
      return self.render(request)


## listing video File format details

class ListVFF(View):
    def get(self,request,*args,**kwargs):
        form = VideoFileForm()
        all_vff=VideoFF.objects.all()
        context={'all_vff':all_vff,'form':form}
      
        return render (request,'templates/dms/ListVFF.html',context=context)

## list video File format information for editing
def edit_vff(request):
  if request.method == "POST":
    form = VideoFileForm(request.POST)
    if form.is_valid():
      form.save()
      auditdata('VideoFileFormat','Update','Admin')  ###adding to the auditlog ###
      return redirect('success_url')
    else:
        form = VideoFileForm()
        return render(request, 'templates/dms/ModifyVFF.html', {'form': form})
  else:
    all_vff=VideoFF.objects.all()
    context={'all_vff':all_vff}

    return render(request,'templates/dms/ModifyVFF.html', context)

############ Light Intensity  ##############

## to add new Light Intensity category  information entered by user
def add_li(request):
  if request.method == "POST":
    form = LIForm(request.POST)
    if form.is_valid():
      form.save()
      auditdata('LightIntensity','Add','Admin')  ###adding to the auditlog ###
      return redirect('success_url')
  else:
      form = LIForm()
      return render(request, 'templates/dms/AddLI.html', {'form': form})


# to update specific  Light Intensity  modified by user
class LIUpdate(UpdateView):
  
  def render(self,request,pk_id):
    get_li=LItypes.objects.get(id=pk_id)
    form=LIForm(instance=get_li)
    context={'form':form}
    return render(request,'templates/dms/LIUpdate.html',context)

  def get(self,request,pk_id):
    get_li=LItypes.objects.get(id=pk_id)
    form=LIForm(instance=get_li)
    context={'form':form}

    return render(request,'templates/dms/LIUpdate.html', context)

  def post(self,request,pk_id):
    update_li=LItypes.objects.get(id=pk_id)
    self.form=LIForm(request.POST,instance=update_li)
    if self.form.is_valid():
      self.form.save()
      auditdata('LightIntensity','Update','Admin')  ###adding to the auditlog ###
      return redirect('success_url')
    else:
      return self.render(request)


## listing Light Intensity  details

class ListLI(View):
    def get(self,request,*args,**kwargs):
        form = LIForm()
        all_li=LItypes.objects.all()
        context={'all_li':all_li,'form':form}
      
        return render (request,'templates/dms/ListLI.html',context=context)

## list Light Intensity  information for editing
def edit_li(request):
  if request.method == "POST":
    form = LIForm(request.POST)
    if form.is_valid():
      form.save()
      auditdata('LightIntensity','Update','Admin')  ###adding to the auditlog ###
      return redirect('success_url')
    else:
        form = LIForm()
        return render(request, 'templates/dms/ModifyLI.html', {'form': form})
  else:
    all_li=LItypes.objects.all()
    context={'all_li':all_li}

    return render(request,'templates/dms/ModifyLI.html', context)

######## Video Files upload ##############3

class GetProjects(View):

    def get(self, request):
        id1 = request.GET.get('id', None)
        projects = Project.objects.filter(company_id = id1).values('id','name')
        
        data = {'data':list(projects)}
        print(data)
        return JsonResponse(data)
      

class GetVehicle(View):

    def get(self, request):
        id1 = request.GET.get('id', None)
        vehicles =Vehicle.objects.filter(company_id = id1).values('id','vehi')
        
        data = {'data':list(vehicles)}
        print(data)
        return JsonResponse(data)      

class GetLocations(View):

    def get(self, request):
        id1 = request.GET.get('id', None)
        location= Location.objects.filter(project_id = id1).values('id','name')
        
        data = {'data':list(location)}
        return JsonResponse(data)



class GetVideoFiles(View):
  def get(self,request):
    id1 = request.GET.get('id', None)
    print('Location ID:',id1)
    Video =VideoFiles.objects.filter(StationName_id = id1).values('id','FileName')
        
    data = {'data':list(Video)}
    print('data',data)
    return JsonResponse(data)

############videos files @@@@@@@@@
############function to filter and pass only the valid  inputs #######
def set_if_not_none(mapping, key, value):
    if value is not None and not value == "":
        mapping[key] = value
        
class ListVideos(View): ## ,pk_id
    def get(self,request,*args,**kwargs):
        
        print('request.GET', request.GET)
        form = VFiles()
        # all_Videos=VideoFiles.objects.all()
        sort_params = {}
             

       ####### Get the inputs from  filter #######
        PName=request.GET.get('ProjectName', None)
        SName=request.GET.get('StationName', None)
        LICat=request.GET.get('LICate',None)
        vidstatus=request.GET.get('videostatus',None)

      ####### call function to pass only the valid filter inputs #######
        set_if_not_none(sort_params, 'ProjectName', PName)
        set_if_not_none(sort_params, 'StationName', SName)
        set_if_not_none(sort_params, 'LICate', LICat)
        set_if_not_none(sort_params, 'videostatus', vidstatus)
        print(sort_params)
        #######pass the valid inputs filters to db model to fetch records ########
        all_Videos=VideoFiles.objects.filter(**sort_params)
            
        VideoFilter=VideoFileFilter(queryset=all_Videos)
                     
        context={'all_Videos':all_Videos,'form':form,'VideoFilter':VideoFilter}
       
        return render (request,'templates/dms/ListVideos.html',context=context)

## to add new project information entered by user

def Videos_form(request):
  print("POSTING POSTING",request.POST)
 
  # path = settings.EXTERNAL_ROOT
  # print(path)
  # Thumbnail_list = os.listdir(path + '/ThumbNailImages')
  # print(Thumbnail_list)
  # video_list = os.listdir(path + '/UploadedVideos')
  # print(video_list)
  form = VFiles()
  if request.method == "POST":
    print("POST METHOD")
    form = VFiles(request.POST,request.FILES)
    if form.is_valid():
     
      print(form)
      form.save()
      auditdata('VideoFiles','Add','Admin')  ###adding to the auditlog ###

      return redirect('success_url')
    else:
      print("INVALID INVALID FORM IS INVALID")
      print(form.errors)
  else:
      print("GET METHOD")
      all_comp=Company.objects.all()
      all_cameraMod=CameraModel.objects.all()
      all_vff=VideoFF.objects.all()
      all_li=LItypes.objects.all()
          
      context={'all_comp':all_comp,'all_cameraMod':all_cameraMod, 'all_vff':all_vff,'all_li':all_li, 'form':form}
      
      return render(request, 'templates/dms/AddVideo.html',  context)

# to update videofile information 
def editvideos_form(request):
  print("inside edit videos")
  
  if request.method == "POST":
    
    form = VFiles(request.POST)

    if form.is_valid():
      form.save()
      auditdata('VideoFiles','Update','Admin')  ###adding to the auditlog ###
      return redirect('success_url')
    else:
        form = VFiles()
        return render(request, 'templates/dms/ModifyVideo.html', {'form': form})
  else:
    
    print("inside ELSE PART")

    # all_Videos=VideoFiles.objects.all() 
    all_Videos=VideoFiles.objects.exclude(videostatus = 'Approved' )
    context={'all_Videos':all_Videos}

    return render(request,'templates/dms/ModifyVideo.html', context)  

############################################



class VideosUpdate(UpdateView):
  def render(self,request,pk_id):
    # thumbpath = Path(settings.EXTERNAL_ROOT) 
    # thumbpath.mkdir(parents=True, exist_ok=True)
    # thumbpath_str = str(thumbpath)

    # fs=FileSystemStorage(location=thumbpath_str) 
    print("inside render function",pk_id)
    if (pk_id==0):
       get_video=VideoFiles.objects.all()
    else:
      get_video=VideoFiles.objects.get(id=pk_id)
    form=VFiles(instance=get_video)
    context={'form':form}
    return render(request,'templates/dms/VideosUpdate.html',context)

  
  def get(self,request,pk_id):
    print("inside get function",pk_id)
    if (pk_id==0):
       get_video=VideoFiles.objects.all()
    else:
      get_video=VideoFiles.objects.get(id=pk_id)

    form=VFiles(instance=get_video)
    
    context={'form':form}
    return render(request,'templates/dms/VideosUpdate.html',context)

  def post(self,request,pk_id):
    update_video=VideoFiles.objects.get(id=pk_id)
    update_video.videostatus="Modified"
    print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
    self.form=VFiles(request.POST,request.FILES,instance=update_video)
    print("request.FILES", request.FILES)
    print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
    if self.form.is_valid():

        # # deleting old uploaded images.
        # image1_path = update_video.Image1.path
        # if os.path.exists(image1_path):
        #     os.remove(image1_path)

        # image2_path = update_video.Image2.path
        # if os.path.exists(image2_path):
        #     os.remove(image2_path)

        # image3_path = update_video.Image3.path
        # if os.path.exists(image3_path):
        #     os.remove(image3_path) 

        ### save updated form details      
        self.form.save()
        auditdata('VideoFiles','Update','Admin')  ###adding to the auditlog ###
        return redirect('success_url')
    else:
      if (pk_id==0):
        update_video=VideoFiles.objects.all()
      else:
        update_video=VideoFiles.objects.get(id=pk_id)
      self.form=VFiles(request.POST,instance=update_video)
      print("not valid", self.form)
      return self.render(request,pk_id)

def VideosApprovalRejection(request):
  print("inside VideosApprovalRejection ",request.method)
  print("inside VideosApprovalRejection ",request.FILES)
  if request.method=="POST":
      id1 = request.POST.get('id', None)
      print("RECORD ID",id1)
      vidstatus=request.POST.get("videostatus")
      print("VIDEO STATUS",vidstatus)
      if vidstatus == "Rejected":
        print("inside Rejected ")
        RejectedReason=request.POST.get("RejectedReason")
        updatevideodet1 = VideoFiles.objects.filter(id = id1).update(videostatus=vidstatus,RejectedReason=RejectedReason)
        auditdata('VideoFiles','Rejected','Admin')  ###adding to the auditlog ###
        print('updatevideodet',updatevideodet1)
      if vidstatus == "Approved":
        print("inside Approval ")
        updatevideodet2 = VideoFiles.objects.filter(id = id1).update(videostatus=vidstatus)
        auditdata('VideoFiles','Rejected','Admin')  ###adding to the auditlog ###
        print('updatevideodet',updatevideodet2)
      # updatevideodet.videostatus=request.POST.get("videostatus")
      
      
      # print('getting videostatus',request.POST.get('videostatus'))
      
      form = VFiles()
      all_Videos = VideoFiles.objects.all()
      context={'all_Videos':all_Videos,'form':form}
      data = {'context':context}
      return render(request,'templates/dms/ApproveRejectVideo.html',context)
      # return JsonResponse(data)
      # return redirect('success_url')
  else:
    print('GET GET GET')
    sort_params={}
    set_if_not_none(sort_params, 'videostatus', 'New')
    set_if_not_none(sort_params, 'videostatus', 'Modified')
    print(sort_params)
    all_Videos=VideoFiles.objects.filter(**sort_params)
    print(all_Videos.count())
    form = VFiles()
    context={'all_Videos':all_Videos,'form':form}   

    return render(request,'templates/dms/ApproveRejectVideo.html', context)  




#videalgo page icoForm()
def ico(request):
  print("$$$$$$$",request.POST)
  if request.method=='POST':
        form = icoForm(request.POST)
        print(request.FILES)
        if form.is_valid():
            form.save()
        #   return render(request, "templates/ico.html", context)
            BaseUrl = "http://10.0.0.2:8002"
            url = f'{BaseUrl}/api/video_to_frame/'
            data = {
    'video_path': '/datavolume/Servershare/intern/label/videos/test_video.mp4', 
    'weight_path': '/datavolume/Servershare/intern/label/weigths/freshtrain.pt',
    'output_path': '/datavolume/Servershare/intern/label/test',
    'skip_frame_rate': 4,
}
            print(data)
            data = json.dumps(data)
            headers = {'Accept' : 'application/json', 'Content-Type' : 'application/json'}
            response = requests.post(url, data=data, headers=headers)
            print(response)
            print (response.text)
            context={ 'form': form,"response":response}
            return render(request, "templates/dms/apisuccess.html",context)


  else:
    print("get method")
    form = icoForm()
    all_companies= Company.objects.all()
    all_projects = Project.objects.all()
    all_locations = Location.objects.all()
    VideoFile = VideoFiles.objects.all()
  # Algorithm=algo.objects.all()
 
    context = {
              'all_companies': all_companies,
          'all_projects': all_projects,
          'all_locations': all_locations,
          'VideoFile': VideoFile,
          # 'Algorithm':Algorithm,
          'form': form,
                          }
    return render(request, "templates/ico.html", context)

 #tags adding  anoForm()
def anot(request):
    print("$$$$$$$",request.POST)
    if request.method == 'POST':
      form = anoForm(request.POST)
      # print(request.FILES)
      if form.is_valid():
      
       form.save()
       return redirect('success_url')
      else:
       form = anoForm()
       return render(request, 'templates/anot.html')   
    else:
      print("get method")
      form = anoForm()
      all_anof=anof.objects.all()
      context = {

            
              'all_anof':all_anof,
          
             'form': form,

                 }
      return render(request, "templates/anot.html",context) 

def icotable(request):   
 
  all_anof=icotest.objects.all()
  context={'all_anof':all_anof}
  return render(request, 'templates/dms/vatab.html',context)    
#tags  anoForm()
# def modifytags(request):
#    if request.method == "POST":
#     form = anoForm(request.POST)
#     if form.is_valid():
#       form.save()
#       return redirect('success_url')
#     else:
#         form = anoForm()
#         return render(request, 'templates/dms/modifytags.html', {'form': form})
#    else:
#     all_anof=anof.objects.all()
#     context={'all_anof':all_anof}
    
#     return render(request,'templates/dms/modifytags.html', context)
  
  #tags update       anoForm()
  
class tagsupdate(UpdateView):
  
  def render(self,request,pk_id):
    get_ta=anof.objects.get(id=pk_id)
    form=anoForm(instance=get_ta)
    context={'form':form}
    return render(request,'templates/dms/uptags.html',context)

  def get(self,request,pk_id):
    get_ta=anof.objects.get(id=pk_id)
    form=anoForm(instance=get_ta)
    context={'form':form}

    return render(request,'templates/dms/uptags.html', context)

  def post(self,request,pk_id):
    update_ta=anof.objects.get(id=pk_id)
    self.form=anoForm(request.POST,instance=update_ta)
    if self.form.is_valid():
      self.form.save()
      return render(request,'templates/anot.html')

      # return redirect('success_url')
    else:
      return self.render(request)  
  
  #table          anoForm()
def display(request):   
 
  all_anof=anof.objects.all()
  context={'all_anof':all_anof}
  return render(request, 'templates/display.html',context) 
 
def ico2(request):
     if request.method == 'POST':
       form = anotForm(request.POST)
       if form.is_valid():
         form.save()
         BaseUrl = "http://10.0.0.2:8002"
         url = f'{BaseUrl}/api/modify_annotations/'
         input_folder_path = request.POST.get('input_folder_path')
         type_of_process = request.POST.get('type_of_process')
         class_names = {
             "auto_rickshaw": ["auto_rickshaw"],
             "bus": ["school _bus"],
             "car": ["c1","c1","c2","c3","c4","c5","c6","c7","c8"],
             "others(earth mover)": ["earthvehicle","others(earth)"],
             "lcv": ["l1","l2","l3","l4","l5","l6","L2"],
             "mini bus": ["minibusM1","minibusM2","mini bus","mini_bus"],
             "Two Wheeler": ["Two","Two Wheeler","two Wheeler","motor_cycle","motor_cycle","motorcycle"],
             "multi axle": ["tl1","tl2","tl3","multi"],
             "tmav_3axle": ["3"],
             "tmav_4axle": ["4"],
             "tmav_6axle": ["6"],
             "tracktor": [],
             "tracktor_trailer": ["tractor_wot","tractor_wt"],
             "ttav2": ["truck_tav","2"],
             "van": ["v1","v2","v3","v6"],
             "Foreign truck": []
         }

         if type_of_process == 'add_id':
           
             url = f'{BaseUrl}/api/modify_annotations/'
             data = {
                 "input_folder_path": input_folder_path,
                 "type_of_process": "add_id",
                 "class_names": class_names
             }
             response = requests.post(url, data=json.dumps(data), headers={'Content-Type': 'application/json'})
             return redirect('addid_url')
        
         elif type_of_process == 'remove_id':
             url = f'{BaseUrl}/api/modify_annotations/'
             data = {
                 "input_folder_path": input_folder_path,
                 "type_of_process": "remove_id",
                 "class_names": class_names
             }
             response = requests.post(url, data=json.dumps(data), headers={'Content-Type': 'application/json'})
             return redirect('remid_url')
            
            
         elif type_of_process == 'rename':
             url = f'{BaseUrl}/api/modify_annotations/'
             data = {
                 "input_folder_path": input_folder_path,
                 "type_of_process": "rename",
                 "class_names": class_names
             }
             response = requests.post(url, data=json.dumps(data), headers={'Content-Type': 'application/json'})
             return redirect('ren_url')
        
         elif type_of_process == 'crop_image':
             url = f'{BaseUrl}/api/modify_annotations/'
             data = {
                 "input_folder_path": input_folder_path,
                 "type_of_process": "crop_image",
                 "class_names": class_names
             }
             try:
               response = requests.post(url, data=json.dumps(data), headers={'Content-Type': 'application/json'})
               json_data = response.json()
               return redirect('crop_url')
             except Exception as json_data:
              json_data = { "add id first"}
              #return JsonResponse(json_data)
              response= HttpResponse(f'Error: {json_data}')
              return response
            #  except Exception as e:
            #    json_data = {"err": "add id first"}
            #    return JsonResponse(json_data)
              #  return redirect('errc_url')
       
         else:
             return JsonResponse({'error': 'Invalid process type'})

     else:
         print("form not valid")
         form = anotForm()
         return render(request, 'templates/ico2.html', {'form': form})
  
         

 
def convert_xml_files(myroot_dir,txt_dir):
   
    for root, dirs, files in os.walk(myroot_dir):
        for filename in files:
            if filename.endswith('.xml'):
                xml_path = os.path.join(root, filename)
                txt_path = os.path.join(txt_dir, os.path.splitext(filename)[0] + '.txt')
                                
                # Load the XML file and extract the text
                tree = ET.parse(xml_path)
                xml_text = ET.tostring(tree.getroot(), encoding='unicode', method='text')
                
                # Save the text to a TXT file
                with open(txt_path, 'w') as f:
                    f.write(xml_text)

def xmt(request):
    if request.method == 'POST':
        form = xmtx(request.POST)
        if form.is_valid():
            myroot_dir = form.cleaned_data['myroot_dir']
            txt_dir = form.cleaned_data['txt_dir']
            # Convert all XML files in the root directory and its subdirectories to TXT
            convert_xml_files(myroot_dir,txt_dir)
            form.save() 
            # Display a success message
            return redirect('xmtx_url')
            # return redirect('success_url')
    else:
          form = xmtx()
    
    context = {'form': form}
    return render(request, 'templates/dms/xmt.html', context)
 
 
 
 
  

def extract_features(image_path):
   
    img = Image.open(image_path)
    img = img.resize((256, 256))
    arr = np.array(img)
    feature_vector = arr.flatten()
    return feature_vector

    
  
def clust1(request):
  if request.method == 'POST':
        form = dupl(request.POST)
        if form.is_valid():
        # Get the directory path from the form data
         image_dir = form.cleaned_data['image_dir']
         print("image_dir",image_dir)
        # Set the number of clusters and the outlier detection parameters
        n_clusters = 1
        lof_contamination = 0.1

        # Loop through each subdirectory and find outliers within each cluster
        for subdir in os.listdir(image_dir):
            subdir_path = os.path.join(image_dir, subdir)
            if os.path.isdir(subdir_path):
                print(f"Finding outliers in {subdir}...")
                
                # Load the images and extract features
                image_paths = [os.path.join(subdir_path, f) for f in os.listdir(subdir_path)]
                features = []
                for image_path in image_paths:
                    features.append(extract_features(image_path))
                X = np.array(features)

                # Cluster the images
                kmeans = KMeans(n_clusters=n_clusters)
                labels = kmeans.fit_predict(X)

                # Find outliers within each cluster
                for i in range(n_clusters):
                    cluster_indices = np.where(labels == i)[0]
                    cluster_features = X[cluster_indices]

                    # Use Local Outlier Factor to detect outliers within the cluster
                    n_neighbors = min(20, len(cluster_features) - 1)
                    lof = LocalOutlierFactor(contamination=lof_contamination)
                    lof.fit(cluster_features)
                    outlier_indices = np.where(lof.fit_predict(cluster_features) == -1)[0]
                    outlier_paths = [image_paths[cluster_indices[j]] for j in outlier_indices]

                    # Move the outliers to a separate folder
                    if len(outlier_paths) > 0:
                        outlier_dir = os.path.join(image_dir, 'outliers', subdir, f'cluster_{i}')
                        os.makedirs(outlier_dir, exist_ok=True)
                        for path in outlier_paths:
                            shutil.move(path, os.path.join(outlier_dir, os.path.basename(path)))
                        # Python program to explain shutil.copy() method
                    # source="/datavolume/Servershare/intern/"
                    # destination="/datavolume/Servershare/intern/"
                    
                    # try:
                    #   shutil.copy(image_dir, image_dir)
                    #   print("File copied successfully.")

                    # # If source and destination are same
                    # except shutil.SameFileError:
                    #   print("Source and destination represents the same file.")

                    # If there is any permission issue
                    

        # Render the success message and the form again
        # success_message = "Outliers have been moved to the 'outliers' folder."
        form.save()
#         url = 'http://10.0.0.2:8002/api/filter_images/'

#         data = {
#     "input_folder_path": "/datavolume/Servershare/intern/label/output/Cropped_Images/",
# }

#         data = json.dumps(data)
#         headers = {'Accept' : 'application/json', 'Content-Type' : 'application/json'}
#         response = requests.post(url, data=data, headers=headers)
#         print(response.json())
        return HttpResponse(f'<div style="background-color:#4CAF22;color:white;padding:20px;border-radius:5px;text-align:center;font-size:20px;font-weight:bold;">Outliers moved successfully</div>') 
        # return HttpResponse("Outliers moved successfully")
        # return render(request, 'templates/clust1.html', {'success_message': success_message})
  else:
    form = dupl()
    
  context = {'form': form}
    # If the request method is GET, render the form
  return render(request, 'templates/clust1.html',context)


    
  

 
  

  
    
  
 
