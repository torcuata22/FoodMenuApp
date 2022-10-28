from django.http import HttpResponse
from django.shortcuts import render, redirect

from .forms import ItemForm  
from .models import Item

def index(request):
     item_list = Item.objects.all()
     #template = loader.get_template('food/index.html')
     context = {
          'item_list': item_list,
     }
     #return HttpResponse(template.render(context,request))
     return render(request, 'food/index.html', context)



def detail (request, item_id):
     item = Item.objects.get(pk = item_id)
     context = {
          'item':item,
     }

     return render(request, 'food/detail.html', context)