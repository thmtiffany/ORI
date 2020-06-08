from django import forms

class TodoListForm(forms.Form):
    text = forms.CharField(max_length=100,
    widget = forms.TextInput(
    attrs={'class': 'form-control', 'placeholder': 'Insert new task here', 'aria-label':
    'Todo', 'aria-describedby': 'add-btn'}
    ))
