import random
import string
from django.utils import timezone
from django.shortcuts import get_object_or_404
from .models import LinkMapping


def shorten(url):
    random_hash = ''.join(
        random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for _ in range(7))
    mapping = LinkMapping(original_url=url, hash=random_hash, creation_date=timezone.now())
    mapping.save()
    return random_hash


def load_url(url_hash):
    return get_object_or_404(LinkMapping, hash=url_hash)
