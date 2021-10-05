from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name="index_ausgaben"),
    path('neue_rechnung/', views.rechnung_form, name="neue_rechnung"),
    path('update_rechnung/<str:id>/', views.update_rechnung, name="update_rechnung"),
    path('delete_rechnung/<str:id>/', views.delete_rechnung, name="delete_rechnung"),
    path('analyse/', views.analyse, name="analyse"),
]
