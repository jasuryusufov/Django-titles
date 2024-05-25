from django import template
from store.models import Category

register = template.Library()


@register.simple_tag()
def get_categories():
    return Category.objects.filter(parent=None)


@register.simple_tag()
def get_sorted():
    sortes = [
        {
            'title': 'Narxi boyicha',
            'sorters': [
                ('price', "O'sish boyicha"),
                ('-price', "Kamayish boyicha")
            ]
        },
        {
            'title': "Rangi boyicha",
            'sorters': [
                ('color', "A dan Z gacha"),
                ('-color', "Z dan A gacha")
            ]
        },
        {
            'title': "O'lchami bo'yicha",
            "sorters": [
                ('size', "O'sish bo'yicha"),
                ('-size', "Kamayish bo'yicha"),
            ]
        }
    ]
    return sortes


@register.simple_tag()
def get_subcategories(category):
    return Category.objects.filter(parent=category)
