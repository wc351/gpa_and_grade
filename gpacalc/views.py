from django.views.generic import ListView, TemplateView, CreateView
from gpacalc.models import GPA
from django.core.urlresolvers import reverse_lazy
from gpacalc.utils import GetGPA


class MainView(TemplateView):
    template_name = "main_page.html"


class GpaView(TemplateView):
    template_name = "gpacalc/gpa.html"


class ClassView(CreateView):
    model = GPA
    template_name = 'gpacalc/addclasses.html'
    success_url = reverse_lazy('gpa:addclasses')


class AllClasses(ListView):
    model = GPA
    template_name = 'gpacalc/allclasses.html'
    success_url = reverse_lazy('gpa:allclasses')

    def get_queryset(self):
        return GPA.objects.filter(user=self.request.user)

    def get_context_data(self, **kwargs):
        context = super(AllClasses, self).get_context_data(**kwargs)
        user = GPA.objects.filter(user=self.request.user)
        if len(user) <= 0:
            context['gpa'] = "Please enter some classes."
        else:
            context['gpa'] = GetGPA(user)
        return context


