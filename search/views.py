from django.shortcuts import render
from django.views import generic
from utils import get_results
from models import App


class HomeView(generic.View):
    def get(self, request):
        return render(request, 'search/home.html')


class SearchView(generic.ListView):
    template_name = 'search/search.html'

    def get_queryset(self):
        results = get_results(self.request.GET.get('query'))
        return results


class AppDetail(generic.DetailView):
    model = App
    template_name = 'search/detail.html'
