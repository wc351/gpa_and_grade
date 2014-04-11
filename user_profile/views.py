from user_profile.models import User_Profile
from django.core.urlresolvers import reverse_lazy
from django.views.generic import CreateView, TemplateView
from user_profile.forms import AddUserForm


class MapView(TemplateView):
    template_name = 'user_profile/map.html'


class CreateUserView(CreateView):
    model = User_Profile
    template_name = 'user_profile/profile.html'
    form_class = AddUserForm

    def get_success_url(self):
        return reverse_lazy('profile:map')

    def form_valid(self, form):
        if self.request.method == 'POST':
            data = form.cleaned_data
            username = data['username']
            year_level = data['year_level']
            lat = str(data['lat'])
            lon = str(data['lon'])
            school = data['school']
            geom = "POINT({} {})".format(lon, lat)
            newuser = User_Profile(username=username, year_level=year_level, lat=lat, lon=lon, school=school, geom=geom)
            return super(CreateUserView, self).form_valid(newuser)
