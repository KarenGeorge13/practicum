from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', index, name='home'),
    path('register/', register, name='register'),
    path('authen/', authen, name='authen'),
    path('profiles/<int:user_id>/', user_profile, name='profile'),
    path('logout/', user_logout, name='logout'),
    path('methodical_instructions/', methodical_instructions, name='methodical_instructions'),
    path('experiment/', experiment, name='experiment'),
    path('parameter-based-experiment/<int:parameter_id>/', parameter_based_experiment, name='parameter-based-experiment'),
    path('delete-parameter/<int:parameter_id>/', delete_parameter, name='delete-parameter')
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)