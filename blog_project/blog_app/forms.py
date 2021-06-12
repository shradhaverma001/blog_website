from django import forms
from blog_app.models import Post,Comment

class PostForm(forms.ModelForm):

    class Meta():
        model = Post    #to connect to the model.
        fields = ('author','title','text')
        # widgets: dict you can hover at below widgets. it is a dictionary for formatting purposes.
        # TextInput(attrs={'class':'textinputclass'}) - widget name and attributes(attrs). which is a sub dictionary 
        widgets={
            'title':forms.TextInput(attrs={'class':'textinputclass'}),
            'text':forms.Textarea(attrs={'class':'editable medium-editor-textarea postcontent'})
            # the 'class':'editable medium-editor-textarea postcontent' is used to allow us to connect to some sort of medium editor and are three css classes and postcontent
            #  is our own class we created. we are connectiong text area attribute to text field in blog post form.
        }

class CommentForm(forms.ModelForm):

    class Meta():
        model = Comment
        fields = ('author','text')

        widgets = {
            'author':forms.TextInput(attrs={'class':'textinputclass'}),
            'text':forms.Textarea(attrs={'class':'editable medium-editor-textarea'})
        }
