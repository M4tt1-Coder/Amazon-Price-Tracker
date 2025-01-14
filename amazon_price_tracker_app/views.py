from django.shortcuts import render

# Create your views here.

# our home page 
def home(request):
    # store comparison information in session -> https://docs.djangoproject.com/en/5.1/topics/http/sessions/
    # TODO - Add the comparison feature
    comparison_product_ids = []
    if 'compared_products' in request.session:
        comparison_product_ids = request.session['compared_products']
    else:
        request.session['compared_products'] = []
    
    # check if more than 3 products have been compared
    # it is not allowed to compare more than 3 products
    to_many_compareed_products = len(comparison_product_ids) > 3
    
    # Mock data for dashboard page
    # mock data test data
    mock_products = [
        {'id': 'be81a713-523d-46e1-a4c2-1b52e3f53604', 'name': 'Product 1', 'description': 'Some Product 1', 'price': 1.99},
        {'id': 'be81a713-523d-46e1-a4c2-2b52e3f53604', 'name': 'Product 2', 'description': 'Some Product 2', 'price': 34.99},
        {'id': 'be81a713-523d-46e1-a4c2-3b52e3f53604', 'name': 'Product 3', 'description': 'Some Product 3', 'price': 13.59},
        {'id': 'be81a713-523d-46e1-a4c2-4b52e3f53604', 'name': 'Product 4', 'description': 'Some Product 4', 'price': 345.99},
        {'id': 'be81a713-523d-46e1-a4c2-5b52e3f53604', 'name': 'Product 5', 'description': 'Some Product 5', 'price': 23.00},
        {'id': 'be81a713-523d-46e1-a4c2-6b52e3f53604', 'name': 'Product 6', 'description': 'Some Product 6', 'price': 3.99},
        {'id': 'be81a713-523d-46e1-a4c2-7b52e3f53604', 'name': 'Product 7', 'description': 'Some Product 7', 'price': 7.49},
    ]
    context = {
        'products': mock_products,
        'compared_product_ids': comparison_product_ids,
        'to_many_compareed_products': to_many_compareed_products
    }
    return render(request, 'home.html', context)

# TODO - Finish the dashboard page
    
def dashboard(request, product_id):
    """
        Entrypoint for the dashboard page.
        
        Args:
            request: The HTTP request object.
            product_id: The ID of the product to be included in the dashboard.
    """
    # TODO - Include // Finish the 'get_product' function
    # product = get_product(product_id)
    mock_product = {'id': 4, 'name': 'Product 4', 'description': 'Some Product 4', 'price': 345.99}
    context = {
        'product': mock_product
    }
    return render(request, 'dashboard.html', context)