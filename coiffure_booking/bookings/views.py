from django.shortcuts import render, redirect
from .models import Booking
from .forms import BookingForm

def booking_list(request):
    bookings = Booking.objects.all().order_by('-date', '-time')
    return render(request, 'bookings/booking_list.html', {'bookings': bookings})

def booking_create(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('booking_list')
    else:
        form = BookingForm()
    return render(request, 'bookings/booking_form.html', {'form': form})
