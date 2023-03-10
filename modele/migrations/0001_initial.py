
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('boards', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(db_index=True, max_length=150)),
                ('slug', models.SlugField(blank=True, max_length=150, null=True)),
                ('body', models.TextField(blank=True, max_length=5000, null=True)),
                ('photo', models.ImageField(blank=True, null=True, upload_to='subject_photos/', verbose_name='Add image (optional)')),
                ('rank_score', models.FloatField(default=0.0)),
                ('active', models.BooleanField(default=True)),
                ('created', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='posted_subjects', to=settings.AUTH_USER_MODEL)),
                ('board', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='submitted_subjects', to='boards.Board')),
                ('mentioned', models.ManyToManyField(blank=True, related_name='m_in_subjects', to=settings.AUTH_USER_MODEL)),
                ('points', models.ManyToManyField(blank=True, related_name='liked_subjects', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('-created',),
            },
        ),
    ]
