from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("property", "0012_rename_user_fix_balcony"),
    ]

    operations = [
        migrations.RenameField(
            model_name="owner",
            old_name="name",
            new_name="full_name",
        ),
        migrations.RenameField(
            model_name="owner",
            old_name="phonenumber",
            new_name="phone_number",
        ),
        migrations.RenameField(
            model_name="owner",
            old_name="owned_flats",
            new_name="flats",
        ),
        migrations.RenameField(
            model_name="flat",
            old_name="likes",
            new_name="liked_by",
        ),
    ]
