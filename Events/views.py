from django.shortcuts import render
from django.views.generic import View
from django.http import JsonResponse

class MarriageEventView(View):
    def get(self, request):
        events = [
            {
                "id": 101,
                "event_name": "Wedding Ceremony",
                "bride_name": "Anjali",
                "groom_name": "Arjun",
                "event_date": "15/12/2026",
                "location": "Kochi",
                "guest_count": 500,
                "budget": 1000000
            },
            {
                "id": 102,
                "event_name": "Wedding Reception",
                "bride_name": "Meera",
                "groom_name": "Rahul",
                "event_date": "20/12/2026",
                "location": "Kollam",
                "guest_count": 300,
                "budget": 750000
            }
        ]
        return JsonResponse(events, safe=False)
class VenueView(View):
    def get(self, request):
        venues = [
            {
                "id": 1,
                "venue_name": "Grand Palace Auditorium",
                "location": "Kochi",
                "capacity": 1000,
                "rent": 150000,
                "availability": True
            },
            {
                "id": 2,
                "venue_name": "Royal Convention Centre",
                "location": "Kollam",
                "capacity": 500,
                "rent": 100000,
                "availability": True
            }
        ]
        return JsonResponse(venues, safe=False)

class CustomerView(View):
    def get(self, request):
        customers = [
            {
                "id": 1,
                "customer_name": "Anjali",
                "email": "anjali@gmail.com",
                "contact": "9876543210",
                "address": "Kochi"
            },
            {
                "id": 2,
                "customer_name": "Meera",
                "email": "meera@gmail.com",
                "contact": "9876543211",
                "address": "Kollam"
            }
        ]
        return JsonResponse(customers, safe=False)  
    
class CateringView(View):
    def get(self, request):
        catering = [
            {
                "id": 1,
                "package_name": "Traditional Kerala Sadya",
                "food_type": "Vegetarian",
                "price_per_person": 250
            },
            {
                "id": 2,
                "package_name": "Premium Wedding Buffet",
                "food_type": "Vegetarian and Non-Vegetarian",
                "price_per_person": 500
            }
        ]
        return JsonResponse(catering, safe=False)

class BookingView(View):
    def get(self, request):
        bookings = [
            {
                "id": 501,
                "customer_name": "Anjali",
                "event_name": "Wedding Ceremony",
                "venue": "Grand Palace Auditorium",
                "decoration": "Royal Decoration",
                "catering": "Traditional Kerala Sadya",
                "photography": "Premium Photography",
                "total_amount": 280000,
                "booking_status": "Confirmed"
            }
        ]
        return JsonResponse(bookings, safe=False)
