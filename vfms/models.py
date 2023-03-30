from django.db import models
from django.conf import settings
from pathlib import Path
import os
from django.core.files.storage import FileSystemStorage


# Create your models here.
#company model
class Company(models.Model):
    name=models.CharField(max_length=200,null=True)
    address=models.CharField(max_length=500,null=True)
    phone=models.CharField(max_length=200,null=True)
    email=models.EmailField(null=True)
    date_created=models.DateTimeField(auto_now_add=True)
    date_updated=models.DateField(auto_now=True)
   

    #function to display acutal customer/company name 
    def __str__(self):
        return self.name

#Project  model
class Project(models.Model):
    name=models.CharField(max_length=200,null=True)
    company=models.ForeignKey(Company,on_delete=models.PROTECT, null=True)
    date_created=models.DateTimeField(auto_now_add=True)
    date_updated=models.DateField(auto_now=True)


    #function to display acutal project name 
    def __str__(self):
        return self.name


#Location  model
class Location(models.Model):
    name=models.CharField(max_length=200,null=True)
    project=models.ForeignKey(Project,on_delete=models.PROTECT,null=True)
    date_created=models.DateTimeField(auto_now_add=True)
    date_updated=models.DateField(auto_now=True)
  

#function to display acutal location name 
    def __str__(self):
        return self.name


#Camera Model types   model
class CameraModel(models.Model):
    name=models.CharField(max_length=200,null=True)
    date_created=models.DateTimeField(auto_now_add=True)
    date_updated=models.DateField(auto_now=True)


#function to display acutal location name 
    def __str__(self):
        return self.name



#Camera Position  types   model
class CameraPosition(models.Model):
    CHeight=models.FloatField(max_length=200,null=True)
    Cview=models.CharField(max_length=200,null=True)
    date_created=models.DateTimeField(auto_now_add=True)
    date_updated=models.DateField(auto_now=True)


#function to display acutal camera Position  
    def __str__(self):
        return (str(self.CHeight) + "__" + str(self.Cview))

#User  Roles
class Role(models.Model):
    name=models.CharField(max_length=200,null=True)
    date_created=models.DateTimeField(auto_now_add=True)
    date_updated=models.DateField(auto_now=True)


    #function to display acutal customer/company name 
    def __str__(self):
        return self.name

#User  model
class User(models.Model):
    name=models.CharField(max_length=200,null=True)
    loginID=models.CharField(max_length=200,null=True)
    password=models.CharField(max_length=200,null=True)
    phone=models.CharField(max_length=200,null=True)
    email=models.EmailField(null=True)
    company=models.ForeignKey(Company,on_delete=models.PROTECT, null=True)
    role=models.ForeignKey(Role,on_delete=models.PROTECT,null=True)
    date_created=models.DateTimeField(auto_now_add=True)
    date_updated=models.DateField(auto_now=True)


    #function to display acutal customer/company name 
    def __str__(self):
        return self.name

#Video File format  types   
class VideoFF(models.Model):
    vtype=models.CharField(max_length=200,null=True)
    # algorithm=models.CharField(max_length=200)
    date_created=models.DateTimeField(auto_now_add=True)
    date_updated=models.DateField(auto_now=True)


#function to display acutal location name 
    def __str__(self):
        return self.vtype

#Light Intensity  types   
class LItypes(models.Model):
    Timings=( 
            ("Day","Day"),
            ("Mid-day","Mid-day"),
            ("Mid-Evening","Mid-Evening"),
            ("Night","Night"),
           
            # ("EarlyMorning","EarlyMorning"),
            )
            
 
    LItype=models.CharField(max_length=200,null=True,choices=Timings)
    date_created=models.DateTimeField(auto_now_add=True)
    date_updated=models.DateField(auto_now=True)


#function to display acutal location name 
    def __str__(self):
        return self.LItype


thumbpath = Path(settings.DRIVE_ROOT) 
thumbpath.mkdir(parents=True, exist_ok=True)
thumbpath_str = str(thumbpath)

fs=FileSystemStorage(location=thumbpath_str) 
class VideoFiles(models.Model):
    vstatus=( 
            ("New","New"),
            ("Approved","Approved"),
            ("Rejected","Rejected"),
            ("Modified","Modified"),
            )

    CompanyName=models.ForeignKey(Company,on_delete=models.DO_NOTHING, default=1)
    ProjectName=models.ForeignKey(Project,on_delete=models.DO_NOTHING,default=1)
    StationName=models.ForeignKey(Location,on_delete=models.DO_NOTHING,default=1)
    CameraNo=models.IntegerField(default=1)
    CModel=models.ForeignKey(CameraModel,on_delete=models.DO_NOTHING,default=1)
    CHeight=models.FloatField(null=True)
    CView=models.CharField(max_length=20,null=True)
    VideoStartTime=models.TimeField(null=True)
    VideoEndTime=models.TimeField(null=True)
    LICate=models.ForeignKey(LItypes,on_delete=models.DO_NOTHING,default=1)
    VideoFormat=models.ForeignKey(VideoFF,on_delete=models.PROTECT,null=True)
    # Image1=models.ImageField(upload_to='ThumbNailImages/',null=True, storage=fs)
    # Image2=models.ImageField(upload_to='ThumbNailImages/',null=True, storage=fs)
    # Image3=models.ImageField(upload_to='ThumbNailImages/',null=True, storage=fs)
    FileName=models.CharField(max_length=200,null=True)
    VideoFile=models.FileField(upload_to='UploadedVideos/',null=True,storage=fs)
    Remarks=models.CharField(max_length=1000,null=True)
    RejectedReason=models.CharField(max_length=1000,null=True,default='NA')
    videostatus=models.CharField(max_length=10,default='New',choices=vstatus)

    def __str__(self):
        return self.FileName

class AuditLog(models.Model):
    form_name=models.CharField(max_length=200)
    action_performed=models.CharField(max_length=200)
    acted_by=models.CharField(max_length=200,default='Admin')
    acted_on=models.DateTimeField(auto_now_add=True)
    
thumbpath = Path(settings.DRIVE_ROOT) 
thumbpath.mkdir(parents=True, exist_ok=True)
thumbpath_str = str(thumbpath)

fs=FileSystemStorage(location=thumbpath_str)  
 
class algo(models.Model):
    Algorithm=models.CharField(max_length=200)
    
    def __str__(self):
         return self.Algorithm
     

class wei(models.Model): 
    Weight=models.CharField(max_length=200)
   
    def __str__(self):
        return self.Weight
class ico1(models.Model):
    # Algorithm=models.CharField(max_length=20,default=None,null=True,blank=True) 
    # Weight=models.CharField(max_length=200,default=None,null=True,blank=True)
    CompanyName=models.ForeignKey(Company,on_delete=models.DO_NOTHING)
    ProjectName=models.ForeignKey(Project,on_delete=models.DO_NOTHING)
    StationName=models.ForeignKey(Location,on_delete=models.DO_NOTHING)
    VideoFile=models.ForeignKey(VideoFiles,on_delete=models.DO_NOTHING)
    # Weight=models.ForeignKey(wei,on_delete=models.DO_NOTHING)
    # Algorithm=models.ForeignKey(alg1,on_delete=models.DO_NOTHING)
    def __str__(self):
        return str(self.ProjectName) + " " + str(self.StationName) + " " + str(self.CompanyName) + " " + str(self.VideoFile)
    

    # Weight=models.ForeignKey(wei,on_delete=models.DO_NOTHING)
    # Algorithm=models.ForeignKey(alg,on_delete=models.DO_NOTHING)
    
       #return self.ProjectName+" "+self.StationName+" "+self.CompanyName+" "+self.VideoFile

class icotest(models.Model):
   
    CompanyName=models.ForeignKey(Company,on_delete=models.DO_NOTHING)
    ProjectName=models.ForeignKey(Project,on_delete=models.DO_NOTHING)
    StationName=models.ForeignKey(Location,on_delete=models.DO_NOTHING)
    VideoFile=models.ForeignKey(VideoFiles,on_delete=models.DO_NOTHING)
    # VideoFile1=models.FileField(upload_to='UploadedVideos/',null=True,storage=fs)
    Algorithm=models.CharField(max_length=20,default=None,null=True,blank=True)
    # Algorithm=models.ForeignKey(algo,on_delete=models.CASCADE) 
    Weight=models.CharField(max_length=200,default=None,null=True,blank=True)
    Skipcount=models.CharField(max_length=200,default=None,null=True,blank=True)
# class tag1(models.Model):
  
#    tagify_options=models.CharField(max_length=255)

# master
class Vehicle(models.Model):
   vehi = models.CharField(max_length=255,default=None,null=True,blank=True)
   def __str__(self):
        return self.vehi

#  fetching  
class anof(models.Model):
   vehi=models.ForeignKey(Vehicle,on_delete=models.DO_NOTHING,blank=True, null=True)
   tags = models.CharField(max_length=255, blank=True, null=True,unique=True)
   def __str__(self):
        return str(self.tags) + " "
   
#    def __str__(self):
#         if self.tags:
#             return self.tags
#         else:
#             return ''
class proc(models.Model):
    protype=models.CharField(max_length=255,default=None)
    def __str__(self):
        return str(self.protype) + " " 
class anott(models.Model):
    input_folder_path=models.CharField(max_length=255,default=None,null=True)
    class_names=models.ForeignKey(Vehicle,on_delete=models.DO_NOTHING)
    # TagifyCustomListSuggestion=models.CharField(max_length=255,default=None,null=True)
    # TagifyCustomInlineSuggestion=models.CharField(max_length=255,default=None,null=True)
    tag=models.ForeignKey(anof,on_delete=models.DO_NOTHING) 
    ADDID = 'add_id'
    RENAME = 'rename'
    CROP = 'crop_image'
    REMOVEID = 'remove_id'
    PROCESS_CHOICES = [
        (ADDID, 'Add ID'),
        (RENAME, 'Rename'),
        (CROP, 'Crop'),
        (REMOVEID, 'Remove ID'),
    ]
    type_of_process = models.CharField(max_length=10,choices=PROCESS_CHOICES)
    
    # processtype=models.ForeignKey(proc,on_delete=models.DO_NOTHING)
   
    
# , related_name='tags'
class clus(models.Model):
    # mov_dir=models.CharField(max_length=300)
    image_dir=models.CharField(max_length=300)
    # threshold=models.IntegerField(unique=True,null=True)                   


class conv(models.Model):
     myroot_dir = models.CharField(max_length=300)
     txt_dir = models.CharField(max_length=300)