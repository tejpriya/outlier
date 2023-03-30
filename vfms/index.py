
# import http reponse library to return responses to the request we receive
from django .http import HttpResponse
# defining the welcome page


# render library import
from django.shortcuts import render

def page(request):
       
       return render(request,'templates/main_base.html')
        #return render(request,'F:\\Django\\Projects\\DMS\\templates\\dms\\index.html')

#redirectng to success url
def successpage(request):
         
    return render(request,'templates/dms/success.html')

#redirectng to workinprogress url
def WorkInProgress(request):
         
    return render(request,'templates/dms/WorkInProgress.html')

#redirectng to error url
def ErrorMessage(request):
         
    return render(request,'templates/dms/Error.html')

    #redirectng to Admin Menu url
def AdminMenu(request):
         
    return render(request,'templates/main_base.html')

#redirectng to Approver Menu url
def ApproverMenu(request):
         
    return render(request,'templates/approval_main.html')

#redirectng to User Menu url
def UserMenu(request):
         
    return render(request,'templates/user_home.html')
    
def apisuc(request):
    return render(request,'templates/apisuccess.html')

def addid(request):
    return render(request,'templates/dms/add.html')

def remid(request):
     return render(request,'templates/dms/rem.html')

def crop(request):
    return render(request,'templates/dms/crop.html') 

def errc(request):
     return render(request,'templates/dms/errc.html') 
 
def ren(request):
    return render(request,'templates/dms/rename.html') 

def xmtx(request):
     return render(request,'templates/dms/xmlsuc.html')