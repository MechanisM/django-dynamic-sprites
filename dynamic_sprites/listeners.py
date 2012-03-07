# coding: utf8

import os

from django.conf import settings

from dynamic_sprites.model_sprite import ModelSprite


class ModelSpriteListener(object):

    def __init__(self, name, image_field, slug_field, queryset):
        self.name = name
        self.image_field = image_field
        self.slug_field = slug_field
        self.queryset = queryset

    def __call__(self, sender, instance, created, raw, using, **kwargs):
        queryset = self.get_queryset(instance)
        sprite = ModelSprite(
            name=self.name,
            queryset=queryset,
            image_field=self.image_field,
            slug_field=self.slug_field
        )
        image = sprite.generate()
        image.save(self.image_absolute_path)
        css = sprite.generate_css(self.image_filename)
        css.save(self.css_absolute_path)

    def get_queryset(self, instance):
        return self.queryset  # or instance.__class__._default_manager.all()

    @property
    def image_absolute_path(self):
        return os.path.join(settings.MEDIA_ROOT, self.image_filename)

    @property
    def image_filename(self):
        return self.name + '.png'

    @property
    def css_absolute_path(self):
        return os.path.join(settings.MEDIA_ROOT, self.name + '.css')
