from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Complaint

# Public Home Landing Page
def home(request):
    return render(request, 'complaints/home.html')

# Student Dashboard (Complaints List)
@login_required
def complaint_list(request):
    complaints = Complaint.objects.filter(user=request.user).order_by('-created_at')
    return render(request, 'complaints/complaint_list.html', {'complaints': complaints})

@login_required
def submit_complaint(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        category = request.POST.get('category')
        description = request.POST.get('description')
        image = request.FILES.get('image')

        Complaint.objects.create(
            user=request.user,
            title=title,
            category=category,
            description=description,
            image=image
        )
        return redirect('complaint_list')

    return render(request, 'complaints/submit_complaint.html')