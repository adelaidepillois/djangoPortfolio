from django.db import models


class Seo(models.Model):
    date_created = models.DateTimeField(
        verbose_name="Date de création",
        auto_now_add=True
    )
    date_updated = models.DateTimeField(
        verbose_name="Date de modification",
        auto_now=True
    )
    url = models.CharField(
        verbose_name="Url de la page",
        max_length=255,
        unique=True
    )
    title = models.CharField(
        verbose_name="Meta Titre",
        max_length=255,
    )
    description = models.TextField(
        verbose_name="Meta Description",
    )