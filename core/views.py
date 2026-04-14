from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.db.models import Q
from .models import Category, Product
import urllib.parse

def home(request):
    categories = Category.objects.all()
    return render(request, 'index.html', {'categories': categories})

def category_products(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    products = category.products.all()
    return render(request, 'category_products.html', {'category': category, 'products': products})

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

    return render(request, 'product_detail.html', {
        'product': product,
        'whatsapp_text': whatsapp_text,
        'whatsapp_number': '8592894615'
    })

def search(request):
    query = request.GET.get('q', '')
    products = []
    if query:
        products = Product.objects.filter(
            Q(name__icontains=query) |
            Q(description__icontains=query) |
            Q(category__name__icontains=query)
        ).distinct()
    
    return render(request, 'search_results.html', {'products': products, 'query': query})

def search_suggest(request):
    query = request.GET.get('q', '')
    if query:
        products = Product.objects.filter(
            Q(name__icontains=query) |
            Q(description__icontains=query) |
            Q(category__name__icontains=query)
        ).distinct()[:5]
        
        results = []
        for p in products:
            image_url = p.image.url if p.image else ''
            results.append({
                'id': p.id,
                'name': p.name,
                'category': p.category.name,
                'image': image_url
            })
        return JsonResponse({'results': results})
    return JsonResponse({'results': []})