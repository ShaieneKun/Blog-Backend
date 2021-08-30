from django import forms
from .models import Article
from markdownx.fields import MarkdownxFormField

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ("title", "body",)
        
        widgets = {
            'title':forms.TextInput(attrs={'class':'form-control'}),
            'body': MarkdownxFormField(),
        }

        labels = {
            'title': ('Title'),
        }
        
