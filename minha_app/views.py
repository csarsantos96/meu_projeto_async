

import asyncio
from django.http import HttpResponse

async def contador_de_tempo(request):
    for i in range(5):
        print(f"Contagem: {i}")
        await asyncio.sleep(1)  # espera 1 segundo de forma assíncrona

    return HttpResponse("Contagem concluída!")

