from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from rest_framework import viewsets
from core.serializers import CustomUserSerializer
from core.models import CustomUser

from rest_framework.response import Response


class CustomUserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = CustomUser.objects.all().order_by('-registration_date')
    serializer_class = CustomUserSerializer

    def put(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        if getattr(instance, '_prefetched_objects_cache', None):
            # If 'prefetch_related' has been applied to a queryset, we need to
            # forcibly invalidate the prefetch cache on the instance.
            instance._prefetched_objects_cache = {}

        return Response(serializer.data)
        # Allow = PUT


def home(request):
    return render(request, 'home.html')
