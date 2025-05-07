from django.http import JsonResponse
from producer import send_message

def produce_message(request):
    message = request.GET.get("message", "Hello from Django!")
    send_message(message)
    return JsonResponse({"status": "Message sent!", "message": message})
