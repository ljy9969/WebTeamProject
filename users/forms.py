from django import forms
from users.models import Member

class LoginForm(forms.ModelForm):
    class Meta:
        model = Member
        fields = ['username', 'password']
        labels = {
            'username': '사용자 이름',
            'password': '비밀번호'
        }
        widgets = {
            'username': forms.TextInput(
                attrs= {
                    'class': 'form-control',
                    'placeholder': '사용자 이름을 입력하세요'
                }
            ),
            'password': forms.PasswordInput(
                attrs= {
                    'class': 'form-control',
                    'placeholder': '비밀번호를 입력하세요'
                }
            )
        }