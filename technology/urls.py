from rest_framework import routers
from .views import TechnologyLevelViewSet

router = routers.DefaultRouter()
router.register(r'levels', TechnologyLevelViewSet)
