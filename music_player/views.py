from django.views.generic import TemplateView


class AppView(TemplateView):
    """
    Main view of the app.
    """
    template_name = 'music_player/index.html'
