from django.urls import path

from . import views

urlpatterns = [
    path('', views.callnonlinear, name='homepage'),
    path('Linear/', views.Linear, name='Linearalgo'),
     path('Interpolation/', views.interpolation, name='Linearalgo'),
          path('Integration/', views.Integration, name='Integration'),
                    path('Euler/', views.Euler, name='Euler'),
                                        path('Picards/', views.Picards, name='Picards'),
                                                                                path('runge/', views.runge, name='Picards'),
    
]