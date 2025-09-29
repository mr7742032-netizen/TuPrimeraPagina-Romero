from django.urls import path
from inicio.views import inicio, crear_guitarra_v2, listado_guitarras #, crear_guitarra_v1

urlpatterns = [
    path('', inicio, name='inicio'),
    # path('crear-guitarra/<marca>/<modelo>/', crear_guitarra_v1, name='crear_guitarra')
    path('guitarras', listado_guitarras, name='listado_guitarras'),
    path('guitarras/crear', crear_guitarra_v2, name='crear_guitarra'),
]
