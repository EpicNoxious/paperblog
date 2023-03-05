from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post
from .forms import PostForm, EditForm
from django.contrib.auth.models import User
from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect 
from django.contrib import messages

from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth.mixins import UserPassesTestMixin

class IndexView(ListView): 
    model = Post
    template_name = 'index.html'
    queryset = Post.objects.order_by('-date_of_create')[:4]
 
def LikeView(request, pk):
    post = get_object_or_404(Post, id=request.POST.get('post_id'))
    liked = False
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
        liked = False
        messages.success(request, 'you unliked this blog')
    else:
        post.likes.add(request.user)
        liked = True
        messages.success(request, 'you liked this blog')
    return HttpResponseRedirect(reverse('blog', args=[str(pk)]))

class BlogsView(ListView): 
    model = Post
    template_name = 'blogs.html'
    queryset = Post.objects.order_by('-date_of_create')[:]

class BlogView(DetailView): 
    model = Post
    template_name = 'blog.html'

    def get_context_data(self, *args, **kwargs):
        context = super(BlogView, self).get_context_data(*args, **kwargs)
        title = str(context['post'])
        index = title.find(' ')
        title1 = title[0:index]
        title2 = title[index+1:len(title)]
        context["titleLine"] = title1       
        context["titleSubLine"] = title2  

        position = get_object_or_404(Post, id=self.kwargs['pk'])
        total_likes = position.total_likes()
        liked = False 
        if position.likes.filter(id=self.request.user.id):
            liked = True    
        context["total_likes"] = total_likes
        context["liked"] = liked
        return context
    
class AddBlogView(UserPassesTestMixin, CreateView): 
    model = Post
    form_class = PostForm
    template_name = 'add.html'
    success_url = reverse_lazy('blogs')
    def test_func(self):
        if(self.request.user.is_superuser):
            form = PostForm(self.request.POST)
            if form.is_valid():
                messages.success(self.request, 'Blog post added!')
                return super().form_valid(form)
            return self.request.user.is_superuser
    def handle_no_permission(self):
        messages.error(self.request, "Only admin is allowed to add a blog!")
        return redirect(reverse('blogs'))
    
class UpdateBlogView(UserPassesTestMixin, UpdateView): 
    model = Post
    form_class = EditForm
    template_name = 'update.html'
    def test_func(self):
        if(self.request.user.is_superuser):
            form = EditForm(self.request.POST)
            if form.is_valid():
                messages.success(self.request, 'Blog post updated!')
                return super().form_valid(form)
            return self.request.user.is_superuser
    def handle_no_permission(self):
        messages.error(self.request, "Only admin is allowed to update a blog!")
        return redirect(reverse('blog', kwargs={'pk': self.kwargs['pk']}))
    

class DeleteBlogView(UserPassesTestMixin, DeleteView): 
    model = Post
    template_name = 'delete.html'
    success_url = reverse_lazy('blogs')
    def test_func(self):
        if(self.request.user.is_superuser):
            if self.request.method == 'POST':
                messages.success(self.request, 'Blog post deleted!')
            return self.request.user.is_superuser
    def handle_no_permission(self):
        messages.error(self.request, "Only admin is allowed to delete a blog!")
        return redirect(reverse('blog', kwargs={'pk': self.kwargs['pk']}))
    
    