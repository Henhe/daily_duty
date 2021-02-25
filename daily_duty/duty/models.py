from django.db import models
from django.core import validators

# Create your models here.
class Month(models.Model):
    name = models.CharField(max_length=20, verbose_name='Haзвaниe месяца',
                            validators=[validators.RegexValidator("^['А-Я']['а-я']+", message='месяц должен начинаться с большой буквы, кириллицей')])
    name_int = models.PositiveSmallIntegerField(db_index=True, verbose_name='Порядковый номер месяца в году',
                                                validators=[validators.MinValueValidator(1),
                                                            validators.MaxValueValidator(12)])

    class Meta:
        verbose_name_plural = 'Месяцы'
        verbose_name = 'Месяц'
        ordering = ['name_int']
        unique_together = ('name', 'name_int')
    def __str__(self):
        return self.name