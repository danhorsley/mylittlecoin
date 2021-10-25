from django.urls import path

from . import views

urlpatterns = [
    path('', views.basic, name='basic'),
    path('wallet', views.wallet, name='wallet'),
    path('last_block', views.last_block, name='last_block'),
    path('new_user', views.new_user, name='new_user'),
    path('mine', views.mine, name='mine'),
    path('deephash', views.deephash, name='deephash'),
]