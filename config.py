from typing import Optional
from django.template.loader import render_to_string
from .models import TestPluginConfig as PluginConfigModel
from .apps import TestPluginConfig as PluginConfig


def get_module_config() -> Optional[str]:
    configs = PluginConfigModel.objects.all()
    config_global = configs.filter(virtual_host="global")
    configs_for_hosts = configs.exclude(virtual_host="global")
    if not configs.exists():
        return None
    config_template = "%s/config.yml" % PluginConfig.name
    context = {
        'module_name': PluginConfig.name,
        'config_global': config_global,
        'configs_for_hosts': configs_for_hosts
    }
    return render_to_string(template_name=config_template, context=context, request=None)
