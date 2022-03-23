from rest_framework.viewsets import ModelViewSet
from inventory_api.custom_methods import IsAuthenticatedCustom
from .serializers import *
from rest_framework.response import Response


class InventoryView(ModelViewSet):
    queryset = Inventory.objects.select_related("group", "created_by")
    serializer_class = InventorySerializer
    permission_classes = (IsAuthenticatedCustom,)

    # pagination_class = CustomPagination

    # def get_queryset(self):
    #     if self.request.method.lower() != "get":
    #         return self.queryset
    #
    #     data = self.request.query_params.dict()
    #     data.pop("page", None)
    #     keyword = data.pop("keyword", None)
    #
    #     results = self.queryset.filter(**data)
    #
    #     if keyword:
    #         search_fields = (
    #             "code", "created_by__fullname", "created_by__email",
    #             "group__name", "name"
    #         )
    #         query = get_query(keyword, search_fields)
    #         return results.filter(query)
    #
    #     return results

    def create(self, request, *args, **kwargs):
        request.data.update({"created_by_id": request.user.id})
        return super().create(request, *args, **kwargs)


class InventoryGroupView(ModelViewSet):
    queryset = InventoryGroup.objects.select_related("belongs_to",
            "created_by").prefecht_related("inventories")
    serializer_class = InventorySerializer
    permission_classes = (IsAuthenticatedCustom,)

    # pagination_class = CustomPagination

    def create(self, request, *args, **kwargs):
        request.data.update({"created_by_id": request.user.id})
        return super().create(request, *args, **kwargs)
