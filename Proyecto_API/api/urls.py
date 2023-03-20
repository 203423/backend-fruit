from django.urls import path, re_path
from django.conf.urls import include

# Importacion de vistas
from api.views import PredictsFruit 

urlpatterns = [
   re_path(r'^predecir/$', PredictsFruit.as_view()),
]