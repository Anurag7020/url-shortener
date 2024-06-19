from django.shortcuts import render, redirect
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import ShortenedURL, URLHit
from .serializers import ShortenedURLSerializer, URLHitSerializer
from django.shortcuts import get_object_or_404

# Create your views here.
class ShortenerAPIView(APIView):
    permission_classes = [IsAuthenticated]
    serializer_class = ShortenedURLSerializer

    def get(self, request):
        data = ShortenedURL.objects.all()
        serializer = ShortenedURLSerializer(data, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ShortenedURLSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class URLHitAPIView(APIView):
    serializer_class = URLHitSerializer

    def get(self, request, code):
        print(code)
        shorten_url = get_object_or_404(ShortenedURL,short_code=code)
        hit = URLHit.objects.create(user=shorten_url.user, short_code=shorten_url.short_code)
        hit.save()
        print(shorten_url.original_url)
        return redirect(shorten_url.original_url)
