from django.contrib import admin

from ads_online.models import Ad, Review


@admin.register(Ad)
class AnnouncementAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'description', 'author', 'created_at', 'image',)


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('text', 'ad', 'author', 'created_at',)
