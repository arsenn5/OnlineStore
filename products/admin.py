from django.contrib import admin

from products.models import Product, Category, Review, Tag

admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Review)
admin.site.register(Tag)
