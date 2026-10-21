import unicodedata

from .datos import ENVIO_POR_PROVINCIA, PEDIDOS, PRODUCTOS, VENTAS_SEMANA

DESCUENTO_MAXIMO = 0.20


def _normalizar(texto: str) -> str:
    texto = unicodedata.normalize("NFD", texto.lower())
    return "".join(c for c in texto if unicodedata.category(c) != "Mn")


# --- Catálogo ---

def buscar_productos(consulta: str) -> dict:
    """Busca productos por nombre o categoría (ej: 'laptop', 'gamer', 'monitor', 'macbook')."""
    palabras = _normalizar(consulta).split()
    resultados = [
        {"sku": sku, "nombre": p["nombre"], "precio_crc": p["precio"], "stock": p["stock"]}
        for sku, p in PRODUCTOS.items()
        if any(w in _normalizar(p["nombre"] + " " + p["categoria"]) for w in palabras)
    ]
    return {"total": len(resultados), "productos": resultados}


def consultar_stock(sku: str) -> dict:
    """Devuelve cuántas unidades quedan de un producto según su SKU (ej: 'SKU-042')."""
    producto = PRODUCTOS.get(sku.upper())
    if not producto:
        return {"error": f"No existe el producto {sku}"}
    return {"sku": sku.upper(), "nombre": producto["nombre"], "stock": producto["stock"]}


# --- Pedidos ---

def ver_pedido(numero: str) -> dict:
    """Consulta el estado de un pedido por su número (ej: '0182')."""
    pedido = PEDIDOS.get(numero.lstrip("#"))
    if not pedido:
        return {"error": f"No existe el pedido #{numero}"}
    return {"numero": numero.lstrip("#"), **pedido}


def calcular_envio(provincia: str) -> dict:
    """Calcula el costo (CRC) y los días de envío a una provincia de Costa Rica."""
    datos = ENVIO_POR_PROVINCIA.get(_normalizar(provincia))
    if not datos:
        return {"error": f"No hacemos envíos a '{provincia}'"}
    return {"provincia": provincia, "costo_crc": datos[0], "dias_habiles": datos[1]}


# --- Administración ---

def sugerir_reposicion() -> dict:
    """Lista los productos que se deberían reponer según stock actual y ventas de la semana."""
    sugerencias = [
        {"sku": sku, "nombre": p["nombre"], "stock": p["stock"], "ventas_semana": VENTAS_SEMANA[sku]}
        for sku, p in PRODUCTOS.items()
        if p["stock"] < VENTAS_SEMANA[sku]
    ]
    return {"reponer": sorted(sugerencias, key=lambda s: s["stock"] - s["ventas_semana"])}


def cambiar_precio(sku: str, nuevo_precio: int, confirmado: bool = False) -> dict:
    """Cambia el precio de UN producto. Requiere confirmado=True, que solo se envía
    después de que el usuario confirme explícitamente el cambio."""
    producto = PRODUCTOS.get(sku.upper())
    if not producto:
        return {"error": f"No existe el producto {sku}"}

    # El backend valida, no el modelo.
    minimo = int(producto["precio"] * (1 - DESCUENTO_MAXIMO))
    if nuevo_precio < minimo:
        return {"rechazado": f"Política: el descuento máximo es {int(DESCUENTO_MAXIMO * 100)}%. Precio mínimo: ₡{minimo:,}"}
    if not confirmado:
        return {"requiere_confirmacion": f"¿Confirmás cambiar {producto['nombre']} de ₡{producto['precio']:,} a ₡{nuevo_precio:,}?"}

    anterior, producto["precio"] = producto["precio"], nuevo_precio
    return {"ok": True, "sku": sku.upper(), "precio_anterior": anterior, "precio_nuevo": nuevo_precio}
