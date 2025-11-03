from django.contrib import admin
from .models import Movie, Actor, Category


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ("title", "release_year", "rating")
    list_filter = ("release_year", "categories")
    search_fields = ("title", "description")
    prepopulated_fields = {"slug": ("title",)}


@admin.register(Actor)
class ActorAdmin(admin.ModelAdmin):
    list_display = ("name", "birth_date")
    search_fields = ("name",)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)