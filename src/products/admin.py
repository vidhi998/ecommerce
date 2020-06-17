from django.contrib import admin

from .models import Product,Variation, ProductFeatured, Category, ProductImage


class VariationInline(admin.TabularInline):
    model = Variation
    extra = 0


class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 0


class ProductAdmin(admin.ModelAdmin):
    inlines = (VariationInline, ProductImageInline)
    list_display = ('__unicode__', 'price')
    class Meta:
        model = Product



# Register your models here.
admin.site.register(Product, ProductAdmin)
admin.site.register(Category)
admin.site.register(ProductFeatured)