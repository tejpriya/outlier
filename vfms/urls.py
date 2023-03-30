from .index import *

from django.conf import settings
from django.conf.urls.static import static


from vfms import views

from vfms.models import *

from django.urls import path , include

from django.views.generic import CreateView,ListView

urlpatterns = [
    #common urls
    path("", page,name="home" ),
    path("SuccessMessage/",successpage,name="success_url"),
    path("WorkInProgress/",WorkInProgress,name="WorkInProgress"),
    path("ErrorMessage/",successpage,name="Error_url"),
    path("Dashboard/", views.dashboarddata,name='dashboarddata'),
    
    path("apis/",apisuc,name="apisuccess_url"),
    path("addid/",addid,name="addid_url"),
    path("remid/",remid,name="remid_url"),
    path("errc/",errc,name="errc_url"),
    path("ren/",ren,name="ren_url"),
    path("crop/",crop,name="crop_url"),
    path("xmtx/",xmtx,name="xmtx_url"),
    #rolebased [Menulevel] access urls
    path("Admin_Home/",AdminMenu,name="AdminMenu"),
    path("Approver_Home/",ApproverMenu,name="ApproverMenu"),
    path("User_Home/",UserMenu,name="UserMenu"),

    #company relevant urls
    path("ListCompany/", views.ListCompany.as_view(),name='ListCompany'),
    path('AddCompany', views.my_form, name='AddCompany'),
    path('ModifyCompany', views.edit_form, name='ModifyCompany'),
    path('Companyupdate/<int:pk_id>/',views.CompanyUpdate.as_view(),name='Companyupdate'),

    #project relevant urls
    path("ListProject/", views.ListProject.as_view(),name='ListProject'),
    path("AddProject/", views.project_form,name='AddProject'),
    path("ModifyProject/",views.editproj_form,name='ModifyProject'),
    path("ProjectUpdate/<int:pk_id>/",views.ProjectUpdate.as_view(),name='UpdateProject'),
    

    #station/Location relevant urls
    path("ListStation/", views.ListStation.as_view(),name='ListStation'),
    path("AddStation/", views.station_form,name='AddStation'),
    path("ModifyStation/",views.editstn_form,name='Modifytation'),
    path("StationUpdate/<int:pk_id>/",views.StationUpdate.as_view(),name='UpdateStation'),


    #Camera Models relevant urls
    path("ListCameraModel/", views.ListcModel.as_view(),name='ListCameraModel'),
    path("AddCameraModel/", views.Cmodel_form,name='AddCameraModel'),
    path("ModifyCameraModel/",views.editcModel_form,name='ModifyCameraModel'),
    path("UpdateCameraModel/<int:pk_id>/",views.CModelUpdate.as_view(),name='UpdatecModel'),


    #Camera Positions relevant urls
    path("ListCameraPosition/", views.ListcPosition.as_view(),name='ListCameraPosition'),
    path("AddCameraPosition/", views.CPosition_form,name='AddCameraPosition'),
    path("ModifyCameraPosition/",views.editcPosition_form,name='ModifyCameraPosition'),
    path("UpdateCameraPosition/<int:pk_id>/",views.CPositionUpdate.as_view(),name='UpdatecPosition'),



    #User Profile relevant urls
    path("ListUser/", views.ListUser.as_view(),name='ListUser'),
    path("AddUser/", views.add_user,name='AddUser'),
    path("ModifyUserProfile/",views.edit_user,name='ModifyUserProfile'),
    path("UpdateUserProfile/<int:pk_id>/",views.UserProfileUpdate.as_view(),name='UpdateUserProfile'),

    #User Roles relevant urls
    path("ListRole/", views.ListRole.as_view(),name='ListRole'),
    path("AddRole/", views.add_role,name='AddRole'),
    path("ModifyRole/",views.edit_role,name='ModifyRole'),
    path("UpdateRole/<int:pk_id>/",views.RoleUpdate.as_view(),name='UpdateRole'),

    ################# Video File Format ###############

    #Video Formats
    path("ListVideoFormat/", views.ListVFF.as_view(),name='ListVideoFormat'),
    path("AddVideoFormat/", views.add_vff,name='AddVideoFormat'),
    path("ModifyVideoFormat/",views.edit_vff,name='ModifyVideoFormat'),
    path("UpdateVideoFormat/<int:pk_id>/",views.VFFUpdate.as_view(),name='UpdateVideoFormat'),

    #Light Intensity
    path("ListLightIntensity/", views.ListLI.as_view(),name='ListLightIntensity'),
    path("AddLightIntensity/", views.add_li,name='AddLightIntensity'),
    path("ModifyLightIntensity/",views.edit_li,name='ModifyLightIntensity'),
    path("UpdateLightIntensity/<int:pk_id>/",views.LIUpdate.as_view(),name='UpdateLightIntensity'),

    ####### video files upload #####################
    path("ListVideos/", views.ListVideos.as_view(),name='ListVideos'),
    path("AddVideo/", views.Videos_form,name='AddVideo'),
    path("ModifyVideo/",views.editvideos_form,name='ModifyVideo'),
    path("UpdateVideo/<int:pk_id>/",views.VideosUpdate.as_view(),name='UpdateVideo'),
   
    path("ApproveRejectVideos/",views.VideosApprovalRejection,name='ApproveRejectVideos'),
    

      path("tagsupdate/<int:pk_id>/",views.tagsupdate.as_view(),name='tagsupdate'),
    ## filtering process of Videod file upload
    path("get_projects/", views.GetProjects.as_view(),name='get_projects'),
    path("get_stations/", views.GetLocations.as_view(),name='get_stations'),  
   #hide 
   path("get_videos/",views.GetVideoFiles.as_view(),name='get_videos'),
 
 
       #videalgo page icoForm()
    path("ico/",views.ico,name='ico'),
    path("icotable/",views.icotable,name='icotable'),
         #annotations #tags adding  anoForm()
    path("anot/",views.anot,name='anot'),
         #table          anoForm()
    path("display/",views.display,name='display'),
         #annotation page  anotForm()   --add,rename,remove,crop
    path("ico2/",views.ico2,name='ico2'),
#     path("add_id/",views.add_id,name='add_id')
    # path("renam/",views.renam,name='renam'),
#     path("cropano/",views.cropano,name='cropano'),  
    path("clust1/",views.clust1,name='clust1'),
    path("xmt/",views.xmt,name='xmt'),
    path("get_vehicle/",views.GetVehicle.as_view(),name='get_vehicle'),
#     path("coun/",views.coun,name='coun')
  # path('my_view/', views.my_view, name='my_view'),
   # path("progress_view/",views.progress_view,name='progress_view'),

      
] 

""" 

"""

