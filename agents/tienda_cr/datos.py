# Datos inventados para el taller. Precios en colones (CRC).

PRODUCTOS = {
    "SKU-001": {"nombre": "Laptop Lenovo IdeaPad 3 Ryzen 5 16GB/512GB", "categoria": "laptop", "precio": 389_000, "stock": 14},
    "SKU-002": {"nombre": "Laptop HP Victus 15 RTX 4050 i5", "categoria": "laptop gamer", "precio": 649_000, "stock": 6},
    "SKU-003": {"nombre": "MacBook Air M3 13\" 16GB/256GB", "categoria": "laptop", "precio": 739_000, "stock": 3},
    "SKU-004": {"nombre": "Laptop ASUS ROG Strix G16 RTX 4070 i9", "categoria": "laptop gamer", "precio": 1_189_000, "stock": 0},
    "SKU-005": {"nombre": "Laptop Acer Aspire 5 i3 8GB/256GB", "categoria": "laptop", "precio": 279_000, "stock": 22},
    "SKU-010": {"nombre": "PC Escritorio Dell OptiPlex i5 16GB/512GB", "categoria": "escritorio", "precio": 459_000, "stock": 9},
    "SKU-011": {"nombre": "PC Gamer Pura Vida Ryzen 7 RTX 4060 Ti", "categoria": "escritorio gamer", "precio": 899_000, "stock": 4},
    "SKU-012": {"nombre": "Mac mini M4 16GB/512GB", "categoria": "escritorio", "precio": 529_000, "stock": 2},
    "SKU-020": {"nombre": "Monitor LG 27\" IPS 144Hz", "categoria": "monitor", "precio": 159_000, "stock": 18},
    "SKU-021": {"nombre": "Monitor Samsung Odyssey G5 32\" curvo", "categoria": "monitor", "precio": 219_000, "stock": 1},
    "SKU-030": {"nombre": "Teclado mecánico Redragon Kumara", "categoria": "accesorio", "precio": 24_900, "stock": 40},
    "SKU-031": {"nombre": "Mouse Logitech MX Master 3S", "categoria": "accesorio", "precio": 59_900, "stock": 12},
    "SKU-042": {"nombre": "Audífonos inalámbricos Sony WH-1000XM5", "categoria": "accesorio", "precio": 189_000, "stock": 12},
}

VENTAS_SEMANA = {
    "SKU-001": 11, "SKU-002": 7, "SKU-003": 5, "SKU-004": 3, "SKU-005": 9,
    "SKU-010": 2, "SKU-011": 5, "SKU-012": 3, "SKU-020": 6, "SKU-021": 4,
    "SKU-030": 8, "SKU-031": 3, "SKU-042": 6,
}

PEDIDOS = {
    "0182": {"cliente": "María Jiménez", "estado": "en camino", "provincia": "Puntarenas", "productos": ["SKU-001"], "entrega_estimada": "2026-10-22"},
    "0183": {"cliente": "Carlos Vargas", "estado": "preparando", "provincia": "San José", "productos": ["SKU-020", "SKU-030"], "entrega_estimada": "2026-10-21"},
    "0184": {"cliente": "Ana Solís", "estado": "entregado", "provincia": "Guanacaste", "productos": ["SKU-042"], "entrega_estimada": "2026-10-18"},
}

ENVIO_POR_PROVINCIA = {
    "san jose": (3_500, 1), "heredia": (3_500, 1), "alajuela": (4_000, 1), "cartago": (4_000, 1),
    "puntarenas": (5_500, 3), "guanacaste": (5_500, 3), "limon": (5_500, 3),
}
