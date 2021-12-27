from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Airport',
            fields=[
                ('code', models.CharField(max_length=3)),
                ('name', models.CharField(max_length=120)),
                ('country', models.CharField(max_length=120)),
                ('city', models.CharField(max_length=120)),
                ('length', models.FloatField()),
                ],
        )
