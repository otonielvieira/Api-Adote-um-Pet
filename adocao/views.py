from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import AdocaoSerializer
from rest_framework.status import HTTP_201_CREATED, HTTP_400_BAD_REQUEST, HTTP_200_OK
from .email_service import enviar_email_confirmacao
from .models import Adocao
import threading


class AdocaoList(APIView):
    def get(self, request, format=None):
        adocoes = Adocao.objects.all()
        serializer = AdocaoSerializer(adocoes, many=True)
        return Response(serializer.data, status=HTTP_200_OK)

    def post(self, request, format=None):
        serializer = AdocaoSerializer(data=request.data)
        if serializer.is_valid():
            adocao = serializer.save()
            enviar_email_confirmacao(adocao)
            return Response(serializer.data, status=HTTP_201_CREATED)
            
        return Response(
            {
                "errors": serializer.errors,
                "message": "Erro de validação! Preencha corretamente todos os Campos!",
            },
            status=HTTP_400_BAD_REQUEST,
        )


"""

import threading

listaThreads = [x.name for x in threading.enumerate()]

if not 'envia-email' in listaThreads:
    th = threading.Thread(target=enviar_email_confirmacao,arg=[adocao],name='envia-email')
    th.start()


"""
