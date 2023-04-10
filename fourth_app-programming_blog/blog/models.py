from django.db import models
from django.urls import reverse


class Blog(models.Model):
    title = models.CharField(max_length=255, verbose_name='Nomi')
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")
    content = models.TextField(blank=True, verbose_name="Kontent")
    photo = models.ImageField(upload_to="photos/%Y/%m/%d", blank=True, verbose_name="Rasm")
    time_completed = models.DateTimeField(auto_now_add=True, verbose_name="Yuklanish vaqti")
    time_update = models.DateTimeField(auto_now=True, verbose_name="Yangilash vaqti")
    is_published = models.BooleanField(default=True, verbose_name="Chop etilgan")
    cat = models.ForeignKey('Category', on_delete=models.PROTECT, verbose_name="Kategoriya")

    def __str__(self):
        return self.title

    def get_absolut_url(self):
        return reverse('post', kwargs={'post_slug': self.slug})

    class Meta:
        verbose_name = "Yangilik"
        verbose_name_plural = "Yangiliklar"
        ordering = ['-time_completed']


class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True, verbose_name="Kategoriya")
    slug = models.SlugField(max_length=100, unique=True, db_index=True, verbose_name="URL")

    def __str__(self):
        return self.name

    def get_absolut_url(self):
        return reverse('category', kwargs={'cat_slug': self.slug})

    class Meta:
        verbose_name = "Kategoriya"
        verbose_name_plural = "Kategoriyalar"