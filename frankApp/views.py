from rest_framework.decorators import api_view
from rest_framework.response import Response

from .quotes import random_quote


@api_view(["GET"])
def get_random_quote(request):
    return Response({"quote": random_quote()})