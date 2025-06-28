
from django.urls import path, include
from . import views

urlpatterns = [
    # path('', views.index, name='shop-home'),
    path('', views.ListPage.as_view(), name='list-page'),

]
