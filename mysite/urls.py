from django.contrib import admin
from django.urls import path

from mysite.core import views

urlpatterns = [
    path('', views.home, name='home'),
    path('population-chart/', views.population_chart, name='population-chart'),
    path('pie-chart/', views.pie_chart, name='pie-chart'),
    path('admin/', admin.site.urls),
]
