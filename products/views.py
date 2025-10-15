from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from products.models import Product
import time

def register_product_page(request):
    return render(request, "products/register.html")

@csrf_exempt
def register_product_api(request):
    if request.method == "POST":
        import json
        try:
            data = json.loads(request.body)
            barcode = data.get("barcode", "").strip()
            name = data.get("name", "").strip()
            provider = data.get("provider", "").strip()
            if not barcode:
                return JsonResponse({"ok": False, "error": "barcode requerido"}, status=400)
            t0 = time.time()
            product, created = Product.objects.get_or_create(
                barcode=barcode,
                defaults={"name": name, "provider": provider}
            )
            t1 = time.time()
            duration_ms = int((t1 - t0) * 1000)
            return JsonResponse({
                "ok": True,
                "product_id": product.id,
                "created": created,
                "duration_ms": duration_ms
            })
        except Exception as e:
            return JsonResponse({"ok": False, "error": str(e)}, status=500)
    return JsonResponse({"ok": False, "error": "Método no permitido"}, status=405)