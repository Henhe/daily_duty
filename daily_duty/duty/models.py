from django.db import models
from django.core import validators


# Create your models here.
class Month(models.Model):
    name = models.CharField(max_length=20, verbose_name='Haзвaниe месяца',
                            validators=[validators.RegexValidator("^['А-Я']['а-я']+",
                                                                  message='месяц должен начинаться с большой буквы, '
                                                                          'кириллицей')])
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
    days_quantity = models.PositiveSmallIntegerField(default=28, verbose_name='Количество дней',
                                                     help_text='количество дней в месяце',
                                                     validators=[validators.MinValueValidator(28),
                                                                 validators.MaxValueValidator(31)])
    day1 = models.DecimalField(max_digits=4, decimal_places=2, verbose_name='1', help_text='рабочее время, ч.',
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
        sum1 = 0
        for i in range(1, 32):
            name_elem = f'day{i}'
            sum1 += self.__getattribute__(name_elem)
        return sum1

    workhours_sum.short_description = 'Рабочее время сумма'

    class Meta:
        verbose_name_plural = 'Рабочее время месяцы'
        verbose_name = 'Рабочее время месяц'
        # ordering = ['-year', 'month']
        # unique_together = ('year', 'month')

    def get_days_as_list_of_dict(self):
        lst = []
        for i in range(1, 32):
            name_elem = f'day{i}'
            lst.append({name_elem: str(float(self.__getattribute__(name_elem))).replace(',', '.')})
        return lst

    def save_hours(self, dict_days):
        for k, v in dict_days.items():
            res = v[0]
            if res == '':
                res = '0'
            self.__setattr__(k, float(res))
        self.save()

    def full__str__(self):
        s = f'{self.period} \n'
        for j in range(4):
            for i in range(1, 8):
                name_elem = f'day{(j * 7 + i)}'
                s += f'{self.__getattribute__(name_elem)}\t'
            s += '\n'
        for i in range(29, int(self.days_quantity) + 1):
            name_elem = f'day{i}'
            s += f'{self.__getattribute__(name_elem)}\t'
        return s

    def __str__(self):
        return f'{self.period}'


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
                                                                     message='фамилия должна начинаться с большой '
                                                                             'буквы, кириллицей')])
    name = models.CharField(max_length=20, verbose_name='Имя',
                            validators=[validators.RegexValidator("^['А-Я']['а-я']+",
                                                                  message='имя должно начинаться с большой буквы, '
                                                                          'кириллицей')])
    middle_name = models.CharField(max_length=20, verbose_name='Отчество', blank=True,
                                   validators=[validators.RegexValidator("^['А-Я']['а-я']+",
                                                                         message='отчество должно начинаться с '
                                                                                 'большой буквы, кириллицей')])
    supportline = models.ForeignKey('SupportLine', verbose_name='Линия поддержки', on_delete=models.PROTECT,
                                    blank=True, null=True)
    commandline = models.ForeignKey('CommandLine', verbose_name='Команда', on_delete=models.PROTECT,
                                    blank=True, null=True)

    def full_name(self):
        return f'{self.surname} {self.name[0:1]}. {self.middle_name[0:1]}.'

    full_name.short_description = 'ФИО'

    class Meta:
        verbose_name_plural = 'Сотрудники'
        verbose_name = 'Сотрудник'

    def __str__(self):
        return f'{self.surname} {self.name[0:1]}. {self.middle_name[0:1]}.'


class Dutyes(models.Model):
    workhours = models.ForeignKey('WorkHours', verbose_name='Период', on_delete=models.PROTECT)
    employee = models.ForeignKey('Employees', verbose_name='Сотрудник', on_delete=models.PROTECT)
    commandline = models.ForeignKey('CommandLine', verbose_name='Команда', on_delete=models.PROTECT,
                                    blank=True, null=True)
    supportline = models.ForeignKey('SupportLine', verbose_name='Линия поддержки', on_delete=models.PROTECT,
                                    blank=True, null=True)
    day1 = models.BooleanField(verbose_name='1', help_text='дежурство',
                               default=False)
    day2 = models.BooleanField(verbose_name='2', help_text='дежурство',
                               default=False)
    day3 = models.BooleanField(verbose_name='3', help_text='дежурство',
                               default=False)
    day4 = models.BooleanField(verbose_name='4', help_text='дежурство',
                               default=False)
    day5 = models.BooleanField(verbose_name='5', help_text='дежурство',
                               default=False)
    day6 = models.BooleanField(verbose_name='6', help_text='дежурство',
                               default=False)
    day7 = models.BooleanField(verbose_name='7', help_text='дежурство',
                               default=False)
    day8 = models.BooleanField(verbose_name='8', help_text='дежурство',
                               default=False)
    day9 = models.BooleanField(verbose_name='9', help_text='дежурство',
                               default=False)
    day10 = models.BooleanField(verbose_name='10', help_text='дежурство',
                                default=False)
    day11 = models.BooleanField(verbose_name='11', help_text='дежурство',
                                default=False)
    day12 = models.BooleanField(verbose_name='12', help_text='дежурство',
                                default=False)
    day13 = models.BooleanField(verbose_name='13', help_text='дежурство',
                                default=False)
    day14 = models.BooleanField(verbose_name='14', help_text='дежурство',
                                default=False)
    day15 = models.BooleanField(verbose_name='15', help_text='дежурство',
                                default=False)
    day16 = models.BooleanField(verbose_name='16', help_text='дежурство',
                                default=False)
    day17 = models.BooleanField(verbose_name='17', help_text='дежурство',
                                default=False)
    day18 = models.BooleanField(verbose_name='18', help_text='дежурство',
                                default=False)
    day19 = models.BooleanField(verbose_name='19', help_text='дежурство',
                                default=False)
    day20 = models.BooleanField(verbose_name='20', help_text='дежурство',
                                default=False)
    day21 = models.BooleanField(verbose_name='21', help_text='дежурство',
                                default=False)
    day22 = models.BooleanField(verbose_name='22', help_text='дежурство',
                                default=False)
    day23 = models.BooleanField(verbose_name='23', help_text='дежурство',
                                default=False)
    day24 = models.BooleanField(verbose_name='24', help_text='дежурство',
                                default=False)
    day25 = models.BooleanField(verbose_name='25', help_text='дежурство',
                                default=False)
    day26 = models.BooleanField(verbose_name='26', help_text='дежурство',
                                default=False)
    day27 = models.BooleanField(verbose_name='27', help_text='дежурство',
                                default=False)
    day28 = models.BooleanField(verbose_name='28', help_text='дежурство',
                                default=False)
    day29 = models.BooleanField(verbose_name='29', help_text='дежурство',
                                default=False)
    day30 = models.BooleanField(verbose_name='30', help_text='дежурство',
                                default=False)
    day31 = models.BooleanField(verbose_name='31', help_text='дежурство',
                                default=False)

    class Meta:
        verbose_name_plural = 'Дежурства'
        verbose_name = 'Дежурство'
        ordering = ['workhours', 'employee']

    def workhours_sum(self):
        sum1 = 0
        for i in range(1, 32):
            name_elem = f'day{i}'
            if self.__getattribute__(name_elem):
                sum1 += 24 - self.workhours.__getattribute__(name_elem)
        return sum1

    workhours_sum.short_description = 'Дежурное время сумма'

    def workhours_days(self):
        sum1 = 0
        for i in range(1, 32):
            name_elem = f'day{i}'
            if self.__getattribute__(name_elem):
                sum1 += 1
        return sum1

    workhours_days.short_description = 'Количество дежурств'

    def workhours_holidays(self):
        sum1 = 0
        for i in range(1, 32):
            name_elem = f'day{i}'
            if self.__getattribute__(name_elem) and self.workhours.__getattribute__(name_elem) == 0:
                sum1 += 1
        return sum1

    workhours_holidays.short_description = 'Количество выходных/праздников'

    def get_days_as_list_of_dict(self):
        lst = []
        for i in range(1, self.workhours.days_quantity + 1):
            name_elem = f'day{i}'
            lst.append({name_elem: bool(float(self.__getattribute__(name_elem)))})

        return lst

    def save_hours(self, dict_days):
        for i in range(1, self.workhours.days_quantity + 1):
            name_elem = f'day{i}'
            res = dict_days.get(name_elem, False)
            if res != False:
                res = res[0]
                res = str(res).lower()
                if res == 'false':
                    res = False
                elif res == 'true':
                    res = True
                else:
                    continue
            self.__setattr__(name_elem, res)
        self.save()

    def get_info_for_index(self):
        dict_ans = {}
        dict_ans['pk'] = self.pk
        dict_ans['employee'] = self.employee
        for i in range(1, self.workhours.days_quantity + 1):
            name_elem = f'day{i}'
            # print(f'{i} {name_elem} {self.__getattribute__(name_elem)} {self.workhours.__getattribute__(name_elem)}')
            if self.__getattribute__(name_elem):
                dict_ans[name_elem] = float(24 - self.workhours.__getattribute__(name_elem))
            else:
                dict_ans[name_elem] = float(0)
        dict_ans['workhours_sum'] = self.workhours_sum
        dict_ans['workhours_holidays'] = self.workhours_holidays
        return dict_ans