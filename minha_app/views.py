

import asyncio
from django.http import HttpResponse

async def contador_de_tempo(request):
    for i in range(5):
        print(f"Contagem: {i}")
        await asyncio.sleep(1)

    return HttpResponse("Contagem concluída!")

