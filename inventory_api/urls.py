from django.contrib import admin
from django.urls import path
from django.contrib import admin
from django.urls import path
from django.urls.conf import include
import user_admin


urlpatterns = [
    path('admin/', admin.site.urls),
    path('user/', include('user_admin.urls')),
]
