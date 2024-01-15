from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("", include("posts.urls")),
    path("admin/", admin.site.urls),
    path("posts/", include("posts.urls"), name="posts"),
    path("filemanager/", include("filemanager.urls")),
    path("accounts/", include("accounts.urls")),
    path("store/", include("store.urls")),
    path("orm/", include("orm.urls")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
