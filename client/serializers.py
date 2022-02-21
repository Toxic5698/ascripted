from rest_framework.serializers import Serializer, ModelSerializer
from client.models import *

class WorkTaskSerializer(ModelSerializer):

    class Meta:
        model = WorkTask
        fields = ['subject', 'date', 'duration', 'start_task', 'end_task', 'task_reward',
                  'other_expense_note', 'other_expense_amount']
