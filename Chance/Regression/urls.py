from django.urls import path
from Regression.views import ParamsAPIView
# from .views import RegisterAPI
# from knox import views as knox_views
# from .views import LoginAPI

urlpatterns = [
    path("Params/", ParamsAPIView.as_view(), name='params'),
    # path('api/register/', RegisterAPI.as_view(), name='register'),
    # path('api/login/', LoginAPI.as_view(), name='login'),
    # path('api/logout/', knox_views.LogoutView.as_view(), name='logout'),
    # path('api/logoutall/', knox_views.LogoutAllView.as_view(), name='logoutall'),
]
