from django.db import models
from modules_installation.models import BasePluginConfig


class TestPluginConfig(BasePluginConfig):
    some_value = models.CharField(verbose_name="Some value", default="value")

    class Meta:
        managed = True


class TestModel1(models.Model):
    pass


class TestModel2(models.Model):
    pass