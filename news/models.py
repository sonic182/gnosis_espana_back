from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.utils.text import slugify


class Category(models.Model):
    name = models.CharField(max_length=90)
    slug_name = models.SlugField(max_length=90, null=True, blank=True)

    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

@receiver(pre_save, sender=Category)
def save_slug_name_category(sender, instance, **kwargs):
    instance.slug_name = instance.slug_name if instance.slug_name != '' else slugify(instance.name)


class Tag(models.Model):
    name = models.CharField(max_length=90)
    slug_name = models.SlugField(max_length=90, null=True, blank=True)

    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

@receiver(pre_save, sender=Tag)
def save_slug_name_tag(sender, instance, **kwargs):
    instance.slug_name = instance.slug_name if instance.slug_name != '' else slugify(instance.name)


class PostAbstract(models.Model):
    title = models.CharField(max_length=120)
    slug_title = models.SlugField(max_length=120, null=True, blank=True)
    content = models.TextField()
    categories = models.ManyToManyField(Category)
    tags = models.ManyToManyField(Tag)

    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def see_categories(self):
        res = ''
        for category in self.categories.all():
            res += category.name  + ', '
        return res[:-2]

    def see_tags(self):
        res = ''
        for tag in self.tags.all():
            res += tag.name  + ', '
        return res[:-2]

    class Meta:
        abstract = True


class Draft(PostAbstract):
    pass

@receiver(pre_save, sender=Draft)
def save_slug_title_draft(sender, instance, **kwargs):
    instance.slug_title = instance.slug_title if instance.slug_title != '' else  slugify(instance.title)


class Post(PostAbstract):
    active = models.BooleanField(default=False)

@receiver(pre_save, sender=Post)
def save_slug_title_post(sender, instance, **kwargs):
    instance.slug_title = instance.slug_title if instance.slug_title != '' else  slugify(instance.title)
