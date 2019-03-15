from django.shortcuts import render

# Create your views here.
def blog_display(request):
    if request.method == 'POST':
        pass
    else:
        return render(request,'blog/form.html',{})