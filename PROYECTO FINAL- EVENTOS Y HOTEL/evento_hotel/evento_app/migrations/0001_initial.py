# Generated by Django 4.2.5 on 2023-11-18 04:53

from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Acompanante',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_acomp', models.CharField(max_length=20)),
                ('apellido_acomp', models.CharField(max_length=20)),
                ('dni_acomp', models.BigIntegerField()),
                ('tel_acomp', models.BigIntegerField()),
                ('Id_part', models.BigIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Agenda',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Id_evento', models.BigIntegerField()),
                ('fecha_event_agend', models.DateField()),
                ('hora_event_agend', models.TimeField()),
                ('lugar_event_agend', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Empleado',
            fields=[
                ('Id_empleado', models.BigAutoField(primary_key=True, serialize=False)),
                ('nombre_emple', models.CharField(max_length=30)),
                ('apellido_emple', models.CharField(max_length=30)),
                ('telef_emple', models.BigIntegerField()),
                ('correo_emple', models.EmailField(max_length=45)),
            ],
        ),
        migrations.CreateModel(
            name='Evento',
            fields=[
                ('nombre_evento', models.CharField(max_length=30)),
                ('fecha_evento', models.DateField()),
                ('lugar_evento', models.CharField(max_length=30)),
                ('descripcion_evento', models.CharField(max_length=30)),
                ('presupuesto_evento', models.BigIntegerField()),
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='EventoEmpleado',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ID_EMPLEADO', models.BigIntegerField()),
                ('ID_EVENTO', models.BigIntegerField()),
                ('fecha_asignacion', models.DateField()),
                ('horario_de_trabajo', models.TimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('Id_usuario', models.BigAutoField(primary_key=True, serialize=False)),
                ('nombre_usu', models.CharField(max_length=20)),
                ('apellido_usu', models.CharField(max_length=30)),
                ('correo_usu', models.EmailField(max_length=45)),
                ('fechaRegistro_usu', models.DateField(auto_now_add=True)),
                ('groups', models.ManyToManyField(related_name='usuarios', to='auth.group')),
                ('user_permissions', models.ManyToManyField(related_name='usuarios', to='auth.permission')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Participante',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_part', models.CharField(max_length=20)),
                ('apellido_part', models.CharField(max_length=20)),
                ('tel_part', models.BigIntegerField()),
                ('lugar_procedencia', models.CharField(max_length=30)),
                ('fecha_llegada', models.DateField()),
                ('evento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='participantes', to='evento_app.evento')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Participantes',
            },
        ),
    ]
