import random
import string

from django.utils.text import slugify

def random_string_generator(size=10, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

def unique_slug_genereator(instance, new_slug=None):
    if new_slug is not None:
        slug = new_slug
    else:
        slug=slugify(instance.title)

    myClass=instance.__class__
    slug_exists=myClass.objects.filter(slug=slug).exists()
    if slug_exists:
        new_slug="{slug}-{randstr}".format(
            slug=slug,
            randstr=random_string_generator(size=4)
        )
        return unique_slug_genereator(instance, new_slug=new_slug)
    return slug