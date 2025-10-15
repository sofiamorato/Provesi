from django.shortcuts import render
import json
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt
from django.db.models import Avg
from inventory.logic.inventory_logic import register_inventory_scan
from inventory.models import InventoryEntry

def home(request):
    # Página con UN botón (más abajo el template)
    # Cambiar 'measurements/index.html' por 'inventory/index.html'
    return render(request, "inventory/index.html")  # Cambié aquí para que apunte a inventory/index.html

@csrf_exempt
@require_POST
def scan_api(request):
    """
    API para registrar la entrada tras el escaneo.
    Body JSON: { "barcode": "...", "quantity": 1, "provider": "ACME", "scenario": "normal|overloaded" }
    """
    try:
        body = json.loads(request.body or "{}")
    except json.JSONDecodeError:
        body = {}
    barcode = (body.get("barcode") or "").strip()
    qty = int(body.get("quantity") or 1)
    provider = (body.get("provider") or "").strip()
    scenario = (body.get("scenario") or "").strip()
    if not barcode:
        return JsonResponse({"ok": False, "error": "barcode requerido"}, status=400)

    try:
        # Llamada a la función 'register_inventory_scan' de 'inventory.logic.inventory_logic'
        entry, duration_ms = register_inventory_scan(barcode, qty=qty, provider=provider or None, scenario=scenario or None)
        return JsonResponse({
            "ok": True,
            "entry_id": entry.id,
            "barcode": entry.product.barcode,
            "duration_ms": duration_ms
        })
    except Exception as e:
        return JsonResponse({"ok": False, "error": str(e)}, status=500)

def metrics(request):
    """
    Métricas para validar ASR.
    - /inventory/metrics/ -> devuelve promedio global
    - /inventory/metrics/?scenario=normal
    - /inventory/metrics/?scenario=overloaded
    """
    scenario = (request.GET.get("scenario") or "").strip().lower()
    qs = InventoryEntry.objects.all()
    if scenario:
        qs = qs.filter(scenario=scenario)
    avg_ms = qs.aggregate(avg=Avg("duration_ms"))["avg"]
    return JsonResponse({"ok": True, "scenario": scenario or "all", "avg_duration_ms": round(avg_ms or 0, 2)})
