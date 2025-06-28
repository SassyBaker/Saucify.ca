from django.contrib import admin
from . import models

# Register your models here.
@admin.register(models.Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ["__str__"]


class ProductImageInline(admin.TabularInline):
    model = models.ProductImage
    extra = 0


@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ["__str__"]
    list_display_links = ()
    list_filter = ()
    search_fields = ()
    inlines = (ProductImageInline,)
    prepopulated_fields = {'slug': ('title',)}

@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ["__str__"]
    list_display_links = ()
    list_filter = ()
    search_fields = ()
    prepopulated_fields = {'slug': ('name',)}


class CouponAdmin(admin.ModelAdmin):
    list_display = ["__str__"]
    list_display_links = ()
    list_filter = ()
    search_fields = ()


class OrderItemInline(admin.TabularInline):
    model = models.OrderItem
    extra = 0
    can_delete = False
    verbose_name_plural = "Order items"
    verbose_name = "Order item"


@admin.register(models.Order)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ["__str__"]
    list_display_links = ()
    list_filter = ()
    search_fields = ()
    inlines = (OrderItemInline,)


class CartItemInline(admin.TabularInline):
    model = models.CartItem
    extra = 0
    can_delete = False
    verbose_name_plural = "Cart items"
    verbose_name = "Cart item"


@admin.register(models.Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ["__str__"]
    list_display_links = ()
    list_filter = ()
    search_fields = ()
    inlines = (CartItemInline,)
