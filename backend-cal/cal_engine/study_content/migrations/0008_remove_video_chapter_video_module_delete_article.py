# Generated by Django 4.2.16 on 2024-12-03 13:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0002_module_section_alter_coursechapter_unique_together_and_more'),
        ('study_content', '0007_remove_videosegment_unique_assessment_per_video_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='video',
            name='chapter',
        ),
        migrations.AddField(
            model_name='video',
            name='module',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='videos', to='course.module'),
        ),
        migrations.DeleteModel(
            name='Article',
        ),
    ]