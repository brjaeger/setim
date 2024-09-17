from django.shortcuts import render, redirect   # Tambahkan import redirect di baris ini
from main.forms import MoodEntryForm
from main.models import MoodEntry

def create_mood_entry(request):
    form = MoodEntryForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        form.save()
        return redirect('main:show_main')

    context = {'form': form}
    return render(request, "create_mood_entry.html", context)

def show_main(request):
    mood_entries = MoodEntry.objects.all()
    
    context = {
        'npm' : '2306165742',
        'name': 'Bryan Mitch',
        'class': 'PBP A',
        'mood_entries': mood_entries   
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

    return render(request, "main.html", {'data' : context, 'products' : products, 'mood_entries' : mood_entries})




