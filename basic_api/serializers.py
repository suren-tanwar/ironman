from rest_framework import serializers
from .models import DragonMasterModel

class DragonMasterSerializer(serializers.ModelSerializer):
    class Meta:
        model = DragonMasterModel
        fields = '__all__'

      


        