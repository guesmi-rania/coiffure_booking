from django.contrib import admin
from django.urls import path, include
from bookings import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.booking_list, name='home'),  # <-- page d’accueil redirigée vers booking_list
    path('bookings/', include('bookings.urls')),
]
