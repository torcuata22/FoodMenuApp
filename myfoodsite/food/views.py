from django.http import HttpResponse
from django.shortcuts import render, redirect

from .forms import ItemForm  
from .models import Item

from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
#from django.template import loader

# Create your views here:
class IndexClassView(ListView): 
     model=Item
     template_name= 'food/index.html'
     context_object_name='item_list'  

def item(request):
     return HttpResponse('<h1>This is the item view</h1>')
class FoodDetail(DetailView):
     model = Item
     template_name = 'food/detail.html'



def create_item(request):
     form = ItemForm(request.POST or None)
     if form.is_valid():
          form.save()
          return redirect('food:index')
     return render(request, 'food/item_form.html', {'form': form})

#this is a class-based view for create item using CreateView

class CreateItem(CreateView):
     model = Item
     fields = ['item_name', 'item_desc', 'item_price', 'item_image'] #only fields we want on the form
     template_name = 'food/item_form.html'
     
     def form_valid(self, form):
          form.instance.user_name = self.request.user
          return super().form_valid(form)




def update_item(request, id):
     item = Item.objects.get(id=id)
     form = ItemForm(request.POST or None, instance = item)
     if form.is_valid():
          form.save()
          return redirect('food:index')

     return render(request, 'food/item_form.html', {'form': form, 'item': item})

def delete_item(request, id):
     item = Item.objects.get(id=id)
     if request.method == 'POST':
          item.delete()
          return redirect('food:index')
     return render(request, 'food/item_delete.html', {'item':item})


     