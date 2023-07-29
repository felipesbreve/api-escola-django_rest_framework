from rest_framework.test import APITestCase
from escola.models import Curso
from django.urls import reverse
from rest_framework import status

class CursoTestCase(APITestCase):

    def setUp(self):
        self.list_url = reverse('Cursos-list')
        self.curso_1 = Curso.objects.create(
            codigo_curso='CTT1',
            descricao='Curso Teste 1',
            nivel='B',
        )
        self.curso_2 = Curso.objects.create(
            codigo_curso='CTT2',
            descricao='Curso Teste 2',
            nivel='A',
        )
    
    # def test_fail(self):
    #     self.fail('Falha intencional')

    def test_get_lista_cursos(self):
        """Teste para verificar a requisição GET para listar os cursos"""
        response=self.client.get(self.list_url)
        self.assertEquals(response.status_code, status.HTTP_200_OK)

    def test_post_cria_cursos(self):
        """Teste para verificar a requisição POST para criar os cursos"""
        data = {
            'codigo_curso': 'CTT3',
            'descricao': 'Curso Teste 3',
            'nivel': 'A'
        }
        response = self.client.post(self.list_url, data=data, format='json')
        self.assertEquals(response.status_code, status.HTTP_201_CREATED)

    def test_delete_excluir_cursos(self):
        """Teste para verificar a requisição DELETE (Não permitida) para excluir um curso"""
        response = self.client.delete('/cursos/1/')
        self.assertEquals(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)

    def test_put_atualizar_cursos(self):
        """Teste para verificar a requisição PUT para atualizar um curso"""
        data = {
            'codigo_curso': 'CTT1',
            'descricao': 'Curso Teste 1 atualizado',
            'nivel': 'I'
        }
        response = self.client.put('/cursos/1/', data=data, format='json')
        self.assertEquals(response.status_code, status.HTTP_200_OK)