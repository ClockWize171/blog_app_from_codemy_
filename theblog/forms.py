from django import forms
from django.forms import widgets
from .models import Comment, Post,Category

# choices = [('coding','coding'), ('sports', 'sports'), ('arts', 'arts')]
choices = Category.objects.all().values_list('name', 'name')

# choices_list = []

# for i in choices:
#     choices_list.append(i)

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'title_tag', 'image_field', 'author', 'category', 'body')
        widgets = {
            'title' : forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Write your title here!'}),
            'title_tag' : forms.TextInput(attrs={'class': 'form-control'}),
            'author' : forms.TextInput(attrs={'class': 'form-control', 'value' : '' , 'id' : 'author', 'type': 'hidden'}),
            # 'author' : forms.Select(attrs={'class': 'form-control'}),
            'category' : forms.Select(choices=choices, attrs={'class': 'form-control'}),
            'body' : forms.Textarea(attrs={'class': 'form-control'}),
        }
    
class EditForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'title_tag', 'body')

        widgets = {
            'title' : forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Write your title here!'}),
            'title_tag' : forms.TextInput(attrs={'class': 'form-control'}),
            'body' : forms.Textarea(attrs={'class': 'form-control'}),
        }

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'body')

        widgets = {
            'name' : forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Write your Name!'}),
            'body' : forms.Textarea(attrs={'class': 'form-control'}),
        }