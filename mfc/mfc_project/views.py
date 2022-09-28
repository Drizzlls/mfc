from django.shortcuts import render
from django.http import HttpResponse
from bitrix24 import *
import time


def index(request):
    utm = {
            "utm_source": request.GET.get('utm_source', ' '),
            "utm_medium": request.GET.get('utm_medium', ' '),
            "utm_content": request.GET.get('utm_content', ' '),
            "utm_campaign": request.GET.get('utm_campaign', ' '),
            "utm_term": request.GET.get('utm_term', ' '),
        }
    return render(request, 'mfc/index.html', {'utm': utm})

def treatment(request):
    if request.POST:
        webhook = "https://novoedelo.bitrix24.ru/rest/16/gmog5f1duaqrjg94/"
        b = Bitrix24(webhook)
        fields = {
            "TITLE": "Заявка из МФЦ",
            "STATUS_ID": "NEW",
            "SOURCE_DESCRIPTION": "Заявка из МФЦ",
            'UF_CRM_1627289620': request.POST.get('summa', ''),
            'UF_CRM_1625646672': request.POST.get('prosrochka', ''),
            'UF_CRM_1600427611284': request.POST.get('vid', ''),
            'UF_CRM_1600427658497': request.POST.get('kreditori', ''),
            'UF_CRM_1664355340': request.POST.get('usluga', ''),
            "PHONE": [{"VALUE": f"{request.POST.get('phone', '')}", "VALUE_TYPE": "WORK"}],
            'NAME': request.POST['name'],
            "UTM_SOURCE": request.POST.get('utm_source', ''),
            "UTM_MEDIUM": request.POST.get('utm_medium', ''),
            "UTM_CONTENT": request.POST.get('utm_content', ''),
            "UTM_CAMPAIGN": request.POST.get('utm_campaign', ''),
            "UTM_TERM": request.POST.get('utm_term', ''),
        }
        addLead = b.callMethod("crm.lead.add", fields=fields)
        if request.POST['summa'] == 'До 250 000 руб.':
            return HttpResponse('True')
        else:
            return HttpResponse('False')

def thsDo(request):
    return render(request, 'mfc/thsDo.html')

def thsPosle(request):
    return render(request, 'mfc/thsPosle.html')