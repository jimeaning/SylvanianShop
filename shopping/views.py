from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .models import Post

class PostList(ListView) :
    model = Post
    ordering = '-pk'
    # paginate_by = 5

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(PostList, self).get_context_data()
        # context['categories'] = Category.objects.all()
        # context['no_category_post_count'] = Post.objects.filter(category=None).count()
        return context
#    template_name = 'blog/post_list.html'

class PostDetail(DetailView) :
    model = Post

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(PostDetail, self).get_context_data()
        # context['categories'] = Category.objects.all()
        # context['no_category_post_count'] = Post.objects.filter(category=None).count()
        # context['comment_form'] = CommentForm
        return context

