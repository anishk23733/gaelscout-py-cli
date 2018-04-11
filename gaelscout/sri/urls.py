from django.urls import path
from . import views

app_name = 'sri'

urlpatterns = [
    path('', views.index, name='index'),
    # path('<str:team_number>/', views.detail, name='detail'),
    # # ex: /polls/5/results/
    # path('<str:team_number>/analyze/', views.analyze, name='results'),
    # # ex: /polls/5/vote/
    # path('<str:team_number>/vote/', views.vote, name='vote'),
]
