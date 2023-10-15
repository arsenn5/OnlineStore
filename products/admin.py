from django.contrib import admin

from products.models import Product, Category, Review, Tag

class ProductAdmin(admin.ModelAdmin):
    list_per_page = 1

admin.site.register(Product, ProductAdmin)
admin.site.register(Category)
admin.site.register(Review)
admin.site.register(Tag)