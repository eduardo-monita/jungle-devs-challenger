from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from posts.models import Author

from main.utils import image_crop_optimizer, clean_unusable_thumbnails


@receiver(post_save, sender=Author)
def create_alticle(sender, instance, **kwargs):
    instance.picture = image_crop_optimizer(image=instance.picture, size=(200, 200))
    instance.picture_mobile = image_crop_optimizer(image=instance.picture, size=(100, 100), rename='mobile')
    
@receiver(post_delete, sender=Author)
def delete_article(sender, instance, using, **kwargs):
    clean_unusable_thumbnails(instance.picture)
    clean_unusable_thumbnails(instance.picture_mobile)
