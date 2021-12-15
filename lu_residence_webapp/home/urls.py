from django.urls import path

from . import views

app_name = 'home'
urlpatterns = [
    path('', views.landing, name='landing'),
    path('news/', views.news, name='news'),
    path('apply/', views.apply, name='apply'),
    path('faq/', views.faq, name='faq'),
    path('fees/', views.fees, name='fees'),
    path('register/', views.register, name='register'),
    path('housing/', views.housing, name='housing'),
    path('workorder/', views.work_order, name='work_order'),
    path('workorder/bartley/', views.bartley, name='workorder_bartley'),
    path('workorder/north_res/', views.north_res, name='workorder_northres'),
    path('workorder/south_res/', views.south_res, name='workorder_southres'),
    path('workorder/townhouse/', views.repair_form, name='workorder_townhouse'),
]
