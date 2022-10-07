from django.urls import path
from app.views import *

app_name='website'

urlpatterns = [

    path ('',home_page_view,name='index'),
    path ('languege/',language,name='language'),
    path ('education/',education,name='education'),
    path ('abilites/',abilites,name='abilites'),
    path ('projects/',projects,name='projects'),
    path ('contects_bio/',contects_bio,name='contects_bio'),
]