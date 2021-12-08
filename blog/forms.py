from django import forms
from django.forms import widgets
from .models import Article, Tag
from markdownx.fields import MarkdownxFormField


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article

        fields = (
            "title",
            "body",
        )

        widgets = {
            "title": forms.TextInput(attrs={"class": "form-control"}),
            "body": MarkdownxFormField(),
        }

        labels = {
            "title": ("Title"),
        }


class TagForm(forms.ModelForm):
    class Meta:
        model = Tag

        fields = "__all__"

        widgets = {"colour": forms.TextInput(attrs={"type": "color"})}
