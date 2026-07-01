from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q, Count

from .models import Order
from .forms import OrderForm
from customers.models import Customer
from products.models import Product


def dashboard(request):

    total_customers = Customer.objects.count()
    total_products = Product.objects.count()
    total_orders = Order.objects.count()

    pending_orders = Order.objects.filter(status='Pending').count()
    completed_orders = Order.objects.filter(status='Completed').count()

    recent_orders = Order.objects.order_by('-created_at')[:5]

    popular_product = Order.objects.values('product__name').annotate(
        total_orders=Count('product')
    ).order_by('-total_orders').first()

    context = {
        'total_customers': total_customers,
        'total_products': total_products,
        'total_orders': total_orders,
        'pending_orders': pending_orders,
        'completed_orders': completed_orders,
        'recent_orders': recent_orders,
        'popular_product': popular_product,
    }

    return render(request, 'dashboard/dashboard.html', context)


def order_list(request):

    search = request.GET.get('search')
    orders = Order.objects.all()

    if search:
        orders = orders.filter(
            Q(customer__name__icontains=search) |
            Q(product__name__icontains=search)
        )

    for order in orders:
        order.total = order.product.price * order.quantity

    context = {
        'orders': orders,
        'search': search,
    }

    return render(request, 'orders/order_list.html', context)


def add_order(request):

    if request.method == 'POST':

        form = OrderForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('order_list')

    else:
        form = OrderForm()

    return render(request, 'orders/order_form.html', {
        'form': form
    })


def edit_order(request, id):

    order = get_object_or_404(Order, id=id)

    if request.method == 'POST':

        form = OrderForm(request.POST, instance=order)

        if form.is_valid():
            form.save()
            return redirect('order_list')

    else:
        form = OrderForm(instance=order)

    return render(request, 'orders/order_form.html', {
        'form': form
    })


def delete_order(request, id):

    order = get_object_or_404(Order, id=id)
    order.delete()

    return redirect('order_list')