from django.shortcuts import render, redirect
from companies.models import Company

def index(request):
    companies = Company.objects.all().order_by('name')
    return render(request, 'companies/index.html', {"companies": companies})

def new(request):
    return render(request, 'companies/new.html')

def create(request):
    print(request.POST)
    company_name = request.POST.get("name")
    company_phone = request.POST.get("phone")
    company_email = request.POST.get("email")
    company_object = Company(name=company_name, phone=company_phone, email=company_email)
    company_object.save()
    return redirect("companies:index")

def info(request, company_id):
    company = Company.objects.get(pk=company_id)
    return render(request, "companies/info.html", {"company": company})


def edit_view(request, company_id):
    company = Company.objects.get(pk = company_id)
    return render(request, "companies/edit.html", {"company": company})

def edit(request, company_id):
    company = Company.objects.get(pk=company_id)
    company.name = request.POST.get("name")
    company.phone = request.POST.get("phone")
    company.email = request.POST.get("email")
    company.save()
    return redirect("companies:index")

def delete(request, company_id):
    company = Company.objects.get(pk=company_id)
    company.delete()
    return redirect("companies:index")


