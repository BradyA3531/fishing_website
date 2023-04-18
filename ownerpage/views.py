from django.shortcuts import render

# Create your views here.

#Reminder: Do Model Stuff later
def ownerpage_view(request):
    return render(request,'ownerpage/ownerpage.html')