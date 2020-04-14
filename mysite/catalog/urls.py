from django.urls import path
from catalog import views

urlpatterns = [
    path('', views.index, name='index'),
    path('datas/', views.DataListView.as_view(), name='datas'),
    path('data/<int:pk>', views.DataDetailView.as_view(), name='data-detail'),
    path('pigs/', views.PigListView.as_view(), name='pigs'),
]

