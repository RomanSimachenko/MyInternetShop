from django.shortcuts import redirect, render
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.db.models import Q
from .forms import CustomUserRegisterForm, CustomUserLoginForm
from .models import Category, Brand, Product, RecommendedProduct, Message, CartProduct, MailingList
from users.models import CustomUser


def errorPage(request):
    """Error page(may be not allowed there)"""
    request_value = request.GET.get('q', default='')

    return redirect(f"/shop/?q={request_value}") if request_value \
        else render(request, 'shop/error.html', {'request_value': request_value})


def login_registerPage(request):
    """login or register new user page"""
    request_value = request.GET.get('q', default='')

    if request_value:
        return redirect(f"/shop/?q={request_value}")

    # check authenticate
    if request.user.is_authenticated:
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

    # save login and register form
    login_form = CustomUserLoginForm()
    register_form = CustomUserRegisterForm()

    if request.method == 'POST':
        # check event login or register
        login_or_register = request.POST.get('login_or_register')
        if login_or_register == 'login':
            login_form = CustomUserLoginForm(request.POST)
            # do username in lowercase
            username = login_form['username'].value().lower()
            password = login_form['password'].value()

            # check if there is user in all registered users else error message
            try:
                user = CustomUser.objects.get(username=username)
            except:
                messages.error(request, "User doesn't exist")

            # authenticate user
            # if user is None it means that user password is incorrect
            user = authenticate(
                request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.error(
                    request, "Username or Password doesn't exist")
        else:
            register_form = CustomUserRegisterForm(request.POST)
            if register_form.is_valid():
                user = register_form.save(commit=False)
                # register new user with username in lowercase
                user.username = user.username.lower()
                user.save()
                login(request, user)
                return redirect('home')
            else:
                messages.error(
                    request, "An error occured during registration")

    return render(request, 'shop/login-register.html', {
        'login_form': login_form,
        'register_form': register_form,
        'request_value': request_value,
    })


def logoutUser(request):
    """Logout user"""
    request_value = request.GET.get('q', default='')

    if request_value:
        return redirect(f"/shop/?q={request_value}")

    if not request.user.is_authenticated:
        return redirect('login-register')

    # if form-button has been pressed - logout
    if request.method == 'POST':
        logout(request)
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

    return render(request, 'shop/confirm.html', {
        'confirm_text': 'Do you really want to logout?',
        'request_value': request_value,
    })


def index(request):
    """The Main(index) page of the site"""
    request_value = request.GET.get('q', default='')

    # get all categories and brands from the database and render them on the page
    category_list = Category.objects.all()
    brand_list = Brand.objects.all()

    # take the first five products and render them on the home page
    product_list = Product.objects.filter(
        Q(name__icontains=request_value) |
        Q(category__name__icontains=request_value) |
        Q(brand__name__icontains=request_value)
    )[:5]

    # get recommended products from the DB
    recommended_products = RecommendedProduct.objects.all()
    if recommended_products:
        recommended_products = RecommendedProduct.objects.all()[0].product.filter(
            Q(name__icontains=request_value) |
            Q(category__name__icontains=request_value) |
            Q(brand__name__icontains=request_value)
        )
    else:
        recommended_products = []

    return render(request, 'shop/index.html', {
        'category_list': category_list,
        'brand_list': brand_list,
        'product_list': product_list,
        'recommended_products': recommended_products,
        'category_tab': category_list[:5],
        'request_value': request_value,
    })


def shop(request):
    """Shop page"""
    request_value = request.GET.get('q', default='')

    # get all categories and brands from the database and render them on the page
    category_list = Category.objects.all()
    brand_list = Brand.objects.all()

    # take products from the database and render them on the shop page
    product_list = Product.objects.filter(
        Q(name__icontains=request_value) |
        Q(category__name__icontains=request_value) |
        Q(brand__name__icontains=request_value)
    )

    return render(request, 'shop/shop.html', {
        'category_list': category_list,
        'brand_list': brand_list,
        'product_list': product_list,
        'request_value': request_value,
    })


def cart(request):
    """Cart page"""
    request_value = request.GET.get('q', default='')

    if request_value:
        return redirect(f"/shop/?q={request_value}")

    if not request.user.is_authenticated:
        return redirect('login-register')

    cart_products = CartProduct.objects.filter(user=request.user)

    return render(request, 'shop/cart.html', {'cart_products': cart_products, 'request_value': request_value})


def checkout(request):
    """Checkout page"""
    request_value = request.GET.get('q', default='')

    if request_value:
        return redirect(f"/shop/?q={request_value}")

    if not request.user.is_authenticated:
        return redirect('login-register')

    cart_products = CartProduct.objects.filter(user=request.user)

    return render(request, 'shop/checkout.html', {'cart_products': cart_products, 'request_value': request_value})


def blog(request):
    """Blog page"""
    request_value = request.GET.get('q', default='')

    if request_value:
        return redirect(f"/shop/?q={request_value}")

    if not request.user.is_authenticated:
        return redirect('login-register')

    # get all categories and brands from the database and render them on the page
    category_list = Category.objects.all()
    brand_list = Brand.objects.all()

    return render(request, 'shop/blog.html', {
        'category_list': category_list,
        'brand_list': brand_list,
        'request_value': request_value,
    })


def contact(request):
    """Contact us page"""
    request_value = request.GET.get('q', default='')

    if request_value:
        return redirect(f"/shop/?q={request_value}")

    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        body = request.POST.get('body')
        new_message = Message(name=name, email=email,
                              subject=subject, body=body)
        new_message.save()
        return redirect('home')

    return render(request, 'shop/contact.html', {'request_value': request_value})


def product_detail(request, pk):
    """Product details page"""
    request_value = request.GET.get('q', default='')

    if request_value:
        return redirect(f"/shop/?q={request_value}")

    # get all categories and brands from the database and render them on the page
    category_list = Category.objects.all()
    brand_list = Brand.objects.all()

    # get product by id
    product = Product.objects.get(id=pk)

    # get recommended products from the DB
    recommended_products = RecommendedProduct.objects.all()[0].product.all()

    return render(request, 'shop/product_detail.html', {
        'product': product,
        'category_list': category_list,
        'brand_list': brand_list,
        'recommended_products': recommended_products,
        'request_value': request_value,
    })


def addCart(request, pk):
    """Add product to cart"""
    request_value = request.GET.get('q', default='')

    if request_value:
        return redirect(f"/shop/?q={request_value}")

    if not request.user.is_authenticated:
        return redirect('login-register')

    product = Product.objects.get(id=pk)

    try:
        cart_product = CartProduct.objects.get(product=product)
        if cart_product.quantity < cart_product.product.quantity:
            cart_product.quantity += 1
            cart_product.save()
    except:
        user = request.user
        cart = CartProduct(user=user, product=product)
        cart.save()

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'), {'request_value': request_value})


def deleteCart(request, pk):
    """Delete product from cart"""
    request_value = request.GET.get('q', default='')

    if request_value:
        return redirect(f"/shop/?q={request_value}")

    if not request.user.is_authenticated:
        return redirect('error')

    product = CartProduct.objects.get(id=pk)
    product.delete()

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'), {'request_value': request_value})


def changeQuantity(request, pk):
    """Change quantity of product"""
    request_value = request.GET.get('q', default='')

    if request_value:
        return redirect(f"/shop/?q={request_value}")

    if not request.user.is_authenticated:
        return redirect('error')

    product = CartProduct.objects.get(id=pk)

    if request.method == 'POST':
        quantity = int(request.POST.get('quantity'))
        if quantity > product.product.quantity:
            product.quantity = product.product.quantity
            product.save()
        elif quantity < 1:
            product.quantity = 1
            product.save()
        else:
            product.quantity = quantity
            product.save()

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'), {'request_value': request_value})


def addQuantity(request, pk):
    """Add quantity of product"""
    request_value = request.GET.get('q', default='')

    if request_value:
        return redirect(f"/shop/?q={request_value}")

    if not request.user.is_authenticated:
        return redirect('error')

    product = CartProduct.objects.get(id=pk)

    if product.quantity < product.product.quantity:
        product.quantity += 1
        product.save()

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'), 'request_value')


def reduceQuantity(request, pk):
    """Reduce quantity of product"""
    request_value = request.GET.get('q', default='')

    if request_value:
        return redirect(f"/shop/?q={request_value}")

    if not request.user.is_authenticated:
        return redirect('error')

    product = CartProduct.objects.get(id=pk)

    if product.quantity > 1:
        product.quantity -= 1
        product.save()

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'), {'request_value': request_value})


def addMail(request):
    """Add mail for mailing"""
    if not request.user.is_authenticated:
        return redirect('login-register')

    request_value = request.GET.get('q', default='')

    email = request.POST.get('email')
    try:
        MailingList.objects.get(email=email)
    except:
        new_email = MailingList(email=email)
        new_email.save()

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'), {'request_value': request_value})
