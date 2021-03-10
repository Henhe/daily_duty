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

class Period(models.Model):

    year = models.PositiveSmallIntegerField(verbose_name='Период год',
                                                validators=[validators.MinValueValidator(2017),
                                                            validators.MaxValueValidator(2040)])
    month = models.ForeignKey('Month', verbose_name='Период месяц', on_delete=models.PROTECT)
    class Meta:
        verbose_name_plural = 'Периоды'
        verbose_name = 'Период'
        ordering = ['-year', 'month']
        unique_together = ('year', 'month')
    def __str__(self):
        return f'{self.month} {self.year}'

class WorkHours(models.Model):
    period = models.ForeignKey('Period', verbose_name='Период', on_delete=models.PROTECT)
    days_quantity = models.PositiveSmallIntegerField(default=28, verbose_name='Количество дней', help_text='количество дней в месяце',
                                                    validators=[validators.MinValueValidator(28),
                                                                validators.MaxValueValidator(31)])
    day1= models.DecimalField(max_digits=4, decimal_places=2, verbose_name='1', help_text='рабочее время, ч.',
                              default=0, validators=[validators.MinValueValidator(0),
                                                            validators.MaxValueValidator(24)])
    day2 = models.DecimalField(max_digits=4, decimal_places=2, verbose_name='2', help_text='рабочее время, ч.',
                               default=0, validators=[validators.MinValueValidator(0),
                                           validators.MaxValueValidator(24)])
    day3 = models.DecimalField(max_digits=4, decimal_places=2, verbose_name='3', help_text='рабочее время, ч.',
                               default=0, validators=[validators.MinValueValidator(0),
                                           validators.MaxValueValidator(24)])
    day4 = models.DecimalField(max_digits=4, decimal_places=2, verbose_name='4', help_text='рабочее время, ч.',
                               default=0, validators=[validators.MinValueValidator(0),
                                           validators.MaxValueValidator(24)])
    day5 = models.DecimalField(max_digits=4, decimal_places=2, verbose_name='5', help_text='рабочее время, ч.',
                               default=0, validators=[validators.MinValueValidator(0),
                                           validators.MaxValueValidator(24)])
    day6 = models.DecimalField(max_digits=4, decimal_places=2, verbose_name='6', help_text='рабочее время, ч.',
                               default=0, validators=[validators.MinValueValidator(0),
                                           validators.MaxValueValidator(24)])
    day7 = models.DecimalField(max_digits=4, decimal_places=2, verbose_name='7', help_text='рабочее время, ч.',
                               default=0, validators=[validators.MinValueValidator(0),
                                           validators.MaxValueValidator(24)])
    day8 = models.DecimalField(max_digits=4, decimal_places=2, verbose_name='8', help_text='рабочее время, ч.',
                               default=0, validators=[validators.MinValueValidator(0),
                                           validators.MaxValueValidator(24)])
    day9 = models.DecimalField(max_digits=4, decimal_places=2, verbose_name='9', help_text='рабочее время, ч.',
                               default=0, validators=[validators.MinValueValidator(0),
                                           validators.MaxValueValidator(24)])
    day10 = models.DecimalField(max_digits=4, decimal_places=2, verbose_name='10', help_text='рабочее время, ч.',
                               default=0, validators=[validators.MinValueValidator(0),
                                           validators.MaxValueValidator(24)])
    day11 = models.DecimalField(max_digits=4, decimal_places=2, verbose_name='11', help_text='рабочее время, ч.',
                               default=0, validators=[validators.MinValueValidator(0),
                                           validators.MaxValueValidator(24)])
    day12 = models.DecimalField(max_digits=4, decimal_places=2, verbose_name='12', help_text='рабочее время, ч.',
                               default=0, validators=[validators.MinValueValidator(0),
                                           validators.MaxValueValidator(24)])
    day13 = models.DecimalField(max_digits=4, decimal_places=2, verbose_name='13', help_text='рабочее время, ч.',
                               default=0, validators=[validators.MinValueValidator(0),
                                           validators.MaxValueValidator(24)])
    day14 = models.DecimalField(max_digits=4, decimal_places=2, verbose_name='14', help_text='рабочее время, ч.',
                               default=0, validators=[validators.MinValueValidator(0),
                                           validators.MaxValueValidator(24)])
    day15 = models.DecimalField(max_digits=4, decimal_places=2, verbose_name='15', help_text='рабочее время, ч.',
                               default=0, validators=[validators.MinValueValidator(0),
                                           validators.MaxValueValidator(24)])
    day16 = models.DecimalField(max_digits=4, decimal_places=2, verbose_name='16', help_text='рабочее время, ч.',
                               default=0, validators=[validators.MinValueValidator(0),
                                           validators.MaxValueValidator(24)])
    day17 = models.DecimalField(max_digits=4, decimal_places=2, verbose_name='17', help_text='рабочее время, ч.',
                               default=0, validators=[validators.MinValueValidator(0),
                                           validators.MaxValueValidator(24)])
    day18 = models.DecimalField(max_digits=4, decimal_places=2, verbose_name='18', help_text='рабочее время, ч.',
                               default=0, validators=[validators.MinValueValidator(0),
                                           validators.MaxValueValidator(24)])
    day19 = models.DecimalField(max_digits=4, decimal_places=2, verbose_name='19', help_text='рабочее время, ч.',
                                default=0, validators=[validators.MinValueValidator(0),
                                            validators.MaxValueValidator(24)])
    day20 = models.DecimalField(max_digits=4, decimal_places=2, verbose_name='20', help_text='рабочее время, ч.',
                               default=0, validators=[validators.MinValueValidator(0),
                                           validators.MaxValueValidator(24)])
    day21 = models.DecimalField(max_digits=4, decimal_places=2, verbose_name='21', help_text='рабочее время, ч.',
                                default=0, validators=[validators.MinValueValidator(0),
                                            validators.MaxValueValidator(24)])
    day22 = models.DecimalField(max_digits=4, decimal_places=2, verbose_name='22', help_text='рабочее время, ч.',
                                default=0, validators=[validators.MinValueValidator(0),
                                            validators.MaxValueValidator(24)])
    day23 = models.DecimalField(max_digits=4, decimal_places=2, verbose_name='23', help_text='рабочее время, ч.',
                                default=0, validators=[validators.MinValueValidator(0),
                                            validators.MaxValueValidator(24)])
    day24 = models.DecimalField(max_digits=4, decimal_places=2, verbose_name='24', help_text='рабочее время, ч.',
                                default=0, validators=[validators.MinValueValidator(0),
                                            validators.MaxValueValidator(24)])
    day25 = models.DecimalField(max_digits=4, decimal_places=2, verbose_name='25', help_text='рабочее время, ч.',
                                default=0, validators=[validators.MinValueValidator(0),
                                            validators.MaxValueValidator(24)])
    day26 = models.DecimalField(max_digits=4, decimal_places=2, verbose_name='26', help_text='рабочее время, ч.',
                                default=0, validators=[validators.MinValueValidator(0),
                                            validators.MaxValueValidator(24)])
    day27 = models.DecimalField(max_digits=4, decimal_places=2, verbose_name='27', help_text='рабочее время, ч.',
                                default=0, validators=[validators.MinValueValidator(0),
                                            validators.MaxValueValidator(24)])
    day28 = models.DecimalField(max_digits=4, decimal_places=2, verbose_name='28', help_text='рабочее время, ч.',
                                default=0, validators=[validators.MinValueValidator(0),
                                            validators.MaxValueValidator(24)])
    day29 = models.DecimalField(max_digits=4, decimal_places=2, verbose_name='29', help_text='рабочее время, ч.',
                                default=0, validators=[validators.MinValueValidator(0),
                                            validators.MaxValueValidator(24)])
    day30 = models.DecimalField(max_digits=4, decimal_places=2, verbose_name='30', help_text='рабочее время, ч.',
                                default=0, validators=[validators.MinValueValidator(0),
                                            validators.MaxValueValidator(24)])
    day31 = models.DecimalField(max_digits=4, decimal_places=2, verbose_name='31', help_text='рабочее время, ч.',
                                default=0, validators=[validators.MinValueValidator(0),
                                            validators.MaxValueValidator(24)])

    def workhours_sum(self):
        return self.day1 + self.day2 + self.day3 + self.day4 + self.day5 + self.day6 + self.day7 + self.day8 + self.day9 + self.day10 + \
        self.day11 + self.day12 + self.day13 + self.day14 + self.day15 + self.day16 + self.day17 + self.day18 + self.day19 + self.day20 + \
        self.day21 + self.day22 + self.day23 + self.day24 + self.day25 + self.day26 + self.day27 + self.day28 + self.day29 + self.day30 + \
        self.day31

    workhours_sum.short_description ='Рабочее время сумма'

    class Meta:
        verbose_name_plural = 'Рабочее время месяцы'
        verbose_name = 'Рабочее время месяц'
        # ordering = ['-year', 'month']
        # unique_together = ('year', 'month')
    def __str__(self):
        s = f'{self.period} \
        (1){self.day1} (2){self.day2} (3){self.day3} (4){self.day4} (5){self.day5} (6){self.day6} (7){self.day7} (8){self.day8} \
        (9){self.day9} (10){self.day10} (11){self.day11} (12){self.day12} (13){self.day13} (14){self.day14} (15){self.day15} \
        (16){self.day16} (17){self.day17} (18){self.day18} (19){self.day19} (20){self.day20} (21){self.day21} (22){self.day22} \
        (23){self.day23} (24){self.day24} (25){self.day25} (26){self.day26} (27){self.day27} (28){self.day28}'
        if self.days_quantity > 30:
            s += f' (29){self.day29} (30){self.day30} (31){self.day31}'
        elif self.days_quantity > 29:
            s += f' (29){self.day29} (30){self.day30}'
        elif self.days_quantity > 28:
            s += f' (29){self.day29}'
        s += f' сумма ={self.workhours_sum()}'
        return s

class SupportLine(models.Model):
    name = models.CharField(max_length=200, verbose_name='Наименование')
    class Meta:
        verbose_name_plural = 'Линия поддержки'
        verbose_name = 'Линия поддержки'
        ordering = ['pk']
    def __str__(self):
        return f'{self.name}'

class CommandLine(models.Model):
    name = models.CharField(max_length=200, verbose_name='Наименование')
    class Meta:
        verbose_name_plural = 'Команды'
        verbose_name = 'Команда'
        ordering = ['pk']
    def __str__(self):
        return f'{self.name}'

class Employees(models.Model):
    surname = models.CharField(max_length=40, verbose_name='Фамилия',
                            validators=[validators.RegexValidator("^['А-Я']['а-я']+",
                                                                  message='фамилия должна начинаться с большой буквы, кириллицей')])
    name = models.CharField(max_length=20, verbose_name='Имя',
                            validators=[validators.RegexValidator("^['А-Я']['а-я']+",
                            message='имя должно начинаться с большой буквы, кириллицей')])
    middle_name = models.CharField(max_length=20, verbose_name='Отчество',
                            validators=[validators.RegexValidator("^['А-Я']['а-я']+",
                                                                  message='отчество должно начинаться с большой буквы, кириллицей')])
    supportline = models.ForeignKey('SupportLine', verbose_name='Линия поддержки', on_delete=models.PROTECT,
                                    null=True)
    commandline = models.ForeignKey('CommandLine', verbose_name='Команда', on_delete=models.PROTECT,
                                    null=True)
    def full_name(self):
        return f'{self.surname} {self.name[0:1]}. {self.middle_name[0:1]}.'

    full_name.short_description = 'ФИО'

    class Meta:
        verbose_name_plural = 'Сотрудники'
        verbose_name = 'Сотрудник'