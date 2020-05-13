from django.urls import path
from catalog import views

urlpatterns = [
    path('', views.index, name='index'),
    path('datas/', views.DataListView, name='datas'),
    path('data/<int:pk>', views.DataDetailView.as_view(), name='data-detail'),
    path('pigs/', views.PigListView, name='pigs'),
    path('pig/<int:pk>', views.PigDetailView.as_view(), name='pig-detail'),
    path('downloadpiglist/', views.export_piglist, name='downloadpiglist'),
    path('downloaddatalist/', views.export_datalist, name='downloaddatalist'),
    path('pig/create/', views.PigCreate.as_view(), name='pig-create'),
    path('pig/<int:pk>/update/', views.PigUpdate.as_view(), name='pig-update'),
    path('pig/<int:pk>/delete/', views.PigDelete.as_view(), name='pig-delete'),
]

