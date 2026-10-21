import os

from google.adk.agents import Agent
from google.adk.models.lite_llm import LiteLlm

from .decider import decider
from .tools import (
    buscar_productos,
    calcular_envio,
    cambiar_precio,
    consultar_stock,
    sugerir_reposicion,
    ver_pedido,
)

modelo = LiteLlm(model=os.getenv("MODELO", "deepseek/deepseek-chat"))

ESTILO = "Respondé en español de Costa Rica, breve y amable. Precios en colones (₡). Nunca inventés datos: usá tus herramientas."

agente_catalogo = Agent(
    name="agente_catalogo",
    model=modelo,
    description="Busca productos, precios y stock de computadoras y accesorios.",
    instruction=f"Sos el experto en catálogo de PuraVida Tech. {ESTILO}",
    tools=[buscar_productos, consultar_stock],
    before_agent_callback=decider,
)

agente_pedidos = Agent(
    name="agente_pedidos",
    model=modelo,
    description="Consulta el estado de pedidos y calcula costos de envío por provincia.",
    instruction=f"Atendés pedidos y envíos de PuraVida Tech. {ESTILO}",
    tools=[ver_pedido, calcular_envio],
    before_agent_callback=decider,
)

agente_admin = Agent(
    name="agente_admin",
    model=modelo,
    description="Tareas internas: sugerir reposición de inventario y cambiar precios.",
    instruction=(
        f"Ayudás al equipo interno de PuraVida Tech. {ESTILO} "
        "Para cambiar un precio: llamá cambiar_precio sin confirmar, mostrale al usuario lo que devuelve "
        "y solo si responde que sí, volvé a llamarla con confirmado=True. Nunca cambiés precios masivamente."
    ),
    tools=[sugerir_reposicion, cambiar_precio],
    before_agent_callback=decider,
)

root_agent = Agent(
    name="asistente_tienda",
    model=modelo,
    description="Asistente principal de PuraVida Tech, e-commerce de computadoras en Costa Rica.",
    instruction=(
        f"Sos el asistente de PuraVida Tech. {ESTILO} "
        "No tenés herramientas propias: derivá cada consulta al agente especialista que corresponda."
    ),
    sub_agents=[agente_catalogo, agente_pedidos, agente_admin],
    before_agent_callback=decider,
)
