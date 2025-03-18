

import asyncio
    """
    The function `contador_de_tempo` asynchronously counts from 0 to 4 with a 1-second delay between
    each count and returns a HttpResponse when completed.
    
    :param request: The `request` parameter in the `contador_de_tempo` function represents an HTTP
    request object in Django. It contains information about the incoming request such as headers,
    method, and data. In this function, the request parameter is not being used, but it is a standard
    parameter in Django view functions
    :return: The function `contador_de_tempo` is returning a Django `HttpResponse` object with the
    message "Contagem concluída!".
    """
from django.http import HttpResponse

async def contador_de_tempo(request):
    for i in range(5):
        print(f"Contagem: {i}")
        await asyncio.sleep(1)

    return HttpResponse("Contagem concluída!")

