from django.urls import path
from . import views

urlpatterns = [
    # Route principale pointant vers la Landing Page
    path('', views.landing_page_view, name='landing_page'),
]
