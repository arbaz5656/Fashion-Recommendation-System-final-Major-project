
from django.urls import path
from . import views
urlpatterns = [
    path("",views.Home,name="Home"),
    path("index",views.index,name="index"),
    path("About",views.About,name="About"),
    path("signup",views.signup,name="signup"),
    path("login",views.login_pg,name="login_pg"),
    path("logout",views.logout_pg,name="logout_pg"),


]
