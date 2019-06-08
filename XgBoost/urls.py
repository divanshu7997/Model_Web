from django.urls import path

from . import views

urlpatterns = [
    # path('', views.index, name='index'),
    # path(r'^admin/', include(admin.site.urls)),
    path('', views.home, name='home'),
    path('op1/', views.op1, name='op1'),
    path('op2/', views.op2, name='op2'),
]