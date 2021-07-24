from django.http.response import JsonResponse
from django.shortcuts import redirect, render
import datetime
import json
from smtplib import SMTPAuthenticationError

from django.core.mail.message import EmailMessage
from django.template.loader import render_to_string

from carts.models import Cart, CartItem
from .models import Order, OrderProduct, Payment
from .forms import OrderForm

# Create your views here.


def payments(request):
    body = json.loads(request.body)
    order = Order.objects.get(
        user=request.user, is_ordered=False, order_number=body["orderID"]
    )

    # Store transaction details inside the Payment model
    payment = Payment(
        user=request.user,
        payment_id=body["transID"],
        payment_method=body["payment_method"],
        amount_paid=order.order_total,
        status=body["status"],
    )
    payment.save()

    order.payment = payment
    order.is_ordered = True
    order.save()

    # Move the cart items to Order Product table
    cart_items = CartItem.objects.filter(user=request.user)

    for item in cart_items:
        order_product = OrderProduct()
        order_product.order = order
        order_product.payment = payment
        order_product.user = request.user
        order_product.product = item.product
        order_product.quantity = item.quantity
        order_product.product_price = item.product.price
        order_product.ordered = True
        order_product.save()

        # many-to-many fields - to populate after saving
        product_variations = item.variations.all()
        order_product.variations.set(product_variations)
        order_product.save()

        # Reduce the quantity of the sold products
        product = item.product
        product.stock -= item.quantity
        product.save()

    # Clear cart
    cart_items.delete()

    # Send order received email to customer
    mail_subject = "Thank you for order!"
    message = render_to_string(
        "orders/order_received_email.html",
        {
            "user": request.user,
            "order": order,
        },
    )
    to_email = request.user.email
    send_email = EmailMessage(mail_subject, message, to=[to_email])
    try:
        send_email.send()
    except SMTPAuthenticationError:
        pass

    # Send order number and transaction id back to
    res_data = {"order_number": order.order_number, "transID": payment.payment_id}

    return JsonResponse(res_data)


def place_order(request):
    current_user = request.user

    # If cart count is less than or equal to 0, to redirect to shop
    cart_items = CartItem.objects.filter(user=current_user)
    cart_count = cart_items.count()
    if cart_count <= 0:
        return redirect("store")

    total = 0
    quantity = 0

    for cart_item in cart_items:
        total += cart_item.product.price * cart_item.quantity
        quantity += cart_item.quantity

    tax = (2 * total) / 100
    grand_total = total + tax

    if request.method == "POST":
        form = OrderForm(request.POST)
        if form.is_valid():
            # Store all the billing information inside Order table
            data = Order()
            data.first_name = form.cleaned_data["first_name"]
            data.last_name = form.cleaned_data["last_name"]
            data.phone = form.cleaned_data["phone"]
            data.email = form.cleaned_data["email"]
            data.address_line_1 = form.cleaned_data["address_line_1"]
            data.address_line_2 = form.cleaned_data["address_line_2"]
            data.country = form.cleaned_data["country"]
            data.state = form.cleaned_data["state"]
            data.city = form.cleaned_data["city"]
            data.order_note = form.cleaned_data["order_note"]

            # Auto populate other fields
            data.order_total = grand_total
            data.tax = tax
            data.ip = request.META.get("REMOTE_ADDR")
            data.user = current_user

            # Save one time to generate the id for Order Number generation
            data.save()

            # Generate order number
            yr = int(datetime.date.today().strftime("%Y"))
            dt = int(datetime.date.today().strftime("%d"))
            mt = int(datetime.date.today().strftime("%m"))
            d = datetime.date(yr, mt, dt)
            current_date = d.strftime("%Y%m%d")  # 20210305
            order_number = current_date + str(data.id)
            data.order_number = order_number
            data.save()

            order = Order.objects.get(
                user=current_user, is_ordered=False, order_number=order_number
            )
            context = {
                "order": order,
                "cart_items": cart_items,
                "total": total,
                "tax": tax,
                "grand_total": grand_total,
            }
            return render(request, "orders/payment.html", context)
        else:
            print(form.errors)
    return redirect("checkout")


def order_complete(request):
    order_number = request.GET.get("order_number")
    transID = request.GET.get("payment_id")

    try:
        order = Order.objects.get(order_number=order_number, is_ordered=True)
        payment = Payment.objects.get(payment_id=transID)
        ordered_products = OrderProduct.objects.filter(order=order).all()
        sub_total = 0
        for i in ordered_products:
            sub_total += i.product.price * i.quantity

        context = {
            "order": order,
            "ordered_products": ordered_products,
            "payment": payment,
            "sub_total": sub_total,
        }
        return render(request, "orders/order_complete.html", context)
    except (Payment.DoesNotExist, Order.DoesNotExist):
        return redirect("home")
