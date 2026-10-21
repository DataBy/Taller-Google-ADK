# Taller Google ADK · PuraVida Tech

Agente de e-commerce de computadoras en Costa Rica con **Google ADK** + **LiteLLM** + **DeepSeek**.

## Levantar

```bash
cp .env.example .env   # poné tu DEEPSEEK_API_KEY
docker compose up --build
```

Abrí http://localhost:8000 y elegí `tienda_cr`.

## Qué demuestra (ver la charla)

| Concepto | Dónde |
|---|---|
| Tools = funciones | `tools.py` |
| Tool routing: el sistema tiene 6 tools, cada agente ve solo 2 | `agent.py` (sub-agentes) |
| Decider: consultas obvias se resuelven sin LLM | `decider.py` |
| Decidir ruta ≠ autorizar: el backend valida límites y pide confirmación | `cambiar_precio` en `tools.py` |

## Preguntas para la demo

1. **Ruta directa:** `¿Hay stock del SKU-042?` · `¿Cómo va el pedido #0182?`
2. **ADK con tools:** `¿Qué laptops gamer tienen?` · `¿Cuánto cuesta el envío a Guanacaste?`
3. **Razonamiento:** `¿Qué producto deberíamos reponer esta semana?`
4. **Validar acción:** `Bajá el precio de todos los productos un 40%` → luego `Bajá el SKU-001 a 350000` → `Sí, confirmo`
