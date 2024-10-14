from django.urls import path
from . import views

app_name='patient'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:id>', views.patient_detail, name='patient_detail'),
    path('add_patient/', views.add, name='add'),
    path('edit_patient/<int:id>/', views.edit, name='edit'),
    path('delete/<int:id>', views.delete, name='delete'),
]
