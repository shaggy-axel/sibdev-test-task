from django.conf import settings
from django.core.cache import cache
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from drf_spectacular.utils import extend_schema
from rest_framework.generics import ListCreateAPIView
from rest_framework.parsers import MultiPartParser
from rest_framework.response import Response

from src.apps.deals.api.serializers import DealCreateListSerializer
from src.apps.deals.models import Deal
from src.apps.deals.utils import get_top_customers_with_gems


class DealListCreateView(ListCreateAPIView):
    queryset = Deal.objects.all()
    serializer_class = DealCreateListSerializer
    parser_classes = (MultiPartParser,)

    @method_decorator(cache_page(settings.CACHE_TTL))
    def list(self, request, *args, **kwargs):
        data = get_top_customers_with_gems()
        serializer = self.get_serializer(data, many=True)
        return Response(serializer.data)

    @extend_schema(responses={200: None})
    def create(self, request, *args, **kwargs):
        super().create(request, *args, **kwargs)
        cache.clear()
        return Response()
