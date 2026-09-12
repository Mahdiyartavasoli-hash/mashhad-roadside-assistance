from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [('core', '0001_initial')]

    operations = [
        migrations.AddField(
            model_name='lead',
            name='website',
            field=models.CharField(blank=True, help_text='Spam honeypot. Should remain empty.', max_length=120),
        ),
        migrations.AlterField(
            model_name='lead',
            name='status',
            field=models.CharField(choices=[('new', 'جدید'), ('contacted', 'تماس گرفته شد'), ('in_progress', 'در حال پیگیری'), ('completed', 'تکمیل شد'), ('cancelled', 'لغو شد')], default='new', max_length=30),
        ),
        migrations.AddIndex(
            model_name='blogpost',
            index=models.Index(fields=['published', '-published_at'], name='core_blogpo_publishe_1a8a4c_idx'),
        ),
        migrations.AddIndex(
            model_name='blogpost',
            index=models.Index(fields=['slug'], name='core_blogpo_slug_6e7f3b_idx'),
        ),
        migrations.AddIndex(
            model_name='lead',
            index=models.Index(fields=['status', '-created_at'], name='core_lead_status_2fcb9a_idx'),
        ),
        migrations.AddIndex(
            model_name='lead',
            index=models.Index(fields=['phone'], name='core_lead_phone_9d98f7_idx'),
        ),
    ]
