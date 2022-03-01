from django import forms

class ContactForm(forms.form):
    name = forms.CharField(max_length=100, label='名前')
    email =forms.EmailField(max_length=100, label='メールアドレス')
    message = forms.CharField(lavel="メッセージ", widget=forms.Textarea())