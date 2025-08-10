from django.db import migrations


def normalize_phones(apps, schema_editor):
    Flat = apps.get_model("property", "Flat")
    import phonenumbers
    from phonenumbers import PhoneNumberFormat, format_number

    qs = (
        Flat.objects
        .exclude(owners_phonenumber__isnull=True)
        .exclude(owners_phonenumber="")
        .iterator()
    )

    for flat in qs:
        try:
            parsed = phonenumbers.parse(flat.owners_phonenumber, "RU")
        except phonenumbers.NumberParseException:
            flat.owner_pure_phone = None
            flat.save(update_fields=["owner_pure_phone"])
            continue

        if phonenumbers.is_valid_number(parsed):
            flat.owner_pure_phone = format_number(parsed, PhoneNumberFormat.E164)
        else:
            flat.owner_pure_phone = None

        flat.save(update_fields=["owner_pure_phone"])


class Migration(migrations.Migration):

    dependencies = [
        ("property", "0006_flat_likes_flat_owner_pure_phone_complaint"),
    ]

    operations = [
        migrations.RunPython(normalize_phones, migrations.RunPython.noop),
    ]
