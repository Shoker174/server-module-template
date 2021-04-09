from typing import Optional
from django.template.loader import render_to_string
from .models import TestPluginConfig


def get_module_config(config_instance) -> Optional[str]:
    if not isinstance(config_instance, TestPluginConfig):
        return None
    config_template = 'test_plugin/config.yml'
    context = {
        "module_name": "test_plugin",
        'some_key': "key",
        "some_value": config_instance.some_value
    }
    return render_to_string(template_name=config_template, context=context, request=None)
