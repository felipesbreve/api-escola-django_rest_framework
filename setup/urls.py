from django.contrib import admin
from django.urls import path, include
from escola.views import AlunosViewSet, CursosViewSet, MatriculasViewSet, ListaMatriculaAluno, ListaAlunosMatriculados
from rest_framework import routers
from django.conf import settings
from django.conf.urls.static import static

router = routers.DefaultRouter()
router.register('alunos', AlunosViewSet, basename='Alunos')
router.register('cursos', CursosViewSet, basename='Cursos')
router.register('matriculas', MatriculasViewSet, basename='Matriculas')

urlpatterns = [
    path('controle-geral/', admin.site.urls),
    # path('admin/', include('admin_honeypot.urls', namespace='admin_honeypot')),
    path('', include(router.urls)),
    path('alunos/<int:pk>/matriculas/', ListaMatriculaAluno.as_view()),
    path('cursos/<int:pk>/matriculas/', ListaAlunosMatriculados.as_view())
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
