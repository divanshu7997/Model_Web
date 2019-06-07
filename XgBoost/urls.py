from django.urls import path

from . import views

urlpatterns = [
    # path('', views.index, name='index'),
    # path(r'^admin/', include(admin.site.urls)),
    path('home/', views.home, name='home'),
    path('op1/', views.op1, name='op1'),
    path('download_1/', views.download_1, name='download_1'),
]