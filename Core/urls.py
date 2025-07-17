from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('acerca/', views.acerca, name='acerca'),

    path('paginas/', views.ListaPaginas.as_view(), name='lista_paginas'),
    path('paginas/crear/', views.CrearPagina.as_view(), name='crear_pagina'),
    path('paginas/<int:pk>/', views.DetallePagina.as_view(), name='detalle_pagina'),
    path('paginas/<int:pk>/editar/', views.EditarPagina.as_view(), name='editar_pagina'),
    path('paginas/<int:pk>/borrar/', views.EliminarPagina.as_view(), name='borrar_pagina'),
]
