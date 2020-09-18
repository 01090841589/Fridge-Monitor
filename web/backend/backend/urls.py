from django.contrib import admin
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework.permissions import AllowAny
from django.urls import path, include

from rest_framework_jwt.views import obtain_jwt_token
from rest_framework_jwt.views import refresh_jwt_token
from rest_framework_jwt.views import verify_jwt_token


schema_view = get_schema_view(
    openapi.Info(
        # 필수 인자
        title="figeMonitor API",
        default_version="v1",
        # 선택 인자
        description="API 서비스입니다.",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="ihs3583@gmail.com"),
        license=openapi.License(name="SSAFY License"),
    ),
    public=True,
   permission_classes=( AllowAny,),
)

urlpatterns = [
    path('api-token-auth/', obtain_jwt_token),
    path('api-token-refresh/', refresh_jwt_token),
    path('api-token-verify/', verify_jwt_token),
    path('admin/', admin.site.urls),
    path('userapi/', include('userApi.urls')),
    path('swagger/', schema_view.with_ui('swagger'), name='schema-swagger-ui'),
]
