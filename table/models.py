from django.db import models


class Tasks(models.Model):
    EQUIPMENT_CHOICES = [
        ('BLUE', 'Синяя'),
        ('GREEN', 'Зелёная'),
        ('AURORA', 'Аврора B0'),
        ('THERMAL', 'Термальная'),
        ('FIRST', 'Первая'),
    ]
    EQUIPMENT_DEFAULT_CHOICES = "Пусто"

    OPERATOR_CHOICES = [
        ('YURA', 'Юрий'),
        ('ZIYO', 'Зийо'),
        ('AZIZ', 'Азиз'),
        ('DIMA', 'Дмитрий'),
        ('DEJURN', 'Дежурные'),
    ]

    OPERATOR_DEFAULT_CHOICES = "Оператор"

    PUNCH_CHOICES = [
        ('PUNCH', 'Панч'),
        ('PUNCH_BEND', 'Панч+Загиб'),
    ]

    STAGE_CHOICES = [
        ('UNREADY', 'На машине'),
        ('READY', 'Готов'),
    ]

    id = models.IntegerField(verbose_name="ID", primary_key=True)
    company_name = models.CharField("Фирма", max_length=255, blank=True)
    qty = models.CharField("Шт.", max_length=255, blank=True)
    file_name = models.CharField("Название", max_length=255, blank=True)
    plate_size = models.CharField("Размер", max_length=255, blank=True)
    equipment = models.CharField("Машина", max_length=255, choices=EQUIPMENT_CHOICES, default=EQUIPMENT_DEFAULT_CHOICES)
    add_data = models.DateField(verbose_name="Дата", auto_now_add=True)
    add_time = models.TimeField(verbose_name="Время", auto_now_add=True)
    punch = models.CharField("Панч", max_length=255, choices=PUNCH_CHOICES, blank=True)
    stage = models.CharField(verbose_name="Состояние", max_length=50, choices=STAGE_CHOICES, default='На машине')
    operator = models.CharField("Вывел", max_length=255, choices=OPERATOR_CHOICES, blank=True)
    ready_datatime = models.CharField(max_length=255, verbose_name="Время готовности", blank=True)

    def __int__(self):
        return self.id

    class Meta:
        verbose_name = "Задание"
        verbose_name_plural = "Задания"
