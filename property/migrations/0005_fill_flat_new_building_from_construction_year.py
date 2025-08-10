from django.db import migrations


def set_new_building(apps, schema_editor):
    Flat = apps.get_model("property", "Flat")
    qs = Flat.objects.filter(new_building__isnull=True).exclude(construction_year__isnull=True)
    for flat in qs.iterator():
        flat.new_building = flat.construction_year >= 2015
        flat.save(update_fields=["new_building"])


class Migration(migrations.Migration):

    dependencies = [
        ("property", "0004_flat_new_building"),
    ]

    operations = [
        migrations.RunPython(set_new_building, migrations.RunPython.noop),
    ]
