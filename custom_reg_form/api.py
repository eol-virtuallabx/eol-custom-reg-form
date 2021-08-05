# -*- coding:utf-8 -*-
import logging
from django.conf import settings
from django.db import models
from django.views.decorators.csrf import ensure_csrf_cookie
from django.views.decorators.http import require_http_methods
from .models import ExtraInfo
from django.views.decorators.csrf import ensure_csrf_cookie, csrf_exempt
from django.contrib.auth.decorators import login_required
from util.json_request import JsonResponse
from django.http.response import HttpResponseBadRequest, HttpResponseForbidden,HttpResponseNotFound
from zeep import Client
from bs4 import BeautifulSoup
import re
import requests

log = logging.getLogger(__name__)

def validate_rut_caja(request,rut):
    try:
        if not request.method == 'GET':
            return HttpResponseNotFound()
        if not 'x-recaptcha-resp' in request.headers:
            return HttpResponseForbidden()
        recaptcha_test = requests.post("https://www.google.com/recaptcha/api/siteverify",data={'secret':settings.CAJA_ANDES.get('recaptchaSecret'),'response':request.headers.get('x-recaptcha-resp')})
        if not recaptcha_test.status_code == 200:
            return HttpResponseForbidden()
        resp_json = recaptcha_test.json()
        if not resp_json.get('success', None) :
            return HttpResponseForbidden()
        client = Client(settings.CAJA_ANDES.get('apiUrl'))
        data = client.service.requestPrestador(rutPrestador=settings.CAJA_ANDES.get('rutPrestador'),tipoPrestador=settings.CAJA_ANDES.get('tipoPrestador'),usuario=settings.CAJA_ANDES.get('usuario'),clave=settings.CAJA_ANDES.get('clave'),rutConsulta=re.sub('\DKk', '', rut))
        result = BeautifulSoup(data,'xml').find('codigoMensaje').string
        return JsonResponse({'result':True if result == '100' else False})
    except Exception as e:
        log.error(str(e))
        return HttpResponseBadRequest(u'Ha ocurrido un error')
