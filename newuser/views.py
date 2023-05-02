from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'user/home.html')
def header(request):
    return render(request,'user/header.html')
def enquire(request):
    return render(request,'user/enquire.html')
def footer(request):
    return render(request,'user/footer.html')
def about(request):
    return render(request,'user/about.html')
def placement(request):
    return render(request,'user/placement.html')
def blog(request):
    return render(request,'user/blog.html')


