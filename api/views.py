from django.shortcuts import render
from django.shortcuts import render
from api.forms import BMICalculatorForm
from rest_framework.views import APIView

def home(request):
    return render(request, 'home.html')

def login_view(request):
    return render(request, 'login.html')

def bmi_calculator(request):
    result = None
    if request.method == 'POST':
        form = BMICalculatorForm(request.POST)
        if form.is_valid():
            weight = form.cleaned_data['weight']
            weight_unit = form.cleaned_data['weight_unit']
            height = form.cleaned_data['height']
            height_unit = form.cleaned_data['height_unit']

            # تحويل الوزن والطول إلى نفس الوحدة (المتر والكيلوغرام)
            if weight_unit == 'lbs':
                weight = weight * 0.453592
            if height_unit == 'inch':
                height = height * 0.0254

            # حساب BMI
            bmi = weight / (height ** 2)
            result = round(bmi, 2)
    else:
        form = BMICalculatorForm()

    return render(request, 'bmi_calculator.html', {'form': form, 'result': result})

def calories_calculator(request):
    return render(request, 'calories_calculator.html')

def food_calculator(request):
    return render(request, 'food_calculator.html')

def food_meals(request):
    return render(request, 'food_meals.html')

def signup_view(request):
    return render(request, 'signup.html')

def info_view(request):
    return render(request, 'more_info.html')



class BmiCalculatore(APIView):
    def post(request, self):
        pass