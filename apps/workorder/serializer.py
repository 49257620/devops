# encoding: utf-8
# -*- coding: utf-8 -*-
# author = ‘LW’

from rest_framework import serializers

from workorder.models import WorkOrder


class WorkOrderSerializer(serializers.ModelSerializer):
    applicant = serializers.HiddenField(default=serializers.CurrentUserDefault())
    apply_time = serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S',read_only=True)
    complete_time = serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S',read_only=True)

    class Meta:
        model = WorkOrder
        fields = '__all__'

    def to_representation(self, instance):
        applicant_obj =  instance.applicant
        assign_to_obj = instance.assign_to
        final_processor_obj = instance.final_processor
        type_value = instance.get_type_display()
        status_value = instance.get_status_display()

        ret = super(WorkOrderSerializer, self).to_representation(instance)

        ret['type'] = {
            'id': instance.type,
            'name': type_value
        }

        ret['status'] = {
            'id': instance.status,
            'name': status_value
        }

        ret['applicant'] = {
            'id': applicant_obj.id,
            'name': applicant_obj.name
        }

        ret['assign_to'] = {
            'id': assign_to_obj.id,
            'name': assign_to_obj.name
        }

        if final_processor_obj:
            ret['final_processor'] = {
                'id': final_processor_obj.id,
                'name': final_processor_obj.name
            }

        return ret


