from . import views
from django.urls import path

urlpatterns = [
    path('index',views.index,name='index'),
    path('listadoSQL',views.listadoSQL,name='listadoSQL'),
    path('crud', views.crud, name='crud'),
    path('alumnosAdd', views.alumnosAdd, name='alumnosAdd'),
    path('alumnos_del/<str:pk>',views.alumnos_del,name="alumnos_del"),
    path('alumnos_findEdit/<str:pk>',views.alumnos_findEdit,name="alumnos_findEdit"),
    path('alumnosUpdate', views.alumnosUpdate, name='alumnosUpdate'),
    path('formRamo',views.formRamo,name='formRamo'),
    path('crud_ramo',views.crud_ramo,name='crud_ramo'),
    path('ramo_del/<str:pk>',views.ramo_del,name="ramo_del"),
    path('seccion_form',views.seccion_form,name="seccion_form"),
    path('alumnoForm',views.alumnoForm,name='alumnoForm'),
    path('menu',views.menu,name="menu"),
]
