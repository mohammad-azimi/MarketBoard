from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

from core import views as core_views


urlpatterns = [
    path("", include("core.urls")),
    path("items/", include("item.urls")),
    path("dashboard/", include("dashboard.urls")),
    path("inbox/", include("conversation.urls")),
    path("admin/", admin.site.urls),
]

handler403 = core_views.permission_denied_view
handler404 = core_views.page_not_found_view
handler500 = core_views.server_error_view

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)