from django.views.generic import TemplateView
# ListView, DetailView, DeleteView, UpdateView, CreateView, FormView
from django.shortcuts import render
from .models import Post


# Create your views here.


# def home(request):
#     return render(request, 'app/home.html')


class HomeView(TemplateView):
    template_name = "app/home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['posts'] = Post.objects.get(id=1)
        context['data'] = "Context is working"
        return context


class AboutView(TemplateView):
    template_name = "app/abt.html"
