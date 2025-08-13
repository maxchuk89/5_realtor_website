from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class Flat(models.Model):
    created_at = models.DateTimeField(
        'Когда создано объявление',
        auto_now_add=True,
        db_index=True
    )
    description = models.TextField('Текст объявления', blank=True)
    price = models.IntegerField('Цена квартиры', db_index=True)
    town = models.CharField('Город', max_length=50, db_index=True)
    town_district = models.CharField('Район города', max_length=50, blank=True)
    address = models.TextField('Адрес', blank=True)
    floor = models.CharField('Этаж', max_length=3, blank=True)
    rooms_number = models.IntegerField(
        'Количество комнат',
        db_index=True,
        blank=True,
        null=True
    )
    living_area = models.FloatField(
        'Жилая площадь кв.м',
        blank=True,
        null=True
    )
    has_balcony = models.BooleanField(
        'Наличие балкона',
        blank=True,
        null=True
    )
    active = models.BooleanField(
        'Активно ли объявление',
        db_index=True
    )
    construction_year = models.IntegerField(
        'Год постройки здания',
        validators=[MinValueValidator(1000), MaxValueValidator(9999)],
        db_index=True,
        blank=True,
        null=True
    )
    new_building = models.BooleanField(
        'Новостройка',
        blank=True,
        null=True
    )
    liked_by = models.ManyToManyField(
        'auth.User',
        related_name='liked_flats',
        verbose_name='Кому понравилось',
        blank=True
    )

    def __str__(self):
        return f'{self.town}, {self.address} — {self.price} руб.'


class Owner(models.Model):
    full_name = models.CharField(
        'ФИО владельца',
        max_length=200,
        db_index=True,
        blank=True
    )
    phone_number = models.CharField(
        'Номер владельца',
        max_length=20,
        blank=True
    )
    pure_phone = PhoneNumberField(
        'Нормализованный номер владельца',
        blank=True,
        null=True
    )
    flats = models.ManyToManyField(
        Flat,
        related_name='owners',
        verbose_name='Квартиры',
        blank=True
    )

    def __str__(self):
        return self.full_name or "Без имени"


class Complaint(models.Model):
    complainant = models.ForeignKey(
        'auth.User',
        on_delete=models.CASCADE,
        verbose_name='Кто жаловался',
        related_name='complaints',
        blank=True,
        null=True
    )
    flat = models.ForeignKey(
        Flat,
        on_delete=models.CASCADE,
        verbose_name='Квартира, на которую пожаловались',
        blank=True,
        null=True
    )
    text = models.TextField(
        'Текст жалобы',
        blank=True
    )

    def __str__(self):
        return f'Жалоба от {self.complainant} на {self.flat}'
