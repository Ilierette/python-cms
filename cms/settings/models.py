from django.db import models



class Banner(models.Model):
    # bannery widoczne na stronie głównej
    # jeśli jest jeden - statyczny obraz
    # jeśli kilka - karuzela
    # CTA button dotyczący bannera

    title = models.CharField(max_length=200, null=True)
    subtitle = models.CharField(max_length=200, blank=True, null=True)
    image = models.ImageField(upload_to="banners", null=True)
    active = models.BooleanField()
    button_text = models.CharField(max_length=200, blank=True, null=True)
    button_link = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        verbose_name = "Banner"
        verbose_name_plural = "Banners"

    def __str__(self):
        return self.title


class MenuItem(models.Model):
    # linki menu na stronie głównej

    name = models.CharField(max_length=200, null=True)
    url = models.SlugField(default="", max_length=200, blank=True, null=True)
    order = models.IntegerField(default=0)

    # wybierak menu rodzica dla menu wielopoziomowych
    parent = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True)

    class Meta:
        verbose_name = "Menu"
        verbose_name_plural = "Menu"
        ordering = ["order"]

    def __str__(self):
        return self.name


TYPES = [
    ("SHOP", 'Shop'),
    ("GALLERY", 'Gallery'),
    ("PORTFOLIO", 'Portfolio')
]

class MainPageSections(models.Model):
    # Sekcje i ich kolejność na stronie głównej

    title = models.CharField(max_length=200, null=True)
    subtitle = models.CharField(max_length=200, blank=True, null=True)
    button_text = models.CharField(max_length=200, null=True)
    button_link = models.CharField(max_length=200, null=True)
    order = models.IntegerField(default=0)
    type = models.CharField(max_length=200, choices=TYPES, null=True)

    class Meta:
        verbose_name = "Page Section"
        verbose_name_plural = "Page Sections"
        ordering = ["order"]
        
    def __str__(self):
        return self.title
