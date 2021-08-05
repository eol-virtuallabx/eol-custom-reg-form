"""
LABX URLS
"""
from django.conf import settings
from django.conf.urls import include, url
from django.urls import path
from . import api

urlpatterns = [
    path('v1/validate_rut_caja/<str:rut>', api.validate_rut_caja , name='validate_rut_caja'),
]

