from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Curso, Avaliacao
from .serializers import CursoSerializer, AvalizacaoSerializer


class CursoAPIView(APIView):
    """
    API de Cursos
    """

    def get(self, request):
        cursos = Curso.objects.all()
        serializer = CursoSerializer(cursos, many=True)
        return Response(serializer.data)


class AvaliacaoAPIView(APIView):
    """
    API de Avaliacoes
    """
    
    def get(self, request):
        avaliacoes = Avaliacao.objects.all()
        serializer = AvalizacaoSerializer(avaliacoes, many=True)
        return Response(serializer.data)
