from django.urls import path
from catalog import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='index'),
    path('datas/', views.DataListView, name='datas'),
    path('data/<str:pk>', views.DataDetailView.as_view(), name='data-detail'),
    path('pigs/', views.PigListView, name='pigs'),
    path('pig/<str:pk>', views.PigDetailView, name='pig-detail'),
    path('downloadpiglist/', views.export_piglist, name='downloadpiglist'),
    path('downloaddatalist/', views.export_datalist, name='downloaddatalist'),
    path('pig/create/', views.PigCreate.as_view(), name='pig-create'),
    path('pig/<str:pk>/update/', views.PigUpdate.as_view(), name='pig-update'),
    path('pig/<str:pk>/delete/', views.PigDelete.as_view(), name='pig-delete'),
    path('pig/<str:pk>/history/', views.Pig_HistoryDetailView, name='pig-history'),
    path('data/<str:pk>/update/', views.DataUpdate.as_view(), name='data-update'),
    path('data/<str:pk>/delete/', views.DataDelete.as_view(), name='data-delete'),
    path('data/<str:pk>/history/', views.Data_HistoryDetailView, name='data-history'),
    path('videos/', views.PigVideoListView, name='videos'),
    path('videos/<str:pk>/video', views.PigVideoView, name='video-detail'),
    path('downloadpigvideo/<str:pk>', views.export_pigvideo, name='downloadpigvideo'),
    path('downloadvideoframe/<str:pk>', views.export_videoframe, name='downloadvideoframe'),
    path('video/create/', views.PigVideoCreate.as_view(), name='video-create'),
    path('depthvideos', views.PigDepthVideoListView, name='depth_videos'),
    path('depthvideo/create/', views.PigDepthVideoCreate.as_view(), name='depth_video-create')
] 

