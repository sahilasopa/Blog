from django import forms

from .models import Blog


class BlogEditForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ('heading', 'blog')

        widgets = {
            'heading': forms.TextInput(attrs={'class': 'form-control input input-tr'}),
            'blog': forms.Textarea(attrs={'class': 'form-control input modern-form__form-control--textarea'}),
        }
        labels = {
            'heading': 'Title'
        }


class NewBlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ('heading', 'blog')

        widgets = {
            'heading': forms.TextInput(attrs={'class': 'form-control input input-tr'}),
            'blog': forms.Textarea(
                attrs={'class': 'form-control input modern-form__form-control--textarea', }),
        }
        labels = {
            'heading': ''
        }
