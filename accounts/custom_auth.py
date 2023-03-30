
from tempfile import TemporaryFile
from .models import Roles
from django.contrib.auth.backends import BaseBackend
from .models import UserAccount

def custom_login(request, user):
    request.session['user_id'] = user.id
    print("\n\n custom_login : ",user.id)
   

def show_data(request):
    try:
        user_id = request.session['user_id']
        user = UserAccount.objects.get(id = user_id)
    except:
        user = "unknown"
    print("\n\n\n Customauth : ",user)
    return {'custom_user':user}

def get_current_user(request):
    try:
        user_id = request.session['user_id']
        current_user = UserAccount.objects.get(id = user_id)
    except:
        current_user = None
    return current_user

def custom_logout(request):
    try:
        print("\n\n custom_logout1 : ",request.session['user_id'])
        del request.session['user_id']
        print("\n\n custom_logout2 : ",request.session['user_id'])
    except KeyError:
        pass

def custom_authenticate(username, password):
    try:
        print(username,password)
        m = UserAccount.objects.get(user_name=username)
        if m.user_password == password:
            print('pwd same')
            return m
    except UserAccount.DoesNotExist:
          return None

class CustomBackend(BaseBackend):

    def authenticate(self, request, username = None, password = None):
        try:
            m = UserAccount.objects.get(user_name=username)
            if m.user_password == password:
                return m
        except UserAccount.DoesNotExist:
            return None
    
    def get_user(self, user_id):
        try:
            return UserAccount.objects.get(pk = user_id)
        except:
            return None
