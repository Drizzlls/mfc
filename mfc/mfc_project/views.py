from django.shortcuts import render
from django.http import HttpResponse
from bitrix24 import *


def index(request):
    return render(request,'mfc/index.html')

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
            'UF_CRM_5F649955DE13E': request.POST.get('usluga', ''),
            "PHONE": [{"VALUE": f"{request.POST.get('phone', '')}", "VALUE_TYPE": "WORK"}],
            'NAME': request.POST['name'],
            "UTM_SOURCE": request.GET.get('utm_source', ''),
            "UTM_MEDIUM": request.GET.get('utm_medium', ''),
            "UTM_CONTENT": request.GET.get('utm_content', ''),
            "UTM_CAMPAIGN": request.GET.get('utm_campaign', ''),
            "UTM_TERM": request.GET.get('utm_term', ''),
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