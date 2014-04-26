from django.views.generic.list import ListView
from django.utils import timezone

from jobs.models import Job


class JobListView(ListView):

    model = Job

    def get_context_data(self, **kwargs):
        context = super(JobListView, self).get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context