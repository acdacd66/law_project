from django.urls import path
from . import views

urlpatterns = [
    path('lawboard', views.lawboardList , name="lb_list"),
    path('lawboard/new', views.lawboardNew , name="lb_new"),
    path('lawboard/create', views.lawboardCreate , name="lb_create"),
    path('lawboard/edit/<int:lb_id>', views.lawboardEdit , name="lb_edit"),
    path('lawboard/update/<int:lb_id>', views.lawboardUpdate , name="lb_update"),
    path('lawboard/<int:lb_id>', views.lawboardDetail, name="lb_detail"),
    path('lawboard/delete/<int:lb_id>', views.lawboardDelete, name="lb_delete"),
    path('lawboard/scrap/<int:pk>',views.lawboardScrap, name="lb_scrap"),
    

    
]