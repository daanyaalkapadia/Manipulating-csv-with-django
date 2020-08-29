from django import forms
class DateInput(forms.DateInput):
    input_type = 'date'
class StudentRegistration(forms.Form):
  id = forms.IntegerField()
  name = forms.CharField()
  gender = forms.ChoiceField(widget=forms.RadioSelect,choices=[('Male','Male'),('Female','Female')])
  date_of_birth = forms.DateField(widget=DateInput)
  city = forms.CharField()
  state = forms.CharField()
  email = forms.EmailField()
  qualification = forms.CharField()
  stream = forms.CharField()

class StudentSearch(forms.Form):
  search = forms.IntegerField()