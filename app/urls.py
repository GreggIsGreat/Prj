from django.urls import path
from . import views
from app.views import HomeView,AboutView
from django.views.generic import TemplateView
#
# app_name = 'website'

urlpatterns = [
    # path('', views.home, name='home'),
    path('', HomeView.as_view()),
    path('abt/', AboutView.as_view()),
]
