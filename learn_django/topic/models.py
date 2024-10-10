from django.db import models
from django.utils.text import slugify


# Create your models here.
class Topic(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='topic/topic-images')
    slug = models.SlugField(max_length=150, unique=True, blank=True)

    def save(
        self,
        *args,
        force_insert=False,
        force_update=False,
        using=None,
        update_fields=None
    ):
        if not self.slug:
            slug = slugify(self.title)
            # Ensure the slug is unique
            duplicates = Topic.objects.filter(slug=slug).count()
            slug += f'-{duplicates}' if duplicates > 0 else ''
            self.slug = slug
        super(Topic, self).save(*args)

    def __str__(self):
        return self.title


class TopicMeta(models.Model):
    topic = models.OneToOneField(Topic, on_delete=models.CASCADE, related_name='metadata')
    likes = models.PositiveBigIntegerField(default=0)
    views = models.PositiveBigIntegerField(default=0)

    def viewed(self):
        """On viewed, increase the view metadata"""
        self.views += 1
        self.save()

    def liked(self):
        """On likes, increase the like metadata"""
        self.likes += 1
        self.save()

    def __str__(self):
        return f'Metadata: {self.topic.title}'
