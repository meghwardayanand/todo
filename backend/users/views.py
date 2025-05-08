from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required, permission_required


from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view
from rest_framework import permissions, generics, status
from rest_framework.response import Response

from users.serializers import UserSignInSerializer, SignUpUserSerializer

# Create your views here.
@login_required
@permission_required([permissions.IsAuthenticated])
@api_view(['POST'])
def signout(request):
    """Sign out user view."""
    try:
        logout(request)
        return Response(
            {"message": "Logged out successfully!"},
            status=status.HTTP_200_OK
        )
    except Exception as e:
        return Response(status=status.HTTP_204_NO_CONTENT)


class SignInAPIView(generics.GenericAPIView):
    serializer_class = UserSignInSerializer
    permission_classes = [permissions.AllowAny]
    authentication_classes = []

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        response = {}
        if serializer.is_valid(raise_exception=True):
            user = serializer.validated_data.pop('user')
            login(request, user)

            token = Token.objects.filter(user_id=user.id).first()
            response.update(serializer.validated_data)
            response['token'] = token.key
        
        return Response(response, status=status.HTTP_200_OK)


class SignUpAPIView(generics.GenericAPIView):
    serializer_class = SignUpUserSerializer
    permission_classes = [permissions.AllowAny]
    authentication_classes = []

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        response = {}
        if serializer.is_valid(raise_exception=True):
            user = serializer.save()
            login(request, user)

            token = Token.objects.filter(user_id=user.id).first()
            response.update(serializer.data)
            response['token'] = token.key

        return Response(response, status=status.HTTP_201_CREATED)
