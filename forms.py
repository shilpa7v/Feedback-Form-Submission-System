
from django import forms
from .models import Feedback, Product

class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ['customer_name', 'email', 'product', 'details', 'happy']

    product = forms.ModelChoiceField(queryset=Product.objects.all())  # Display products as a dropdown
