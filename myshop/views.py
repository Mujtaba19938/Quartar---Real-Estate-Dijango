from django.shortcuts import render
from .models import Customer

def view_404(request):
    return render(request, "myshop/404.html")

def about(request):
    return render(request, "myshop/about.html")

def account(request):
    return render(request, "myshop/account.html")

def add_listing(request):
    return render(request, "myshop/add-listing.html")

def appointment(request):
    return render(request, "myshop/appointment.html")

def blog(request):
    return render(request, "myshop/blog.html")

def blog_details(request):
    return render(request, "myshop/blog-details.html")

def blog_grid(request):
    return render(request, "myshop/blog-grid.html")

def blog_left_sidebar(request):
    return render(request, "myshop/blog-left-sidebar.html")

def blog_right_sidebar(request):
    return render(request, "myshop/blog-right-sidebar.html")

def cart(request):
    return render(request, "myshop/cart.html")

def checkout(request):
    return render(request, "myshop/checkout.html")

def coming_soon(request):
    return render(request, "myshop/coming-soon.html")

def contact(request):
    return render(request, "myshop/contact.html")

def faq(request):
    return render(request, "myshop/faq.html")

def history(request):
    return render(request, "myshop/history.html")

def index(request):
    return render(request, "myshop/index.html")

def index_10(request):
    return render(request, "myshop/index-10.html")

def index_11(request):
    return render(request, "myshop/index-11.html")

def index_2(request):
    return render(request, "myshop/index-2.html")

def index_3(request):
    return render(request, "myshop/index-3.html")

def index_4(request):
    return render(request, "myshop/index-4.html")

def index_5(request):
    return render(request, "myshop/index-5.html")

def index_6(request):
    return render(request, "myshop/index-6.html")

def index_7(request):
    return render(request, "myshop/index-7.html")

def index_8(request):
    return render(request, "myshop/index-8.html")

def index_9(request):
    return render(request, "myshop/index-9.html")

def locations(request):
    return render(request, "myshop/locations.html")

def login(request):
    return render(request, "myshop/login.html")

def order_tracking(request):
    return render(request, "myshop/order-tracking.html")

def portfolio(request):
    return render(request, "myshop/portfolio.html")

def portfolio_2(request):
    return render(request, "myshop/portfolio-2.html")

def portfolio_details(request):
    return render(request, "myshop/portfolio-details.html")

def product_details(request):
    return render(request, "myshop/product-details.html")

def register(request):
    return render(request, "myshop/register.html")

def service(request):
    return render(request, "myshop/service.html")

def service_details(request):
    return render(request, "myshop/service-details.html")

def shop(request):
    return render(request, "myshop/shop.html")

def shop_grid(request):
    return render(request, "myshop/shop-grid.html")

def shop_left_sidebar(request):
    return render(request, "myshop/shop-left-sidebar.html")

def shop_list(request):
    return render(request, "myshop/shop-list.html")

def shop_right_sidebar(request):
    return render(request, "myshop/shop-right-sidebar.html")

def team(request):
    return render(request, "myshop/team.html")

def team_details(request):
    return render(request, "myshop/team-details.html")

def wishlist(request):
    return render(request, "myshop/wishlist.html")
