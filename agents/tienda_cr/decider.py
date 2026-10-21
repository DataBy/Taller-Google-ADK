import re

from google.adk.agents.callback_context import CallbackContext
from google.genai import types

from .tools import consultar_stock, ver_pedido

# Reglas simples: si la consulta es obvia y trae parámetros claros, se resuelve sin LLM.
REGLAS = [
    (re.compile(r"\b(stock|quedan|hay|disponible)\b.*\b(SKU-\d{3})\b", re.I), consultar_stock),
    (re.compile(r"\bpedido\s*#?(\d{4})\b", re.I), ver_pedido),
]


def decider(callback_context: CallbackContext) -> types.Content | None:
    contenido = callback_context.user_content
    if not contenido or not contenido.parts or not contenido.parts[0].text:
        return None
    texto = contenido.parts[0].text

    for patron, tool in REGLAS:
        match = patron.search(texto)
        if match:
            resultado = tool(match.groups()[-1])
            if "error" in resultado:
                return None
            return types.Content(
                role="model",
                parts=[types.Part(text=f"⚡ Ruta directa (Decider, sin LLM) → {tool.__name__}('{match.groups()[-1]}')\n\n{_formatear(resultado)}")],
            )
    return None  # Caso complejo: lo resuelve el agente de ADK.


def _formatear(resultado: dict) -> str:
    return "\n".join(f"- **{k}**: {v}" for k, v in resultado.items())
