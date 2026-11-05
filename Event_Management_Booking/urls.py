from django.contrib import admin
from django.urls import path
from Events.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('marriage/',MarriageEventView.as_view()),
    path('venue/',VenueView.as_view()),
    path('customer/',CustomerView.as_view()),
    path('catering/',CateringView.as_view()),
    path('booking/',BookingView.as_view()),


]
