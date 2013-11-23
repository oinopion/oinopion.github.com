from django.db import models
from django.db.models import permalink
from django.core import signing
from django.utils.translation import ugettext_lazy as _
from model_utils import Choices
from model_utils.managers import QueryManager
from model_utils.models import TimeStampedModel, StatusModel


class Article(TimeStampedModel, StatusModel):
    STATUS = Choices(
        ('draft', _('draft')),
        ('published', _('published')),
    )

    title = models.CharField(_('title'), max_length=200)
    slug = models.SlugField(_('slug'), max_length=100)
    text = models.TextField(_('text'))

    objects = models.Manager()
    published = QueryManager(status=STATUS.published)

    signer = signing.TimestampSigner(salt="article")

    class Meta:
        ordering = ('-created',)

    @permalink
    def get_absolute_url(self):
        return 'article_detail', (), {'slug': self.slug}

    def signed_id(self):
        return self.signer.sign(str(self.pk))

    def is_signed_id(self, signature):
        try:
            pk = self.signer.unsign(signature)
            return str(self.pk) == pk
        except signing.BadSignature:
            return False
