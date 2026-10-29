from django.urls import path
from .views import (
    EmpleadoListCreateAPIView,
    EmpleadoRetriveUpdateDestroyAPIView
)

urlpatterns = [
    path("api/empleados/", EmpleadoListCreateAPIView.as_view(), name="empleado-list-create"),
    path("api/empleados/<int:pk>/", EmpleadoRetriveUpdateDestroyAPIView.as_view(), name="empleado-detail"), 
]