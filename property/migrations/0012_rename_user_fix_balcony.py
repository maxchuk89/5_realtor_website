from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [

        ("property", "0011_remove_flat_owner_remove_flat_owner_pure_phone_and_more"),
    ]

    operations = [
        migrations.RenameField(
            model_name="complaint",
            old_name="user",
            new_name="complainant",
        ),
        migrations.AlterField(
            model_name="flat",
            name="has_balcony",
            field=models.BooleanField("Балкон", null=True, blank=True, db_index=True),
        ),
    ]
