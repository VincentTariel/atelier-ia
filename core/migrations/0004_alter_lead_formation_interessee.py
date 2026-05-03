# Migration manuelle — alignement choices + verbose_name pour le pivot
# coaching 1-to-1 Claude Desktop. Pas de modification de schéma BDD
# (CharField max_length=20 inchangé).

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_alter_lead_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lead',
            name='formation_interessee',
            field=models.CharField(
                choices=[
                    ('decouverte', 'Découvrir Claude Desktop pour mon métier'),
                    ('cas_precis', "J'ai un cas précis en tête"),
                    ('guide_pdf',  'Je veux juste recevoir le guide PDF'),
                ],
                default='decouverte',
                max_length=20,
                verbose_name="Sujet d'intérêt",
            ),
        ),
    ]
