# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('test1', '0002_auto_20150417_2234'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='tit',
            new_name='title',
        ),
    ]
