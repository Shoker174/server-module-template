from django.views.generic import TemplateView
from modules_installation.views import BasePluginView


class ModuleInfoView(BasePluginView, TemplateView):
    page_section = 'modules'
    template_name = 'index.html'

    def get(self, request, *args, **kwargs):

        context = {
            'module_name': 'testapp45'
        }

        return self.render_to_response(context)


class ModuleMenuSubItemView(BasePluginView, TemplateView):
    page_section = 'modules'
    template_name = 'index.html'

    def get(self, request, *args, **kwargs):

        context = {
            'module_name': 'testapp45'
        }
        print(context)
        return self.render_to_response(context)
