# Generated by Django 3.2.22 on 2023-10-10 08:54

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Autor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('apellidos', models.CharField(blank=True, max_length=200)),
                ('edad', models.IntegerField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Biblioteca',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('fechaCreacion', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('apellidos', models.CharField(max_length=200)),
                ('email', models.CharField(max_length=200, unique=True)),
                ('puntos', models.FloatField(db_column='puntos_biblioteca', default=5.0)),
                ('telefono', models.IntegerField()),
                ('dni', models.CharField(max_length=30, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Libro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200)),
                ('idioma', models.CharField(choices=[('ES', 'Español'), ('EN', 'Inglés'), ('FR', 'Frances'), ('IT', 'Italiano')], default='ES', max_length=2)),
                ('descripcion', models.TextField()),
                ('fecha_publicacion', models.DateField()),
                ('ISBN', models.CharField(max_length=200, unique=True)),
                ('genero', models.CharField(choices=[('TR', 'Terror'), ('MS', 'Misterio'), ('FN', 'Fantasia'), ('CF', 'Ciencia Ficción'), ('SP', 'Suspense')], max_length=2)),
                ('autores', models.ManyToManyField(to='biblioteca.Autor')),
                ('biblioteca', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='biblioteca.biblioteca')),
            ],
        ),
        migrations.CreateModel(
            name='Prestamo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_prestamo', models.DateTimeField(default=django.utils.timezone.now)),
                ('Cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='biblioteca.cliente')),
                ('libro', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='biblioteca.libro')),
            ],
        ),
        migrations.CreateModel(
            name='DatosCliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('direccion', models.TextField()),
                ('gustos', models.TextField()),
                ('telefono', models.IntegerField()),
                ('altura', models.FloatField()),
                ('peso', models.FloatField()),
                ('cliente', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='biblioteca.cliente')),
            ],
        ),
    ]