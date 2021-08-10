# Eol Custom Reg Form

Allows to verify if the user identification number (RUT) belongs to Caja Los Andes.

## lms.yml Configuration

The following fields must be added to the lms config file

```yaml
CAJA_ANDES:
  rutPrestador: id
  tipoPrestador: number
  usuario: user
  clave: pass
  apiUrl: 'http://url'
  recaptchaSecret: 'secret'

REGISTRATION_EXTENSION_FORM: 'custom_reg_form.forms.ExtraInfoForm'
REGISTRATION_EXTRA_FIELDS:
    city: hidden 
    confirm_email: hidden 
    country: required 
    gender: hidden 
    goals: hidden 
    honor_code: required 
    level_of_education: hidden 
    mailing_address: hidden 
    terms_of_service: hidden 
    year_of_birth: required
```
## cms.yml Configuration

The following fields must be added to the lms config file

```yaml
CAJA_ANDES:
  rutPrestador: id
  tipoPrestador: number
  usuario: user
  clave: pass
```
