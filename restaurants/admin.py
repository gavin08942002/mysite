from bs4 import Comment
from django.contrib import admin
from restaurants.models import Restaurant,Food,Comment
# Register your models here.
class RestaurantAdmin(admin.ModelAdmin):
    list_display = ('name','phone_number','address')

class FoodAdmin(admin.ModelAdmin):
    list_display = ('name','price','comment','is_spicy','restaurant')


class CommentAdmin(admin.ModelAdmin):
    list_display = ('visitor','content','email','date_time')


admin.site.register(Restaurant,RestaurantAdmin)
admin.site.register(Food,FoodAdmin)
admin.site.register(Comment,CommentAdmin)