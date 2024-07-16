from django.test import TestCase

# Create your tests here.
import requests
from bs4 import BeautifulSoup

def get_data(link):
    response = requests.get(link)
    soup = BeautifulSoup(response.text,'html.parser')

    def return_value(clas,num):
        result = soup.find_all('div',class_=clas)[num].text
        return result.strip()
    
    values = {}

    values['owner'] = return_value('fw-bold text-gray-800 fs-6',0)
    values['plaque'] = return_value('fw-bold fs-6 text-gray-800 d-flex align-items-center',0)
    values['vin'] = return_value('fw-bold text-gray-800 fs-6',1)
    values['brand'] = return_value('fw-bold fs-6 text-gray-800',0)
    values['sub_brand'] = return_value('fw-bold text-gray-800 fs-6',2)
    values['verify_reason'] = return_value('fw-bold text-gray-800 fs-6',3)
    values['service'] = return_value('fw-bold text-gray-800 fs-6',4)
    values['line'] = return_value('fw-bold text-gray-800 fs-6',5)
    values['model year'] = return_value('fw-bold text-gray-800 fs-6',6)
    values['date'] = return_value('fw-bold fs-6 text-gray-800 d-flex align-items-center',1)
    values['last day'] = return_value('fw-bold fs-6 text-gray-800 d-flex align-items-center',2)
    values['no_tech'] = return_value('fw-bold fs-6 text-gray-800 d-flex align-items-center',3)
    values['folio'] = return_value('fw-bold fs-6 text-gray-800 d-flex align-items-center',4)
    values['ferify init'] = return_value('fw-bold fs-6 text-gray-800 d-flex align-items-center',5)
    values['finish init'] = return_value('fw-bold fs-6 text-gray-800 d-flex align-items-center',6)
    
    return values
    
from datetime import datetime
from django.core.exceptions import ValidationError

def convert_date_format(date_str):
    try:
        return datetime.strptime(date_str, '%d-%m-%Y').strftime('%Y-%m-%d')
    except ValueError:
        raise ValidationError('Invalid date format. It must be in DD-MM-YYYY format.')

# from .models import Specialty

# Create your tests here.

from .models import Teacher

# for instance in Teacher.objects.all():
#     instance.created = convert_date_format(instance.created)
#     instance.save()
Teacher.objects.all().delete()
