from .models import Inventory, InventoryGroup
from user_admin.serializers import CustomUserSerializer
from rest_framework import serializers


class InventoryGroupSerializer(serializers.ModelSerializer):
    created_by = CustomUserSerializer(read_only=True)
    created_by_id = serializers.CharField(write_only=True)

