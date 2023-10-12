from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User,auth
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

# Create your views here.
def home(request):
    return render(request,'index.html')
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('finalapp:new_page')
        else:
            messages.info(request, "Invalid credentials")
    return render(request, 'login.html')
def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        cpassword = request.POST['cpassword']
        if password == cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request, "Already registerd")
                return redirect('finalapp:register')
            else:
                user = User.objects.create_user(username=username, password=password)
                user.save();
                return redirect('finalapp:login')
                messages.info(request, " Register Successfully")
        else:
            messages.info(request, "password not matched")
            return redirect('finalapp:register')
        return redirect('/')
    return render(request, 'registration.html')


from django.contrib import messages

def new_page(request):
    if request.method == 'POST':
        return redirect('finalapp:new_page')  # Redirect to the 'order_form' view when the form is submitted
    return render(request, 'new_page.html')


def order_form(request):
    if request.method == 'POST':
        username = request.POST['username']
        dob = request.POST['dob']
        age = request.POST['age']
        gender = request.POST['gender']
        phone = request.POST['phone']
        mail_id = request.POST['mail_id']
        address = request.POST['address']
        department = request.POST['department']
        course = request.POST['course']
        purpose = request.POST['purpose']
        material = request.POST.get('material', '')  # Use an empty string as a default value if 'material' is not in request.POST
        user = User.objects.create_user = auth.authenticate(username=username, dob=dob, age=age, gender=gender, phone=phone, mail_id=mail_id,address=address, department=department, course=course, purpose=purpose,material=material)
        if purpose == "Place Order":
            messages.success(request, "Thank you for choosing us. Your order is confirmed")
        else:
            messages.success(request, "Thank you for interest")

    return render(request,'order_form.html')  # Redirect to the 'order_form' view after registration
