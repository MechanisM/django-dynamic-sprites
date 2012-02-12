import os

from django.conf import settings
from django.test import TestCase

from dynamic_sprites.image import Image
from dynamic_sprites.packing import BinPacking, HorizontalPacking, VerticalPacking
from dynamic_sprites.sprite import Sprite

class HorizontalSpriteTestCase(TestCase):

    def setUp(self):
        self.sprite = Sprite('flags',
            images=[
                ('brazil', 'country/flags/brazil.gif'),
                ('usa', 'country/flags/usa.jpg'),
            ],
            packing_class=HorizontalPacking
        )

    def test_name(self):
        self.assertEqual('flags', self.sprite.name)
    
    def test_css_class(self):
        self.assertEqual('sprite-flags', self.sprite.css_class)
    
    def test_dimensions(self):
        self.assertEqual(475 + 476, self.sprite.width)
        self.assertEqual(max(335, 330), self.sprite.height)
    
    def test_sprite_image(self):
        generated = self.sprite.generate()
        self.assertEqual(self.sprite.width, generated.width)
        self.assertEqual(self.sprite.height, generated.height)
        
        path = 'country/flags/sprite.png'
        absolute_path = os.path.join(settings.MEDIA_ROOT, path)
        
        try:
            generated.save(path)
            self.assertTrue(os.path.exists(absolute_path))
            generated_from_fs = Image(path)
            self.assertEqual(generated.width, generated_from_fs.width)
            self.assertEqual(generated.height, generated_from_fs.height)
        finally:
            os.remove(absolute_path)


class VerticalSpriteTestCase(TestCase):
    
    def setUp(self):
        self.sprite = Sprite('flags',
            images=[
                ('brazil', 'country/flags/bra.png'),
                ('usa', 'country/flags/usa.png'),
                ('canada', 'country/flags/can.png'),
            ],
            packing_class=VerticalPacking
        )

    def test_name(self):
        self.assertEqual('flags', self.sprite.name)
    
    def test_css_class(self):
        self.assertEqual('sprite-flags', self.sprite.css_class)
    
    def test_dimensions(self):
        self.assertEqual(48, self.sprite.width)
        self.assertEqual(3*48, self.sprite.height)
    
    def test_sprite_image(self):
        generated = self.sprite.generate()
        self.assertEqual(self.sprite.width, generated.width)
        self.assertEqual(self.sprite.height, generated.height)
        
        path = 'country/flags/sprite.png'
        absolute_path = os.path.join(settings.MEDIA_ROOT, path)
        
        try:
            generated.save(path)
            self.assertTrue(os.path.exists(absolute_path))
            generated_from_fs = Image(path)
            self.assertEqual(generated.width, generated_from_fs.width)
            self.assertEqual(generated.height, generated_from_fs.height)
        finally:
            os.remove(absolute_path)


class BinSpriteTestCase(TestCase):

    def setUp(self):
        self.sprite = Sprite('flags',
            images=[
                ('brazil', 'country/flags/bra.png'),
                ('usa', 'country/flags/usa.png'),
                ('canada', 'country/flags/can.png'),
            ],
            packing_class=BinPacking
        )

    def test_name(self):
        self.assertEqual('flags', self.sprite.name)

    def test_css_class(self):
        self.assertEqual('sprite-flags', self.sprite.css_class)

    def test_dimensions(self):
        self.assertEqual(96, self.sprite.width)
        self.assertEqual(96, self.sprite.height)

    def test_sprite_image(self):
        generated = self.sprite.generate()
        self.assertEqual(self.sprite.width, generated.width)
        self.assertEqual(self.sprite.height, generated.height)

        path = 'country/flags/sprite.png'
        absolute_path = os.path.join(settings.MEDIA_ROOT, path)
        
        try:
            generated.save(path)
            self.assertTrue(os.path.exists(absolute_path))
            generated_from_fs = Image(path)
            self.assertEqual(generated.width, generated_from_fs.width)
            self.assertEqual(generated.height, generated_from_fs.height)
        finally:
            os.remove(absolute_path)
