from django.urls import path
from . import views

urlpatterns = [
    path('add/', views.add_data, name='add_data'),
    path('update/<int:user_id>/', views.update_data, name='update_data'),
]