from django.http.response import JsonResponse
from django.shortcuts import render
from django.http import HttpResponse
from .models import Message   

def home(request):
    messages = Message.objects.order_by('-created_at')
    return render(request, 'dom2/home.html', {'messages': messages})

def send_message(request):
    if request.method == 'POST':
        text = request.POST.get('text', '').strip()

        if not text:
            return JsonResponse({'error': 'Messagem vazia.'}, status=400)

        word_count = len(text.split())

        msg = Message.objects.create(
            text=text,
            word_count=word_count
        )

        return JsonResponse({
            'text': msg.text,
            'created_at': msg.created_at.strftime('%d-%m-%Y %H:%M'),
            'word_count': msg.word_count
        })

    return JsonResponse({'error': 'Método inválido.'}, status=400)
