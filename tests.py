from django.test import TestCase
from .models import TestPluginConfig as Config
from .config import get_module_config


class ConfigTestCase(TestCase):
    def setUp(self):
        Config.objects.create(virtual_host="global", some_key="bar", some_value="foo")
        Config.objects.create(virtual_host="example.com", some_key="foo", some_value="bar")

    def test_config(self):
        self.assertIsNotNone(get_module_config())
