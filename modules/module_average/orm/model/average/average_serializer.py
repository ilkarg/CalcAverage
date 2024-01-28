from rest_framework import serializers
from modules.module_average.orm.model.average.average import Average

class AverageSerializer(serializers.ModelSerializer):
	class Meta:
		model = Average
		fields = '__all__'