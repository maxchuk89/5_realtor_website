from django.db import migrations


def import_owners(apps, schema_editor):
    Flat = apps.get_model("property", "Flat")
    Owner = apps.get_model("property", "Owner")

    flats = (
        Flat.objects
        .only("owner", "owners_phonenumber", "owner_pure_phone")
        .iterator()
    )

    for flat in flats:
        name = (flat.owner or "").strip()
        phone = (flat.owners_phonenumber or "").strip()
        pure = flat.owner_pure_phone

        if not name and not phone and not pure:
            continue

        defaults = {}
        if pure:
            defaults["pure_phone"] = pure

        Owner.objects.get_or_create(
            name=name,
            phonenumber=phone,
            defaults=defaults,
        )


class Migration(migrations.Migration):

    dependencies = [
    ("property", "0009_owner"),
    ]

    operations = [
        migrations.RunPython(import_owners, migrations.RunPython.noop),
    ]
