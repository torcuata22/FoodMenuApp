from . import views
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

app_name = 'food'
urlpatterns = [
    path('', views.index, name = 'index'),
    path('<int:item_id>/', views.detail, name='detail'),
    path('item/', views.item, name = 'item',),
    path('add/', views.create_item, name='create_item'),
    path('update/<int:id>',views.update_item, name='update_item'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)