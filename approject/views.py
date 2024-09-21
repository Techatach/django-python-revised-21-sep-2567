from django.shortcuts import render
#from joblib import load
import joblib 
model = joblib.load(r'C:\Users\Taechatuch\Desktop\DjangoData\project\modeldata\diabetes_model.pkl')

def predictor(request):
    if request.method == 'POST':
        Pregnancies = request.POST['Pregnancies']
        Glucose = request.POST['Glucose']
        BloodPressure = request.POST['BloodPressure']
        SkinThickness = request.POST['SkinThickness']
        Insulin = request.POST['Insulin']
        BMI = request.POST['BMI']
        DiabetesPedigreeFunction = request.POST['DiabetesPedigreeFunction']
        Age = request.POST['Age']
        y_pred = model.predict([[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]]) 
        return render(request, 'result.html', {'result':y_pred})
    return render(request, 'index.html')


