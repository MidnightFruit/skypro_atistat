from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny

from User.models import User
from User.serializers import UserSerializer


class UserCreateAPIView(CreateAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    
    def perform_create(self, serializer):
        user = serializer.save(is_active=False)
        user.set_password(user.password)
        user.save()