
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('subjects', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('notif_type', models.CharField(choices=[('subject_mentioned', 'Mentioned in Subject'), ('comment_mentioned', 'Mentioned in Comment'), ('comment', 'Comment on Subject'), ('follow', 'Followed by someone'), ('sent_msg_request', 'Sent a Message Request'), ('confirmed_msg_request', 'Sent a Message Request')], default='Comment on Subject', max_length=500)),
                ('is_read', models.BooleanField(default=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('Actor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='c_acts', to=settings.AUTH_USER_MODEL)),
                ('Object', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='act_notif', to='subjects.Subject')),
                ('Target', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='c_notif', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('-created',),
            },
        ),
    ]
