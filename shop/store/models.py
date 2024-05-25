from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


class Category(models.Model):
    """Categoriyalar yaratish"""
    title = models.CharField(max_length=60, verbose_name='Katgeoriya nomi')
    image = models.ImageField(upload_to='categories/', verbose_name='Kategoriya Rasmi', blank=True, null=True)
    slug = models.SlugField(unique=True, null=True)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, verbose_name='Kategoriya',
                               related_name='subcategories')

    def get_absolute(self):
        return reverse('category_detail', kwargs={'slug': self.slug})

    def get_image(self):
        if self.image:
            return self.image
        else:
            return f"https://st4.depositphotos.com/14953852/24787/v/450/depositphotos_247872612-stock-illustration-no-image-available-icon-vector.jpg"

    def __str__(self):
        """Objectdagi bitta attributni admin panelga chiqaradi"""
        return self.title

    def __repr__(self):
        """Malumotni Web Brauserda korsatadi"""
        return f"Category: pk={self.pk},title={self.title}"

    class Meta:
        """Admin panelda Class nomini ozgartirish"""
        verbose_name = "Kategoriya"
        verbose_name_plural = "Kategoriyalar"


class Product(models.Model):
    """Productlarni yaratish"""
    title = models.CharField(max_length=120, verbose_name="Mahsulot nomi")
    price = models.FloatField(verbose_name='Mahsulot narxi')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Saytga chiqarilgan vaqti")
    quantity = models.IntegerField(default=0, verbose_name='Ombordagi soni')
    description = models.TextField(blank=True, default="Tez orada bu yerda malumot boladi",
                                   verbose_name="Mahsulot haqida malumot")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Kategoriya',
                                 related_name='products')
    slug = models.SlugField(unique=True, null=True)
    size = models.IntegerField(default=30, verbose_name='mm dagi olchami')
    color = models.CharField(max_length=30, default='Kumush', verbose_name='Rangi/Materiyali')

    def get_absolute(self):
        return reverse('product_detail', kwargs={'slug': self.slug})

    def get_first_photo(self):
        if self.images:
            try:
                return self.images.first().image.url
            except:
                return f"https://st4.depositphotos.com/14953852/24787/v/450/depositphotos_247872612-stock-illustration-no-image-available-icon-vector.jpg"
        else:
            return f"https://st4.depositphotos.com/14953852/24787/v/450/depositphotos_247872612-stock-illustration-no-image-available-icon-vector.jpg"

    def __str__(self):
        """Objectdagi bitta attributni admin panelga chiqaradi"""
        return self.title

    def __repr__(self):
        """Malumotni Web Brauserda korsatadi"""
        return f"Category: pk={self.pk},title={self.title}"

    class Meta:
        """Admin panelda Class nomini ozgartirish"""
        verbose_name = "Mahsulot"
        verbose_name_plural = "Mahsulotlar"


class Gallery(models.Model):
    """Mahsulot rasmlari"""
    image = models.ImageField(upload_to='products/', verbose_name='Rasm')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='images')

    class Meta:
        """Admin panelda Class nomini ozgartirish"""
        verbose_name = "Rasm"
        verbose_name_plural = "Mahsulot Gallery"
