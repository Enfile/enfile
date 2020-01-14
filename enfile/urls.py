from django.contrib import admin
from django.urls import path, include

from user.urls import router as user_router
from technology.urls import router as technology_router

urlpatterns = [
    path(r'admin/', admin.site.urls),
    path(r'api/user/', include(user_router.urls)),
    path(r'api/technology/', include(technology_router.urls))

]
