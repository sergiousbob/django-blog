import form as form
from django import forms
from .models import Post, Category, Comment

#choices =[('хочу взять в руки','хочу взять в руки'), ('отдаю в руки', 'отдаю в руки')]
choices = Category.objects.all().values_list('name', 'name')

choice_list = []
for item in choices:
    choice_list.append (item)
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields =('title', 'title_tag', 'author','category', 'body', 'snippet', 'header_image')


        widgets ={
            'title': forms.TextInput(attrs = {'class': 'form-control', 'placeholder':'Введите заголовок поста'}),
            'title_tag': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Введите тег поста'}),
            'author': forms.TextInput(attrs={'class': 'form-control', 'value': '','id': 'elder', 'type': 'hidden'}),
            #'author': forms.Select(attrs={'class': 'form-control'}),
            'category': forms.Select(choices=choice_list, attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control', 'placeholder':'Введите текст поста'}),
            'snippet': forms.Textarea(attrs={'class': 'form-control'}),
        }

class EditForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'title_tag', 'body', 'snippet')


        widgets ={
            'title': forms.TextInput(attrs = {'class': 'form-control', 'placeholder':'Введите заголовок поста'}),
            'title_tag': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Введите тег поста'}),
            'author': forms.Select(attrs={'class': 'form-control'}),

            'body': forms.Textarea(attrs={'class': 'form-control', 'placeholder':'Введите текст поста'}),
            'snippet': forms.Textarea(attrs={'class': 'form-control'}),
        }

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'body')


        widgets ={
            'name': forms.TextInput(attrs = {'class': 'form-control', 'placeholder':'Введите заголовок поста'}),

            'body': forms.Textarea(attrs={'class': 'form-control', 'placeholder':'Введите текст поста'}),
        }