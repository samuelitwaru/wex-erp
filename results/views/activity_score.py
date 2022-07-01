from rest_framework import viewsets
from ..models import ActivityScore
from ..serializers import ActivityScoreSerializer
from rest_framework.decorators import action
from rest_framework.response import Response


class ActivityScoreViewSet(viewsets.ModelViewSet):
    queryset = ActivityScore.objects.all()
    serializer_class = ActivityScoreSerializer

    def get_queryset(self):
        params = self.request.query_params
        queryset = super().get_queryset()
        if params:
            queryset = queryset.filter(**params.dict())
        return queryset

    @action(detail=False, methods=['GET'], name='get_count', url_path='count')
    def get_count(self, request, *args, **kwargs):
        params = self.request.query_params
        queryset = super().get_queryset()
        if params:
            queryset = queryset.filter(**params.dict())
        count = queryset.count()
        return Response({'count':count})