from django.shortcuts import render

def dashboard(request):
    # Add any logic or data retrieval needed for your dashboard here
    return render(request, 'dashboard.html')
