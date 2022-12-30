from django import forms

from .models import Post

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title','author', 'text', 'image')
        labels = {
            'title': 'Az étel neve:',
            'author': 'A receptet készítette:',
            'text': 'A recept:',
            'image': 'Tölts fel az elkészült ételről egy képet!'
        }

    