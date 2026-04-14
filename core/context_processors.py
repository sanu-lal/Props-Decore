from .models import Category

def site_settings(request):
    return {
        'site_name': 'Props Decore',
        'whatsapp_number': '1234567890'
    }

def nav_categories_processor(request):
    """
    Returns all categories to be available globally in templates,
    ordered alphabetically.
    """
    return {
        'nav_categories': Category.objects.all().order_by('name')
    }
