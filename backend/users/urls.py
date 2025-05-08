from django.urls import path

from users.views import signout, SignInAPIView, SignUpAPIView


app_name = "users"
urlpatterns = [
    path('signup/', SignUpAPIView.as_view(), name='signup'),
    path('signin/', SignInAPIView.as_view(), name='signin'),
    path('signout/', signout, name='signout'),
]
