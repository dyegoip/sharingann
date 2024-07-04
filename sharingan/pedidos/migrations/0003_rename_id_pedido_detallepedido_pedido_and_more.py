# Generated by Django 5.0.6 on 2024-07-04 03:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pedidos', '0002_detallepedido_id_alter_detallepedido_id_pedido'),
    ]

    operations = [
        migrations.RenameField(
            model_name='detallepedido',
            old_name='id_pedido',
            new_name='pedido',
        ),
        migrations.RenameField(
            model_name='detallepedido',
            old_name='id_producto',
            new_name='producto',
        ),
        migrations.RenameField(
            model_name='pedido',
            old_name='rut_cliente',
            new_name='cliente',
        ),
        migrations.AlterUniqueTogether(
            name='detallepedido',
            unique_together=set(),
        ),
        migrations.AddField(
            model_name='detallepedido',
            name='cantidad',
            field=models.PositiveIntegerField(default=1),
        ),
        migrations.AddField(
            model_name='detallepedido',
            name='precio_unitario',
            field=models.DecimalField(decimal_places=2, default=1, max_digits=10),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='pedido',
            name='id_pedido',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='pedido',
            name='total_pedido',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
        ),
        migrations.RemoveField(
            model_name='detallepedido',
            name='cantidad_producto',
        ),
        migrations.RemoveField(
            model_name='detallepedido',
            name='precio_producto',
        ),
    ]