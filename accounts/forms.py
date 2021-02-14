from django import forms
from django.contrib.auth import get_user_model, authenticate

User = get_user_model()


class RegisterForm(forms.Form):
  username = forms.CharField(
      widget=forms.TextInput(
          attrs={
              'placeholder': 'Enter Username'
          }
      )
  )
  email = forms.EmailField(
      widget=forms.TextInput(
          attrs={
              'placeholder': 'Enter Email'
          }
      )
  )
  password1 = forms.CharField(
      label='Password',
      min_length=5,
      max_length=30,
      widget=forms.PasswordInput(
          attrs={
            'placeholder': 'Enter Password'
          }
      )
  )
  password2 = forms.CharField(
      label='Confirm Password',
      max_length=30,
      widget=forms.PasswordInput(
          attrs={
            'placeholder': 'Confirm Password'
          }
      )
  )

  def clean_username(self):
    username = self.cleaned_data.get("username")
    qs = User.objects.filter(username__iexact=username)

    if qs.exists():
      raise forms.ValidationError(
          "This is an invalid user, please pick another username.")

    return username

  def clean_password2(self):
    confirm_password = self.cleaned_data.get('password2', '')
    original_password = self.cleaned_data.get('password1')
    if original_password != confirm_password:
      raise forms.ValidationError("Password doesn't match")

    return confirm_password

  def clean_email(self):
    email = self.cleaned_data.get("email")
    qs = User.objects.filter(email__iexact=email)

    if qs.exists():
      raise forms.ValidationError("This email is already in use.")

    return email


class LoginForm(forms.Form):
  username = forms.CharField(
      widget=forms.TextInput(
          attrs={
              'placeholder': 'Enter Username'
          }
      )
  )
  password = forms.CharField(
      widget=forms.PasswordInput(
          attrs={
              'placeholder': 'Enter Password'
          }
      )
  )

  # def clean_username(self):
  #   username = self.cleaned_data.get("username")
  #   qs = User.objects.filter(username__iexact=username)

  #   if not qs.exists():
  #     raise forms.ValidationError("This is an invalid user.")

  #   return username

  # def clean_password(self):
  #   username = self.cleaned_data.get("username")
  #   password = self.cleaned_data.get('password')
  #   user = authenticate(username=username, password=password)

  #   if user == None:
  #     raise forms.ValidationError("Invalid password.")

  #   return password

  def clean(self):
    username = self.cleaned_data.get('username')
    password = self.cleaned_data.get('password')

    if username and password:
      user = authenticate(username=username, password=password)

      if user == None:
        raise forms.ValidationError("Invalid username or password.")


class UserUpdateForm(forms.ModelForm):

  def __init__(self, user, *args, **kwargs):
    self.user = user
    super().__init__(*args, **kwargs)

  email = forms.EmailField()

  class Meta:
    model = User
    fields = ['username', 'email']

  def clean_username(self):
    username = self.cleaned_data.get("username")
    qs = User.objects.filter(username__iexact=username)

    if ' ' in username:
      raise forms.ValidationError(
          "This is an invalid user, username cannot have space.")

    if qs.exists():
      if self.user.username == username:
        pass
      else:
        raise forms.ValidationError(
            "This is an invalid user, please pick another username.")

    return username

  def clean_email(self):
    email = self.cleaned_data.get("email")
    qs = User.objects.filter(email__iexact=email)
    if qs.exists():
      if self.user.email == email:
        pass
      else:
        raise forms.ValidationError("This email is already in use.")

    return email
