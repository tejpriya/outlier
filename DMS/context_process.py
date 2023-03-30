
from django.conf import settings

def media_path(request):
    return {
        # 'MEDIA': settings.MEDIA_URL,
        'EXTERNAL':settings.EXTERNAL_URL,
        'DRIVE':settings.DRIVE_URL,
            }
