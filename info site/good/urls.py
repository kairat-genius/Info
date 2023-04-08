from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('main/', views.main, name='main'),
    path('about/', views.about, name='about'),
    path('news/', views.news, name='news'),
    path('create/', views.create, name='create'),
    path('test/', views.test),
    path('news/<int:pk>', views.NewDetaiView.as_view(), name='news-detail'),
    path('news/<int:pk>/update', views.NewUpdateView.as_view(), name='news-update'),
    path('news/<int:pk>/delete', views.NewDeleteView.as_view(), name='news-delete')
]