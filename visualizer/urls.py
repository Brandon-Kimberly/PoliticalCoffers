from django.urls import path
from .views import render_top_earners_chart, top_earners_chart, render_spending_pie
from .views import spending_pie, render_donors_pie, donors_pie, render_donors_pie_base

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('earning-chart/', views.render_top_earners_chart, name='earners-chart'),
    path('earning-chart-data/', views.top_earners_chart, name='earners-chart-data'),
    path('spending-pie/', views.render_spending_pie, name='spending-pie'),
    path('spending-pie-data/', views.spending_pie, name='spending-pie-data'),
    path('donors-pie/', views.render_donors_pie, name='donor-pie'),
    path('donors-pie-data/', views.donors_pie, name='donors-pie-data'),
    path('donors-pie-base/', views.render_donors_pie_base, name='donors-pie-base'),
    path('load-data/', views.load_data, name='load_data')
]