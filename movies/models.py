from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils.text import slugify
from django.urls import reverse
import datetime


class TimeStampedModel(models.Model):
    """Modelo abstrato para timestamps padronizados."""
    created_at = models.DateTimeField("Criado em", auto_now_add=True)
    updated_at = models.DateTimeField("Atualizado em", auto_now=True)

    class Meta:
        abstract = True


class Category(models.Model):
    """Categoria de filme (ex: Ação, Drama, etc.)."""
    name = models.CharField("Nome", max_length=100, unique=True)

    class Meta:
        verbose_name = "Categoria"
        verbose_name_plural = "Categorias"
        ordering = ["name"]

    def __str__(self):
        return self.name


class Actor(models.Model):
    """Representa um ator."""
    name = models.CharField("Nome", max_length=100)
    birth_date = models.DateField("Data de nascimento", null=True, blank=True)

    class Meta:
        verbose_name = "Ator"
        verbose_name_plural = "Atores"
        ordering = ["name"]

    def __str__(self):
        return self.name


class Movie(TimeStampedModel):
    """Representa um filme no catálogo."""

    title = models.CharField("Título", max_length=255)
    slug = models.SlugField("Slug", max_length=255, unique=True, blank=True)
    description = models.TextField("Descrição", blank=True)
    release_year = models.IntegerField(
        "Ano de lançamento",
        validators=[
            MinValueValidator(1888),
            MaxValueValidator(datetime.date.today().year + 1),
        ],
    )
    photo = models.ImageField(
        "Foto do filme",
        upload_to="movies/photos/%Y/%m/",
        blank=True,
        null=True
    )
    trailer_url = models.URLField("URL do trailer", blank=True, null=True)
    rating = models.DecimalField("Nota", max_digits=3, decimal_places=1, default=0.0)
    categories = models.ManyToManyField(Category, verbose_name="Categorias", related_name="movies")
    actors = models.ManyToManyField(Actor, verbose_name="Atores", related_name="movies")

    class Meta:
        verbose_name = "Filme"
        verbose_name_plural = "Filmes"
        ordering = ["-release_year", "title"]

    def __str__(self):
        return f"{self.title} ({self.release_year})"

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("movies:detail", kwargs={"slug": self.slug})
