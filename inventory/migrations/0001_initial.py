# 0001_initial.py

import django.db.models.deletion
from django.db import migrations, models

class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('products', '0001_initial'),  # Asegúrate de que 'products' esté como dependencia
    ]

    operations = [
        migrations.CreateModel(
            name='InventoryEntry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField(default=1)),
                ('provider', models.CharField(blank=True, max_length=200)),
                ('scanned_at', models.DateTimeField(auto_now_add=True)),
                ('duration_ms', models.PositiveIntegerField(default=0)),
                ('scenario', models.CharField(blank=True, default='', max_length=20)),
                # Aquí cambiamos 'variables.product' por 'products.product'
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='entries', to='products.product')),
            ],
            options={
                'indexes': [models.Index(fields=['scanned_at'], name='measurement_scanned_412d0a_idx'), models.Index(fields=['scenario'], name='measurement_scenari_b2227e_idx')],
            },
        ),
    ]
