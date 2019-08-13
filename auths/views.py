from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated


class Hello(APIView):
    # 인증 요구 (DRF 기능)
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        content = {'message': f'Hello, {request.user.username}'}
        return Response(content)
