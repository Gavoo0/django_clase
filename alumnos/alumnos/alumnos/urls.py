from . import views
from django.urls import path

urlpatterns = [
    path('index',views.index,name='index'),
    path('listadoSQL',views.listadoSQL,name='listadoSQL'),
    path('crud', views.crud, name='crud'),
    path('alumnosAdd', views.alumnosAdd, name='alumnosAdd'),

]
