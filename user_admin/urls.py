from django.urls import include, path
from .views import (CreateUserView, LoginView,
                    UpdatePasswordView, MeView, UserActivitiesView, UsersView)
from rest_framework.routers import DefaultRouter, SimpleRouter

router = DefaultRouter(trailing_slash=False)

router.register("create-user", CreateUserView, 'create user')
router.register("login", LoginView, 'login')
router.register("update-password", UpdatePasswordView, 'update password')
router.register("me", MeView, 'me')
router.register("activities", UserActivitiesView, 'activities log')
router.register("users", UsersView, 'users view')

urlpatterns = [
    path('', include(router.urls)),
]
