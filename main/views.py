from django.shortcuts import render

def show_main(request):
    data = {
        'npm' : '2306165742',
        'name': 'Bryan Mitch',
        'class': 'PBP A'
    }

    products = [
        {
            'name': 'Game 1',
            'description': 'Adventure',
            'price': 100000,
        },
        {
            'name': 'Game 2',
            'description': 'Simulator',
            'price': 80000,
        },
        {
            'name': 'Game 3',
            'description': 'Battle Royale',
            'price': 200000,
        }
    ]



    return render(request, "main.html", {'data' : data, 'products' : products})