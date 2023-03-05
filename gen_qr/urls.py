from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.urls import path
from . import views
from .views import qrtable

app_name = "gen_qr"
urlpatterns = [
    path("", views.index, name="index"),
    path("create/", views.create, name="create"),
    path("create/create_ajax/", views.create_ajax, name="create_ajax"),
    path("qrcamera/", views.qrcamera, name="qrcamera"),
    #path("qrtable/", views.qrtable, name="qrtable"),
    path("qrtable/", qrtable.as_view(), name="qrtable"),
    path("dummy/", views.dummy, name="dummy"),
    path("access_shortner/<slug>/", views.access_shortner, name="access_shortner"),
]
urlpatterns += staticfiles_urlpatterns()