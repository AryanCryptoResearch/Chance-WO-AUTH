from rest_framework import serializers 
from Regression.models import Params

class ParamsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Params
        fields = "__all__"
