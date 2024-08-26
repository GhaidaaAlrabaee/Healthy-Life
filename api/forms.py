from django import forms

class BMICalculatorForm(forms.Form):
    weight = forms.DecimalField(label='Weight', max_digits=5, decimal_places=2)
    weight_unit = forms.ChoiceField(choices=[('kg', 'KG'), ('lbs', 'POUNDS')])
    height = forms.DecimalField(label='Height', max_digits=5, decimal_places=2)
    height_unit = forms.ChoiceField(choices=[('cm', 'CM'), ('inch', 'INCHES')])
