from django.urls import path
from . import views

app_name = 'teaminfo'

urlpatterns = [
    path('', views.index, name='index'),
    path('division/', views.division, name='division'),
    path('<str:team_number>/', views.detail, name='detail'),
    path('<str:team_number>/vote/', views.vote, name='vote'),
]
