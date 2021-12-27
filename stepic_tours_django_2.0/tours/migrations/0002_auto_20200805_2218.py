from django.db import migrations, models


class Migration(migrations.Migration):

 class Migration(migrations.Migration):

    dependencies = [
        ('tours', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='airport',
            name='code',
            field=models.CharField(max_length=3),
        ),
        migrations.AlterField(
            model_name='airport',
            name='name',
            field=models.CharField(max_length=120),
        ),
        migrations.AlterField(
            model_name='airport',
            name='country',
            field=models.CharField(max_length=120),
        ),
        migrations.AlterField(
            model_name='airport',
            name='city',
            field=models.CharField(max_length=120),
        ),
        migrations.AlterField(
            model_name='airport',
            name='length',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='airport',
            name='lat',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='airport',
            name='lon',
            field=models.FloatField(),
        )

