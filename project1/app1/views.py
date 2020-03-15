from django.shortcuts import render
from django.http import HttpResponse
from app1.models import AccessRecord,Topic,Webpage

# Create your views here.

def index(request):
    webpages_list = AccessRecord.objects.order_by('date')
    date_dict = {'access_records':webpages_list}
    my_dict = {'insert_me':"Hello From Views.py"}
    return render(request,'app1/index.html',context=date_dict)
