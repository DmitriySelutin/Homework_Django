from django.views.generic import DetailView, ListView, DeleteView
from django.views.generic.edit import CreateView, UpdateView
from django.urls import reverse_lazy, reverse
from .models import Blog
from django.shortcuts import render


class BlogListView(ListView):
    model = Blog
    template_name = 'blog/home.html'
    context_object_name = 'blogs'

    def get_queryset(self):
        return Blog.objects.filter(sign_publication=True)


class BlogCreateView(CreateView):
    model = Blog
    fields = ['name', 'content', 'image', 'view_count', 'sign_publication']
    template_name = 'blog/blog_form.html'
    success_url = reverse_lazy('blog:home')


class BlogDetailView(DetailView):
    model = Blog
    template_name = 'blog/blog.html'
    context_object_name = 'blog'

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.view_count += 1
        self.object.save()
        return self.object


class BlogUpdateView(UpdateView):
    model = Blog
    fields = ['name', 'content', 'image', 'view_count', 'sign_publication']
    template_name = 'blog/blog_form.html'
    success_url = reverse_lazy('blog:home')

    def get_success_url(self):
        return reverse('blog:blog_detail', args=[self.kwargs.get('pk')])


class BlogDeleteView(DeleteView):
    model = Blog
    template_name = 'blog/blog_delete.html'
    success_url = reverse_lazy('blog:home')
