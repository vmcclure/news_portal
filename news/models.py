from django.db import models

# Create your models here.
class News(models.Model):
    title = models.CharField(max_length=150, verbose_name='Наименование')
    content = models.TextField(blank=True, verbose_name='контент')
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', verbose_name="Фото",blank=True)
    is_published = models.BooleanField(default=True)
    category = models.ForeignKey('Category', on_delete=models.PROTECT, null=True)

    def __str__(self):
        return self.title
    class Meta:
        verbose_name = 'новость'
        verbose_name_plural = "новости"
        ordering = ['-create_at']

class Category(models.Model):
    title = models.CharField(max_length=150, db_index=True, verbose_name='категории')
    def __str__(self):
        return self.title
    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'
        ordering = ['title']