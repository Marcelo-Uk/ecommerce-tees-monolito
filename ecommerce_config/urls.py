# /home/ubuntu/ecommerce_monolith/ecommerce_config/urls.py
"""
URL configuration for ecommerce_config project.
"""
from django.contrib import admin
from django.urls import path, include
# Import static helper for development static file serving
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls),

    # API URLs (prefixed with /api/)
    path("api/auth/", include(("autenticacao.urls", "autenticacao"), namespace="autenticacao")),
    path("api/pagamentos/", include(("pagamentos.urls", "pagamentos"), namespace="pagamentos")),
    path("api/produtos/", include(("produtos.urls", "produtos"), namespace="produtos")),

    # Frontend Pages URLs (served by the core app)
    # Include these at the root level
    path("", include(("core.urls", "core"), namespace="core")),
]

# Add static files serving configuration for development environment
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS[0])
    # Note: STATICFILES_DIRS is a list, we assume the first entry is our main static dir.
    # For production, static files should be handled differently (e.g., collectstatic and web server config).

