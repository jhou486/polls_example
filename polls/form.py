from django import forms


class PersonForm(forms.Form):
    name = forms.CharField(label='글쓴이', max_length=30)
    text = forms.CharField(label='한줄리뷰')