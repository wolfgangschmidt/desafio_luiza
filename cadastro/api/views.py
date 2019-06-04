
from rest_framework import generics
from cadastro.models import Funcionario
from .serializer import FuncionarioSerializer

class FuncionarioCrudApiView(generics.RetrieveUpdateDestroyAPIView):
	
	look_up_field = "pk"
	serializer_class = FuncionarioSerializer
	def get_queryset(self):
		return Funcionario

class FuncionarioApiView(generics.CreateAPIView):
	
	look_up_field = "pk"
	serializer_class = FuncionarioSerializer
	def get_queryset(self):
		return Funcionario