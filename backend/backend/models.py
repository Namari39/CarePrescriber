from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.forms import ValidationError

from backend.constants import MAX_LENGTH, MIN_VALUE, MAX_VALUE


class Schedule(models.Model):
    '''Модель выписанных рецептов врачем.'''

    medicament_name = models.CharField(max_length=MAX_LENGTH)
    frequency = models.PositiveIntegerField(
        validators=[
            MinValueValidator(MIN_VALUE),
            MaxValueValidator(MAX_VALUE)
        ],
        verbose_name='Периодичность'
    )
    duration_days = models.PositiveIntegerField(
        verbose_name='Продолжительность лечения (дни)',
        null=True,
        blank=True,
        help_text='Укажите количество дней, если применение не постоянное.'
    )
    is_permanent = models.BooleanField(
        default=False,
        verbose_name='Постоянное применение'
    )
    user_id = models.IntegerField(verbose_name='Медицинский полис')

    class Meta:
        unique_together = ('user_id', 'medicament_name')

    def __str__(self):
        return f"{self.user_id} - {self.medicament_name}"

    def clean(self):
        if self.is_permanent and self.duration_days:
            raise ValidationError(
                {
                    'duration_days':
                    'Нельзя указать длительность для постоянного применения.'
                }
            )
        if not self.is_permanent and not self.duration_days:
            raise ValidationError(
                {
                    'duration_days':
                    'Укажите длительность или отметьте как постоянное.'
                }
            )
