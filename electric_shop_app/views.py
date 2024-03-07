from rest_framework import viewsets
from rest_framework.filters import SearchFilter
from rest_framework.response import Response

from .models import Supplier
from .permissions import IsActiveEmployee
from .serializers import SupplierSerializer

class SupplierViewSet(viewsets.ModelViewSet):
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer
    permission_classes = [IsActiveEmployee]
    filter_backends = [SearchFilter]
    search_fields = ['country']


    def update(self, request, *args, **kwargs):
        # Запрет обновления поля 'Задолженность перед поставщиком'
        partial = kwargs.pop('partial', False)
        instance = self.get_object()

        if 'debt' in request.data and instance.debt != request.data['debt']:
            return Response({'detail': 'Обновление поля "Задолженность перед поставщиком" запрещено.'}, status=status.HTTP_400_BAD_REQUEST)

        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        return Response(serializer.data)
