from django.db import migrations


def link_owners(apps, schema_editor):
    Flat = apps.get_model("property", "Flat")
    Owner = apps.get_model("property", "Owner")

    qs = (
        Flat.objects
        .only("id", "owner", "owners_phonenumber")
        .iterator()
    )
    for flat in qs:
        name = (getattr(flat, "owner", "") or "").strip()
        phone = (getattr(flat, "owners_phonenumber", "") or "").strip()
        if not name and not phone:
            continue
        owner = Owner.objects.filter(name=name, phonenumber=phone).first()
        if owner:
            owner.owned_flats.add(flat)


class Migration(migrations.Migration):

    dependencies = [
        ("property", "0008_import_owners_from_flats"),
    ]

    operations = [
        migrations.RunPython(link_owners, migrations.RunPython.noop),
    ]
