from django.urls import path
from . import views

urlpatterns = [
    path('interest-report/', views.calculate_interest_report, name='interest_report'),
    path('export-to-excel/', views.export_to_excel, name='export_to_excel'),
]
