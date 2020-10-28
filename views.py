from django.views.generic import TemplateView

class ModuleInfoView(TemplateView):
    page_section = 'modules'
    template_name = 'index.html'

    def get(self, request, *args, **kwargs):

        context = {
            'module_name': 'testapp45'
        }

        return self.render_to_response(context)
