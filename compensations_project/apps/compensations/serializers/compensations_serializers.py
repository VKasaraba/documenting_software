from rest_framework import serializers
from compensations_project.apps.compensations.models.compensations import BonusCompensation, CompensationRequest, CompensationType, EducationalCompensation, MedicalCompensation, OvertimeWorkCompensation, SportCompensation


class BonusCompensationSerializer(serializers.ModelSerializer):
    class Meta:
        model = BonusCompensation
        fields = '__all__'


class MedicalCompensationSerializer(serializers.ModelSerializer):
    class Meta:
        model = MedicalCompensation
        fields = '__all__'


class EducationalCompensationSerializer(serializers.ModelSerializer):
    class Meta:
        model = EducationalCompensation
        fields = '__all__'


class SportCompensationSerializer(serializers.ModelSerializer):
    class Meta:
        model = SportCompensation
        fields = '__all__'


class OvertimeWorkCompensationSerializer(serializers.ModelSerializer):
    class Meta:
        model = OvertimeWorkCompensation
        fields = '__all__'


COMPENSATION_TYPE_SERIALIZER_DICT = {
    CompensationType.BONUS: BonusCompensationSerializer,
    CompensationType.MEDICAL: MedicalCompensationSerializer,
    CompensationType.EDUCATIONAL: EducationalCompensationSerializer,
    CompensationType.SPORT: SportCompensationSerializer,
    CompensationType.OVERTIME: OvertimeWorkCompensationSerializer,
}


class CompensationRequestSerializer(serializers.ModelSerializer):
    compensation_info = serializers.SerializerMethodField()


    class Meta:
        model = CompensationRequest
        fields = '__all__'

    def get_compensation_info(self, obj):
        user = self.context['request'].user
        info_obj = obj.get_compensation_info_obj(user)
        serializer_class = COMPENSATION_TYPE_SERIALIZER_DICT[obj.compensation_type]
        return serializer_class(info_obj).data
