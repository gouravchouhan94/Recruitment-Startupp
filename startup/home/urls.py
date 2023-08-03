from django.urls import path, include
from .views import app


urlpatterns = [
    
    path("" , app, name="home")
    # ... the rest of your URLconf goes here ...
 
   
]