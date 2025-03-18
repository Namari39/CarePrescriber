from django import forms

from backend.models import Schedule


class ScheduleForm(forms.ModelForm):
    '''Форма для заполнения рецепта.'''

    class Meta:
        model = Schedule
        fields = [
            'medicament_name',
            'frequency',
            'duration_days',
            'is_permanent',
            'user_id'
        ]
        labels = {
            'medicament_name': 'Название лекарства',
            'frequency': 'Периодичность (раз в день)',
            'duration_days': 'Продолжительность лечения (дни)',
            'user_id': 'Идентификатор пользователя',
        }
