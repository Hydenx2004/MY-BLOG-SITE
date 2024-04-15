from django.forms import ModelForm
from blog.models import Blog,Blog_id

class BlogForm(ModelForm):

    class Meta:

        model = Blog
        fields = ["Author","Blog_Id","Title","Image","Content"]


class BlogIdForm(ModelForm):

    class Meta:

        model = Blog_id
        fields = ["Blog_Id"]
