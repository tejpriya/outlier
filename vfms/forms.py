from django import forms
from .models import *
from taggit.forms import TagWidget
#from django_filebrowser.widgets import FileBrowseWidget
class MyForm(forms.ModelForm): #company model form
  class Meta:
    model = Company
    fields=['name','address','phone','email',]

class ProjForm(forms.ModelForm):  #project model form
  class Meta:
    model = Project
    fields=['company','name',]

class LocationForm(forms.ModelForm): #location/station model form
  class Meta:
    model = Location
    fields=['project','name',
           
            ]


class CModelForm(forms.ModelForm): #cameramodel model form
    class Meta: 
      model =  CameraModel
      fields=['name',]

class CPositionForm(forms.ModelForm): #camerapostion model form
    class Meta: 
      model =  CameraPosition
      fields=['CHeight','Cview',]


class UserForm(forms.ModelForm): #user model form
  class Meta:
    model = User
    fields=['name','password','loginID','phone','email','company','role']


class RoleForm(forms.ModelForm): #Roles model form
    class Meta: 
      model =  Role
      fields=['name',]

class VideoFileForm(forms.ModelForm): #Video File Formats model form
    class Meta: 
      model =  VideoFF
      fields=['vtype',]
      # 'algorithm',]

class LIForm(forms.ModelForm): #Light Intensity model form
    class Meta: 
      model =  LItypes
      fields=['LItype',]



class VFiles(forms.ModelForm): #video files
    class Meta: 
      model =  VideoFiles
      videostatus = forms.CharField(widget=forms.HiddenInput())
      RejectedReason= forms.CharField(widget=forms.HiddenInput())
      fields=['CompanyName',
              'ProjectName',
              'StationName',
              'CameraNo',
              'CModel',
              'CHeight',
              'CView',
              'VideoStartTime',
              'VideoEndTime',
              'LICate',
              'VideoFormat',
              # 'Image1',
              # 'Image2',
              # 'Image3',
              'FileName',
              'VideoFile',
              'Remarks',
             
              ]

# class alg(forms.ModelForm):
#   model=algo
#   fields=['Algorithm',
#           'Weight',
#           ]    

class alg1(forms.ModelForm):
    models=algo
    fields=['Algorithm',
    ]
# class wei(forms.ModelForm):
#     models=wei
#     fields=['Weight',
# ]    

  
class icoForm(forms.ModelForm):
    # folder_path = forms.CharField(max_length=255, widget=FileBrowseWidget())
    # files = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}))

      #folder_path = forms.CharField(max_length=255, widget=forms.FileInput(attrs={'webkitdirectory': True}))
      #save_location = forms.FileField(widget=forms.ClearableFileInput(attrs={'webkitdirectory': True})) 
     class Meta: 
          model = icotest
          

          fields=['CompanyName',
                  'ProjectName',
                  'StationName',
                  'VideoFile',
                #  'VideoFile1',
                  'Algorithm', 
                  'Weight',
                  'Skipcount'
          ]
          #exclude =['folder_path']


                  

class VehicleForm(forms.ModelForm):
    class Meta:
        model = Vehicle
        fields = ['vehi',] 
        
class anoForm(forms.ModelForm):
   vehi = forms.ModelChoiceField(Vehicle.objects.all())
   tags = forms.CharField(widget=forms.TextInput(attrs={'data-role': 'tagsinput','style': 'width: 200px !important;'}))
   class Meta:
     model=anof                 
     fields=['vehi','tags',] 
     
class typ(forms.ModelForm):
     
     class Meta:
       model=proc
       fields=['protype',]
       
class anotForm(forms.ModelForm):
  class_names = forms.ModelChoiceField(Vehicle.objects.all())
  input_folder_path=forms.CharField(max_length=255)
  tag=forms.ModelChoiceField(anof.objects.all())
  # TagifyCustomInlineSuggestion=forms.CharField(widget=TagWidget(attrs={'placeholder': 'Enter tags'}))  # processtype=forms.ModelChoiceField(proc.objects.all())
  type_of_process = forms.ChoiceField(choices=[("add_id", "ADDID"), ("rename", "RENAME"), 
                                           ("crop_image", "CROP"), ("remove_id", "REMOVEID")], 
                                  widget=forms.Select(attrs={"class": "form-control", "id": "api-select",'style': 'width: 330px;' 'opacity: 0.5;'}))

  class Meta:
      model=anott
      fields=['input_folder_path',
              'class_names',
              'tag',
              # 'TagifyCustomListSuggestion',
              # 'TagifyCustomInlineSuggestion',
              'type_of_process',]   
      

# class dup(forms.ModelForm):
  #  source_folder = forms.FileField(label='Source Folder', widget=forms.FileInput(attrs={'directory': True}))
  #  destination_folder = forms.FileField(label='Destination Folder', widget=forms.FileInput(attrs={'directory': True}))
  # dropzone= forms.FileField(upload_to='upload/',null=True,storage=fs)
   
  #  class Meta:
  #   model=dups
  #   fields=['cropped_images_path','moving_path']
  #   cropped_images_path = forms.CharField(max_length=300)
  #   moving_path = forms.CharField(max_length=300)
    # fields=['source_folder',
    #        'destination_folder', ]
    


class dupl(forms.ModelForm):
   image_dir = forms.CharField(max_length=300)
  #  mov_dir = forms.CharField(max_length=300)
  #  threshold=forms.IntegerField(label='Threshold')
   class Meta:
     model=clus
     fields=['image_dir']
     
            #  , 'mov_dir',]
    #  'threshold']
    
    #  def clean(self):
    #     cleaned_data = super().clean()
    #     img_dir = cleaned_data.get('img_dir')
    #     mov_dir = cleaned_data.get('mov_dir')
    #     # threshold = cleaned_data.get('threshold')

    #     # Check if the image directory exists
    #     if not os.path.exists(img_dir):
    #         raise forms.ValidationError('Image directory does not exist')

    #     # Check if the duplicate directory exists, create it if it doesn't
    #     if not os.path.exists(mov_dir):
    #         os.makedirs(mov_dir)

    #     return cleaned_data
    
   
 
class xmtx(forms.ModelForm):
  class Meta:
    model=conv
    fields=['myroot_dir',
             'txt_dir']    
    root_dir = forms.CharField(max_length=300)
    txt_dir = forms.CharField(max_length=300)