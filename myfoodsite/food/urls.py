from . import views
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

app_name = 'food'
urlpatterns = [
    path('', views.index, name = 'index'),
    path('<int:item_id>/', views.detail, name='detail'),
    path('item/', views.item, name = 'item',),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)