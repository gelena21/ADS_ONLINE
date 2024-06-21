from django.db import models

from users.models import User

NULLABLE = {'blank': True, 'null': True}


class Ad(models.Model):
    """
    Модель объявления.

    Атрибуты:
    title (CharField): Название товара.
    price (IntegerField): Цена товара.
    description (TextField): Описание товара.
    author (ForeignKey): Автор объявления.
    created_at (DateTimeField): Дата и время создания объявления.
    image (ImageField): Изображение товара.
    """
    title = models.CharField(max_length=200, verbose_name='Название товара')
    price = models.IntegerField(verbose_name='Цена товара')
    description = models.TextField(max_length=300, verbose_name='Описание', **NULLABLE)
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Автор", **NULLABLE)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата и время создания объявления')
    image = models.ImageField(upload_to='preview/', verbose_name='Изображение', **NULLABLE)

    def __str__(self) -> str:
        """
        Возвращает строковое представление объекта.
        """
        return f"Объявление: {self.title}"

    class Meta:
        """
        Метакласс для определения порядка сортировки и имен модели.
        """
        ordering = ['-created_at']
        verbose_name = "Объявление"
        verbose_name_plural = "Объявления"


class Review(models.Model):
    """
   Модель отзыва к объявлению.

   Атрибуты:
   text (TextField): Текст отзыва.
   ad (ForeignKey): Объявление, к которому относится отзыв.
   author (ForeignKey): Автор отзыва.
   created_at (DateTimeField): Дата и время создания отзыва.
   """
    text = models.TextField(verbose_name='Текст', **NULLABLE)
    ad = models.ForeignKey(Ad, on_delete=models.CASCADE, verbose_name="Объявление")
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Автор", **NULLABLE)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата и время создания')

    def __str__(self) -> str:
        """
        Возвращает строковое представление объекта.
        """
        return f"Отзыв к объявлению: {self.ad}"

    class Meta:
        """
        Метакласс для определения имен модели.
        """
        verbose_name = "Отзыв"
        verbose_name_plural = "Отзывы"
