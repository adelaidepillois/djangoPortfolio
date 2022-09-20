from django.db import models


class Experience(models.Model):
    order = models.IntegerField(
        verbose_name="Ordre"
    )

    date_created = models.DateTimeField(
        verbose_name="Date de création",
        auto_now_add=True
    )
    date_updated = models.DateTimeField(
        verbose_name="Date de modification",
        auto_now=True
    )
    title = models.CharField(
        max_length=255, verbose_name="Nom de l'expérience"
    )
    location = models.CharField(
        max_length=255, verbose_name="Lieu de l'expérience",
        default='Bordeaux'
    )
    content = models.TextField(
        verbose_name="Détail de l'expérience'"
    )
    image = models.ImageField(
        verbose_name="Image de l'expérience"
    )
    logo = models.ImageField(
        verbose_name="Logo de l'expérience",
        default='logo'
    )
    is_active = models.BooleanField(
        verbose_name="Expérience active"
    )
    date_started = models.DateField(
        verbose_name="Date de début",
        default='10/09/2022'
    )
    date_ended = models.DateField(
        verbose_name="Date de fin",
        default='10/09/2022'
    )
    date_published = models.TextField(
        verbose_name="Année de l'expérience"
    )

    class Meta:
        verbose_name = "Expérience"
        verbose_name_plural = "Expérience"
        ordering = ['order']

    def __str__(self):
        return self.title


class Skill(models.Model):
    order = models.IntegerField(
        verbose_name="Ordre"
    )

    date_created = models.DateTimeField(
        verbose_name="Date de création",
        auto_now_add=True
    )
    date_updated = models.DateTimeField(
        verbose_name="Date de modification",
        auto_now=True
    )
    INFO = 'IN'
    THEO = 'TH'
    SOFT = 'ST'
    CAT_CHOICES = (
        (INFO, 'Informatique'),
        (THEO, 'Théorique'),
        (SOFT, 'Soft-Skills')
    )
    category = models.CharField(
        verbose_name="Catégorie",
        choices=CAT_CHOICES,
        max_length=2,
        default=INFO
    )
    title = models.CharField(
        max_length=255, verbose_name="Nom de l'expérience"
    )
    logo = models.ImageField(
        verbose_name="Logo de l'expérience",
        default='logo'
    )
    is_active = models.BooleanField(
        verbose_name="Expérience active"
    )

    class Meta:
        verbose_name = "Expérience"
        verbose_name_plural = "Expérience"
        ordering = ['order']

    def __str__(self):
        return self.title
