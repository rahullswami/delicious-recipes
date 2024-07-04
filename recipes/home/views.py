from django.shortcuts import render
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required(login_url = '/login/')
def home(request):

    peoples = [
        {'name' : 'rahul swami' , 'age': 17},
        {'name' : 'ankur swami' , 'age':10},
        {'name' : 'mohit swami' , 'age': 59},
        {'name' : 'sachin jatav' , 'age': 15},
        {'name' : 'sonu sir' , 'age': 90},
        {'name' : 'rohit' , 'age': 89},
    ]

    text = ' Lorem ipsum dolor sit, amet consectetur adipisicing elit. Minus sed dolore non blanditiis corrupti quisquam unde placeat at amet! Sed et consequuntur ut porro similique modi asperiores impedit, quae, doloremque ipsum rerum eveniet, illo qui corporis. Nobis impedit iste iure, quae commodi eius natus, molestias sapiente ex eos fugit aliquid illum saepe dolor. Velit nulla magni eligendi veritatis voluptatem, laudantium magnam nostrum reprehenderit blanditiis ipsum impedit aspernatur placeat, sit rerum quo quibusdam commodi eveniet adipisci tenetur. Omnis error magni iste tenetur laborum eveniet ea nemo minima rerum quos, exercitationem praesentium quo cum rem incidunt in! Molestiae ipsa distinctio similique nulla.'

    page_name = {'page' : 'Home'}
    active = {'active' : 'active'}


    return render(request , 'index.html', context={'peoples': peoples , 'text':text,'page_name':page_name, 'active':active})

@login_required(login_url = '/login/')
def about(request):
    page_name= {'page' : 'About'}
    active = {'active' : 'active'}
    marks = [
        {'subject': 'math','mark': 90},
        {'subject': 'english','mark': 80},
        {'subject': 'science','mark': 30},
        {'subject': 'ss','mark': 40},
        {'subject': 'sanskrit','mark': 10},
        {'subject': 'japanes','mark': 100},
    ]
    return render(request, 'about.html', context={'page_name':page_name , 'marks': marks, 'active':active})
