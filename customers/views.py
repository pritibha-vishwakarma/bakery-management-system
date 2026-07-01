from django.shortcuts import render, redirect, get_object_or_404

from .models import Customer
from .forms import CustomerForm


def customer_list(request):

    customers = Customer.objects.all()

    context = {
        'customers': customers,
    }

    return render(request, 'customers/customer_list.html', context)


def add_customer(request):

    if request.method == 'POST':

        form = CustomerForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('customer_list')

    else:
        form = CustomerForm()

    context = {
        'form': form,
    }

    return render(request, 'customers/customer_form.html', context)


def edit_customer(request, id):

    customer = get_object_or_404(Customer, id=id)

    if request.method == 'POST':

        form = CustomerForm(request.POST, instance=customer)

        if form.is_valid():
            form.save()
            return redirect('customer_list')

    else:
        form = CustomerForm(instance=customer)

    context = {
        'form': form,
    }

    return render(request, 'customers/customer_form.html', context)


def delete_customer(request, id):

    customer = get_object_or_404(Customer, id=id)
    customer.delete()

    return redirect('customer_list')