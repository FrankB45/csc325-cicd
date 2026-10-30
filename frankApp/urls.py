# Add API routes here. They are served under /api/.

from django.urls import path
from .views import get_random_quote, get_random_number

urlpatterns = [
    path("quotes/", get_random_quote, name="get-random-quote"),
    path("numbers/", get_random_number, name="get-random-number"),
]