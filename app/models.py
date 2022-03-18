from django.db import models
from user_admin.models import CustomUser


# class InventoryGroup(models.Model):
#     created_by = models.ForeignKey(
#         CustomUser, null=True, related_name="inventory_groups", on_delete=models.SET_NULL)
#     name = models.CharField(max_length=100, unique=True)
#     belongs_to = models.ForeignKey('self', null=True, on_delete=models.SET_NULL)

