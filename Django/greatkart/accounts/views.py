from .forms import RegistrationForm, UserProfileForm, UserForm
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib import messages, auth
from django.contrib.auth.decorators import login_required
import requests

# Verification Email
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes
from django.contrib.auth.tokens import default_token_generator
from django.core.mail import EmailMessage

from .models import Account, UserProfile
from carts.models import Cart, CartItem
from carts.views import _cart_id
from orders.models import Order, OrderProduct


# Create your views here.


def register(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data["first_name"]
            last_name = form.cleaned_data["last_name"]
            email = form.cleaned_data["email"]
            phone_number = form.cleaned_data["phone_number"]
            password = form.cleaned_data["password"]
            confirm_password = form.cleaned_data["confirm_password"]
            username = email.split("@")[0]

            if password != confirm_password:
                messages.error("Password and Confirm Password are not the same!")
                context = {"form": form}
                return render(request, "accounts/register.html", context)

            user = Account.object.create_user(
                first_name=first_name,
                last_name=last_name,
                email=email,
                username=username,
                password=password,
            )
            user.phone_number = phone_number
            user.save()

            # Create User Profile
            user_profile = UserProfile()
            user_profile.user = user
            user_profile.profile_picture = "default/default-user.jpg"
            user_profile.save()

            # User Activation
            current_site = get_current_site(request)
            mail_subject = "Please activate your account"
            message = render_to_string(
                "accounts/account_verification_email.html",
                {
                    "user": user,
                    "domain": current_site,
                    "uid": urlsafe_base64_encode(force_bytes(user.pk)),
                    "token": default_token_generator.make_token(user),
                },
            )
            to_email = email
            send_email = EmailMessage(mail_subject, message, to=[to_email])
            send_email.send()
            # messages.success(
            #     request,
            #     "Thank you for registering with us. We have sent you a verification email to your email address. Please verify it.",
            # )
            return redirect("/accounts/login/?command=verification&email=" + email)
    else:
        form = RegistrationForm()

    context = {"form": form}
    return render(request, "accounts/register.html", context)


def login(request):
    if request.method == "POST":
        email = request.POST["email"]
        password = request.POST["password"]

        user = auth.authenticate(email=email, password=password)

        print("Start to login")

        if user is not None:
            try:
                cart = Cart.objects.get(cart_id=_cart_id(request))
                is_cart_item_exists = CartItem.objects.filter(cart=cart).exists()
                if is_cart_item_exists:
                    cart_items = CartItem.objects.filter(cart=cart)

                    # Getting the product variations by cart id
                    for item in cart_items:
                        variation = item.variations.all()
                        variation = list(variation)

                        # Get the cart items from the user to access his product variations
                        ex_cart_items = CartItem.objects.filter(
                            user=user, product=item.product
                        )
                        ex_var_list = []
                        ids = []
                        for ex_item in ex_cart_items:
                            existing_variation = ex_item.variations.all()
                            ex_var_list.append(list(existing_variation))
                            ids.append(ex_item.id)

                        print(variation)
                        print(ex_var_list)

                        if variation in ex_var_list:
                            index = ex_var_list.index(variation)
                            item_id = ids[index]
                            ex_item = CartItem.objects.get(id=item_id)
                            ex_item.quantity += 1
                            ex_item.user = user
                            ex_item.save()
                        else:
                            item.user = user
                            item.save()
            except:
                pass

            auth.login(request, user)
            messages.success(request, "You are now logged in.")
            url = request.META.get("HTTP_REFERER")
            try:
                query = requests.utils.urlparse(url).query
                # next=/cart/checkout
                params = dict(x.split("=") for x in query.split("&"))
                if "next" in params:
                    nextPage = params["next"]
                    return redirect(nextPage)
            except:
                pass
            return redirect("dashboard")
        else:
            messages.error(request, "Invalid login credentials.")
            return redirect("login")

    return render(request, "accounts/login.html")


@login_required(login_url="login")  # login is required, if not, to route to 'login'
def logout(request):
    auth.logout(request)
    messages.success(request, "You are logged out.")
    return redirect("login")


def activate(request, uidb64, token):
    try:
        uid = urlsafe_base64_decode(
            uidb64
        ).decode()  # decode because we encoded in the email content
        user = Account._default_manager.get(pk=uid)
    except (TypeError, ValueError, OverflowError, Account.DoesNotExist):
        user = None

    if user is not None and default_token_generator.check_token(user, token):
        # user exists and token is valid
        user.is_active = True
        user.save()
        messages.success(request, "Congratulations! Your account is activated.")
        return redirect("login")
    else:
        messages.error(request, "Invalid activation link.")
        return redirect("register")


@login_required(login_url="login")
def dashboard(request):
    orders = Order.objects.order_by("-created_at").filter(
        user=request.user, is_ordered=True
    )
    orders_count = orders.count()
    user_profile = get_object_or_404(UserProfile, user=request.user)

    context = {"orders_count": orders_count, "user_profile": user_profile}
    return render(request, "accounts/dashboard.html", context)


def forgotPassword(request):
    if request.method == "POST":
        email = request.POST.get("email")
        if Account.object.filter(email=email).exists():
            user = Account.object.get(email__exact=email)

            # Password Reset email
            current_site = get_current_site(request)
            mail_subject = "Reset Your Password"
            message = render_to_string(
                "accounts/reset_password_email.html",
                {
                    "user": user,
                    "domain": current_site,
                    "uid": urlsafe_base64_encode(force_bytes(user.pk)),
                    "token": default_token_generator.make_token(user),
                },
            )
            to_email = email
            send_email = EmailMessage(mail_subject, message, to=[to_email])
            send_email.send()

            messages.success(
                request, "Password reset email has been sent to your email address."
            )
            return redirect("login")
        else:
            messages.error(request, "Account does not exist!")
            return redirect("forgotPassword")

    return render(request, "accounts/forgotPassword.html")


def resetPasswordValidate(request, uidb64, token):
    try:
        uid = urlsafe_base64_decode(
            uidb64
        ).decode()  # decode because we encoded in the email content
        user = Account._default_manager.get(pk=uid)
    except (TypeError, ValueError, OverflowError, Account.DoesNotExist):
        user = None

    if user is not None and default_token_generator.check_token(user, token):
        # user exists and token is valid
        request.session["uid"] = uid
        messages.success(request, "Please reset your password")
        return redirect("resetPassword")
    else:
        messages.error(request, "This link has been expired!")
        return redirect("login")


def resetPassword(request):
    if request.method == "POST":
        password = request.POST.get("password")
        confirm_password = request.POST.get("confirm_password")
        if password == confirm_password:
            uid = request.session.get("uid")
            user = Account.object.get(pk=uid)
            user.set_password(password)
            user.save()

            messages.info(request, "Password reset successful.")
            return redirect("login")
        else:
            messages.error(request, "Passwords do not match!")
            return redirect("resetPassword")

    return render(request, "accounts/resetPassword.html")


@login_required(login_url="login")
def my_orders(request):
    orders = Order.objects.order_by("-created_at").filter(
        user=request.user, is_ordered=True
    )
    context = {"orders": orders}
    return render(request, "accounts/my_orders.html", context)


@login_required(login_url="login")
def edit_profile(request):
    user_profile = get_object_or_404(UserProfile, user=request.user)

    if request.method == "POST":
        user_form = UserForm(request.POST, instance=request.user)
        profile_form = UserProfileForm(
            request.POST, request.FILES, instance=user_profile
        )
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()

            messages.success(request, "Your profile has been successfully updated.")
            return redirect("dashboard")
    else:
        user_form = UserForm(instance=request.user)
        profile_form = UserProfileForm(instance=user_profile)

    context = {
        "user_form": user_form,
        "profile_form": profile_form,
        "user_profile": user_profile,
    }
    return render(request, "accounts/edit_profile.html", context)


@login_required(login_url="login")
def change_password(request):
    if request.method == "POST":
        current_password = request.POST["current_password"]
        new_password = request.POST["new_password"]
        confirm_password = request.POST["confirm_password"]

        user = request.user

        if new_password == confirm_password:
            success = user.check_password(current_password)
            if success:
                user.set_password(new_password)
                user.save()

                messages.success(request, "Password updated successfully.")
                auth.logout(request)
                return redirect("login")
            else:
                messages.error(request, "Please enter a valid current password.")
                return redirect("change_password")
        else:
            messages.error(request, "Passwords do not match.")
            return redirect("change_password")

    return render(request, "accounts/change_password.html")


@login_required(login_url="login")
def order_detail(request, order_id):
    order = Order.objects.get(order_number=order_id, is_ordered=True, user=request.user)
    payment = order.payment

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

    return render(request, "accounts/order_detail.html", context)
