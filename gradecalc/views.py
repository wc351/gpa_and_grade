from django.views.generic import TemplateView, ListView, CreateView, DetailView
from gradecalc.models import Grade
from django.core.urlresolvers import reverse_lazy
from gradecalc.utils import GetGrade


class GradeView(TemplateView):
    template_name = "gradecalc/grade.html"


class GradeCalcView(CreateView):
    model = Grade
    template_name = "gradecalc/gradecalc.html"
    success_url = reverse_lazy('grade')


class ViewGrades(ListView):
    model = Grade
    template_name = "gradecalc/viewgrades.html"

    def get_queryset(self):
        return Grade.objects.filter(user=self.request.user)


class ViewClass(DetailView):
    model = Grade
    template_name = 'gradecalc/viewclass.html'

    def get_context_data(self, **kwargs):
        context = super(ViewClass, self).get_context_data(**kwargs)
        grade = Grade.objects.filter(pk=self.kwargs['pk'])[0]
        context['grade'] = GetGrade(grade)
        return context