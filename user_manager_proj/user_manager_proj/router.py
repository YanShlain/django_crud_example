from users_app.viewsets import UserViewSets
from rest_framework import routers


router = routers.DefaultRouter()
router.register('user', UserViewSets)
