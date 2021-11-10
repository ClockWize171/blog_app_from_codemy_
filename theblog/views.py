from django.db.models.fields import SlugField
from django.shortcuts import render,get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from django.views.generic import (
    ListView as lv, 
    DetailView as dv,
    CreateView as cv,
    UpdateView as uv,
    DeleteView as delv, 
)
from .models import Category, Comment, Post
from .forms import CommentForm, PostForm, EditForm
from django.urls import reverse_lazy,reverse

def LikeView(request, pk):
    
        post = get_object_or_404(Post, id=request.POST.get('post_id'))
        liked = False
        if post.likes.filter(id=request.user.id).exists():
            post.likes.remove(request.user)
            liked = False
        else:
            post.likes.add(request.user)
            liked = True
        return HttpResponseRedirect(reverse('article_detail', args=[str(pk)]))
    
        #return HttpResponse("You must login First!")

class HomeView(lv):
    model = Post
    template_name = 'home.html'
    ordering = ['-publish_date']

    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        context = super(HomeView, self).get_context_data(*args, **kwargs)
        context["cat_menu"] = cat_menu
        return context

class DetailView(dv):
    model = Post
    template_name = 'article_detail.html'

    def get_context_data(self, *args, **kwargs):
        context = super(DetailView, self).get_context_data(*args, **kwargs)

        stuff = get_object_or_404(Post, id=self.kwargs['pk'])
        total_likes = stuff.total_likes()

        liked = False
        if stuff.likes.filter(id=self.request.user.id).exists():
            liked = True

        context["total_likes"] = total_likes
        context["liked"] = liked
        return context

class PostView(cv):
    model = Post
    form_class = PostForm
    template_name = 'add_post.html'
    #fields = '__all__'

class CategoryView(cv):
    model = Category
    #form_class = PostForm
    template_name = 'add_category.html'
    fields = '__all__'

def CategoryPageView(request, cats):
    template_name= "categories.html"
    category_post = Post.objects.filter(category=cats.replace('-', ' '))
    remove_hyphen = cats.capitalize().replace('-', ' ')
    context = {'cats': remove_hyphen, 'category_post': category_post}
    return render(request, template_name , context)

class UpdatePost(uv):
    model = Post
    form_class = EditForm
    template_name = 'update_post.html'
    #fields = ['title', 'title_tag', 'body']

class DeletePost(delv):
    model = Post
    template_name = 'delete_post.html'
    #fields = ['title', 'title_tag', 'body']
    success_url = reverse_lazy("home")

class AddCommentView(cv):
    model = Comment
    form_class = CommentForm
    template_name = 'add_comment.html'
    def form_valid(self,form):
        form.instance.post_id = self.kwargs['pk']
        return super().form_valid(form)
    #fields = '__all__'
    success_url = reverse_lazy("home")