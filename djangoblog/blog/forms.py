from django import forms
from blog.models import Post,Category
class PostForm(forms.ModelForm):

    class Meta:
       model = Post
       fields = ['title', 'content','category','tag','image']

    def __init__(self, *args, **kwargs):
       user = kwargs.pop('user')
       super(PostForm, self).__init__(*args, **kwargs)
       self.fields['category'].queryset = Category.objects.filter(Blog=user)

class PostSearchForm(forms.Form):
    search_word = forms.CharField(label='Search Word')