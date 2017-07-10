from django.shortcuts import render, redirect
from forms import ContactForm

# Create your views here.


def portfolio(request):
	data = {
		'name':'',
		'message':'',
		'subject':'',
		'message':''
	}
	form = ContactForm(data)
	if request.method=='POST':
		form = ContactForm(request.POST)
		if form.is_valid():
			obj = form.save(commit=False)
			obj.save()
			return redirect("posts:list")
	
	return render(request,"portfolio.html",{"form":form})