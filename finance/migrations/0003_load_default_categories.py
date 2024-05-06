from django.db import migrations


def load_default_categories(apps, schema_editor):
    Category = apps.get_model("finance", "Category")
    category = Category.objects.create(name="Other")
    category.save()
    category = Category.objects.create(name="Housing")
    category.save()
    category = Category.objects.create(name="Utilities")
    category.save()
    category = Category.objects.create(name="Entertainment")
    category.save()
    category = Category.objects.create(name="Food")
    category.save()
    category = Category.objects.create(name="Travel")
    category.save()


class Migration(migrations.Migration):

    dependencies = [
        ('finance', '0002_alter_category_options_alter_transaction_category_and_more copy'),
    ]

    operations = [
        migrations.RunPython(load_default_categories),
        
    ]
