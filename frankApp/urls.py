# Add API routes here. They are served under /api/.

from django.urls import path
from .views import get_random_quote

urlpatterns = [
    path("quotes/", get_random_quote, name="get-random-quote"),
]