from django.db import models
from django.contrib.auth import get_user_model
from core.models import BaseModel


User = get_user_model()


class Category(BaseModel):
    title = models.CharField('Заголовок',
                             max_length=256,
                             blank=False)
    description = models.TextField('Описание',
                                   blank=False)
    slug = models.SlugField('Идентификатор',
                            blank=False,
                            unique=True,
                            help_text='Идентификатор страницы для URL; '
                                      'разрешены символы латиницы, цифры, '
                                      'дефис и подчёркивание.')

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'Категории'


class Location(BaseModel):
    name = models.CharField('Название места',
                            max_length=256,
                            blank=False)

    class Meta:
        verbose_name = 'местоположение'
        verbose_name_plural = 'Местоположения'


class Post(BaseModel):
    title = models.CharField(verbose_name='Заголовок',
                             max_length=256,
                             blank=False)
    text = models.TextField('Текст',
                            blank=False)
    pub_date = models.DateTimeField(verbose_name='Дата и время публикации',
                                    blank=False,
                                    help_text='Если установить дату и время в '
                                              'будущем — можно делать '
                                              'отложенные публикации.')
    author = models.ForeignKey(User,
                               verbose_name='Автор публикации',
                               on_delete=models.CASCADE,
                               blank=False)
    location = models.ForeignKey(Location,
                                 verbose_name='Местоположение',
                                 on_delete=models.SET_NULL,
                                 null=True)
    category = models.ForeignKey(Category,
                                 verbose_name='Категория',
                                 on_delete=models.SET_NULL,
                                 null=True,
                                 blank=False)

    class Meta:
        verbose_name = 'публикация'
        verbose_name_plural = 'Публикации'
