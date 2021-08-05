# -*- coding:utf-8 -*-
from .models import ExtraInfo
from django.forms import ModelForm

class ExtraInfoForm(ModelForm):
    """
    The fields on this form are derived from the ExtraInfo model in models.py.
    """
    def __init__(self, *args, **kwargs):
        super(ExtraInfoForm, self).__init__(*args, **kwargs)
        self.fields['labx_firstname'].error_messages = {
            "required": u"Por favor ingresa Nombres.",
        }
        self.fields['labx_lastname'].error_messages = {
            "required": u"Por favor ingresa Apellidos.",
        }
        self.fields['labx_rut'].error_messages = {
            "required": u"Por favor ingresa RUT.",
        }
        self.fields['labx_birth_date'].error_messages = {
            "required": u"Por favor ingresa Fecha Nacimiento.",
            "invalid":u"Fecha no valida",
        }
        self.fields['labx_gender'].error_messages = {
            "required": u"Por favor selecciona Género.",
        }
        self.fields['labx_phone'].error_messages = {
            "required": u"Por favor ingresa Teléfono.",
        }
        self.fields['labx_country_nac'].error_messages = {
            "required": u"Por favor selecciona País de Nacionalidad.",
        }
        self.fields['labx_part_address'].error_messages = {
            "required": u"Por favor ingresa Dirección.",
        }
        self.fields['labx_part_region'].error_messages = {
            "required": u"Por favor selecciona Región.",
        }
        self.fields['labx_part_provincia'].error_messages = {
            "required": u"Por favor selecciona Provincia.",
        }
        self.fields['labx_part_comuna'].error_messages = {
            "required": u"Por favor selecciona Comuna.",
        }
        self.fields['labx_lab_address'].error_messages = {
            "required": u"Por favor ingresa Dirección.",
        }
        self.fields['labx_lab_region'].error_messages = {
            "required": u"Por favor selecciona Región.",
        }
        self.fields['labx_lab_provincia'].error_messages = {
            "required": u"Por favor selecciona Provincia.",
        }
        self.fields['labx_lab_comuna'].error_messages = {
            "required": u"Por favor selecciona Comuna.",
        }

        self.fields['labx_work'].error_messages = {
            "required": u"Por favor selecciona Profesión/Ocupación.",
        }
        self.fields['labx_educ_level'].error_messages = {
            "required": u"Por favor selecciona Nivel de Estudios.",
        }
        self.fields['labx_lab_lugar'].error_messages = {
            "required": u"Por favor ingresa Institución donde Trabajas Actualmente.",
        }
        self.fields['labx_lab_type'].error_messages = {
            "required": u"Por favor selecciona Tipo Institución en la que Trabajas.",
        }
        self.fields['labx_lab_rubro'].error_messages = {
            "required": u"Por favor selecciona Rubro de la Institución en la que Trabajas.",
        }
        self.fields['labx_lab_cargo'].error_messages = {
            "required": u"Por favor ingresa Cargo.",
        }


    class Meta(object):
        model = ExtraInfo
        fields = ('labx_rut','labx_firstname','labx_lastname','labx_birth_date','labx_gender','labx_phone','labx_country_nac','labx_part_address','labx_part_region','labx_part_provincia','labx_part_comuna','labx_lab_address','labx_lab_region','labx_lab_provincia','labx_lab_comuna','labx_work','labx_educ_level','labx_lab_lugar','labx_lab_type','labx_lab_rubro','labx_lab_cargo')

