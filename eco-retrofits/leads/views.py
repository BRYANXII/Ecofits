from django.shortcuts import render, redirect
from .forms import LeadForm

def lead_capture(request):
    if request.method == 'POST':
        form = LeadForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('thank_you')
    else:
        form = LeadForm()
    return render(request, 'leads/lead_form.html', {'form': form})

def thank_you(request):
    return render(request, 'leads/thank_you.html')
    
