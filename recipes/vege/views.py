from django.shortcuts import render ,redirect
from vege.models import Receipe
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url = '/login/')
def receipes(request): 
    if request.method == "POST":
        data = request.POST
        receipe_name = data.get('receipe_name')
        receipe_description = data.get('receipe_description')
        receipe_image = request.FILES.get('receipe_image')
        Receipe.objects.create(
            receipe_name=receipe_name,
            receipe_description=receipe_description,
            receipe_image=receipe_image,
        )
        return redirect('/receipes')
    
    queryst = Receipe.objects.all()

    if request.GET.get('search'):
        queryst = queryst.filter(receipe_name__icontains = request.GET.get('search'))


    context = {'receipes': queryst}
    return render(request, 'receipes.html', context)


def delete_receipe(request , id):# receipe is delete method 
    queryset = Receipe.objects.get(id=id)
    queryset.delete()
    return redirect('/receipes/')


@login_required(login_url = '/login/')
def update_receipe(request, id):# receipe is update method  
    queryset = Receipe.objects.get(id=id)
    
    if request.method == "POST":
        data = request.POST
        receipe_name = data.get('receipe_name')
        receipe_description = data.get('receipe_description')
        receipe_image = request.FILES.get('receipe_image')

        queryset.receipe_name = receipe_name
        queryset.receipe_description = receipe_description

        if receipe_image:
            queryset.receipe_image = receipe_image

        queryset.save()
        return redirect('/receipes/')
    context = {'receipe': queryset}
    return render(request, 'update_receipe.html',context)