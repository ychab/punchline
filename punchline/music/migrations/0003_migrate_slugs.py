from django.db import migrations, models
from django.utils.text import slugify


def migrate_slug(apps, schema_editor):
    Artist = apps.get_model('music.Artist')
    Album = apps.get_model('music.Album')
    Song = apps.get_model('music.Song')

    slug_fields = {
        Artist: 'nickname',
        Album: 'name',
        Song: 'title',
    }
    for model, field in slug_fields.items():
        for obj in model.objects.all():
            obj.slug = slugify(getattr(obj, field))
            obj.save()


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0002_slug_fields'),
    ]

    operations = [
        migrations.RunPython(
            code=migrate_slug,
            reverse_code=migrations.RunPython.noop,
        ),
    ]
