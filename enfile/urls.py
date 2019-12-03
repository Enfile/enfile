from django.contrib import admin
from django.urls import path

from user.urls import router as user_router

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/', include(user_router.urls))
]
