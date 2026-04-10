from django.shortcuts import render, get_object_or_404
from .models import Category, Product
import urllib.parse

def home(request):
    categories = Category.objects.all()
    return render(request, 'index.html', {'categories': categories})

def category_products(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    products = category.products.all()
    return render(request, 'user stage.html', {'category': category, 'products': products})

import urllib.parse
from django.shortcuts import render, get_object_or_404


def product_detail(request, product_id):
    product = get_object_or_404(Product, id=product_id)

    brand_name = "Props Decore"
    image_url = request.build_absolute_uri(product.image.url) if product.image else ""

    price = f"₹{product.price}" if product.price else "N/A"

    message = f"""Hello {brand_name},

I would like to order this product:

• Product Name: {product.name}
• Price: {price}

Product Image:
{image_url}

Please share more details.
"""

    whatsapp_text = urllib.parse.quote(message)

    return render(request, 'product_details.html', {
        'product': product,
        'whatsapp_text': whatsapp_text,
        'whatsapp_number': '8592894615'
    })