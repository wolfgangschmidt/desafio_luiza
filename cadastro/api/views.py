
from rest_framework import generics, mixins
from cadastro.models import Funcionario
from .serializer import FuncionarioSerializer

class FuncionarioCrudApiView(generics.RetrieveUpdateDestroyAPIView):
	
	look_up_field = "pk"
	serializer_class = FuncionarioSerializer
	def get_queryset(self):
		return Funcionario.objects.all()


class FuncionarioApiView(mixins.CreateModelMixin, generics.ListAPIView):
	
	look_up_field = "pk"
	serializer_class = FuncionarioSerializer
	def get_queryset(self):
		return Funcionario.objects.all()

	def post(self, request, *args, **kwargs):
		return self.create(request, *args, *kwargs)