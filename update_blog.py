"""
JC Consultoría Estratégica — Agente de Contenido Automático
Genera un nuevo artículo de blog cada 7 días usando la API de Claude
y lo inserta automáticamente en blog.html
"""

import anthropic
import datetime
import random
import re

# ── Temas rotativos sobre negocios dominicanos ──────────────────────────────
TEMAS = [
    "Cambios recientes en la normativa fiscal de la DGII y cómo afectan a las PYMES",
    "Estrategias de planificación fiscal para empresas dominicanas en 2026",
    "Cómo optimizar el flujo de caja de tu empresa usando análisis de datos",
    "Obligaciones TSS del empleador: errores más comunes y cómo evitarlos",
    "Factura electrónica e-CF: guía práctica para implementarla en tu negocio",
    "KPIs financieros esenciales para empresarios dominicanos",
    "Cómo reducir legalmente tu carga tributaria de ITBIS",
    "Cierre fiscal anual: checklist completo para empresas en RD",
    "Auditoría interna: por qué tu empresa necesita una antes de la DGII",
    "Beneficios laborales obligatorios en República Dominicana 2026",
    "Dashboard financiero: cómo visualizar la rentabilidad de tu negocio",
    "SRL vs empresa individual: cuál conviene más para tu negocio en RD",
    "Anticipos del impuesto sobre la renta: cálculo y estrategias",
    "Retenciones fiscales en RD: guía completa para empleadores",
    "Cómo interpretar tu estado de flujo de caja y tomar mejores decisiones",
]

# ── Categorías por tema ──────────────────────────────────────────────────────
CATEGORIAS = {
    0: "dgii", 1: "fiscal", 2: "data", 3: "tss", 4: "dgii",
    5: "data", 6: "fiscal", 7: "contabilidad", 8: "contabilidad",
    9: "nomina", 10: "data", 11: "emprendedor", 12: "fiscal",
    13: "fiscal", 14: "data",
}

EMOJIS = {
    "fiscal": "⚡", "contabilidad": "📋", "data": "📊",
    "nomina": "👥", "emprendedor": "🚀", "dgii": "📢", "tss": "👔",
}

CATEGORIAS_LABELS = {
    "fiscal": "Fiscal / Impuestos", "contabilidad": "Contabilidad",
    "data": "Data & Análisis", "nomina": "Nómina & RRHH",
    "emprendedor": "Emprendedores", "dgii": "Aviso DGII", "tss": "TSS",
}


def generar_articulo(tema: str) -> dict:
    """Genera un artículo de blog completo usando Claude."""
    client = anthropic.Anthropic()

    prompt = f"""Eres Jonathan Constanza, CPA y Data Analyst dominicano con más de 10 años de experiencia 
en consultoría estratégica, fiscalidad dominicana (DGII, ITBIS, IR-17, TSS) y análisis de datos financieros.
Tu estilo es profesional, directo y con autoridad técnica. Firmas como "Jonathan Constanza | CPA & Consultor Estratégico".

Genera un artículo de blog completo y original sobre: "{tema}"

El artículo debe seguir EXACTAMENTE este formato:

TÍTULO: [título atractivo aquí]
RESUMEN: [resumen de 1-2 oraciones aquí]
CONTENIDO:
[contenido completo aquí con subtítulos marcados con ##]

Requisitos del artículo:
- Título impactante orientado al empresario dominicano
- Resumen conciso de 1-2 oraciones
- 3-4 secciones con subtítulos ## claros
- Al menos un dato o cifra específica y relevante
- Mencionar regulaciones dominicanas cuando aplique (DGII, TSS, Código Tributario, Ley 11-92)
- Cierre con llamada a la acción: contactar a Jonathan vía WhatsApp 809-931-4911
- Tono: experto pero accesible, sin jerga innecesaria
- Extensión total: 400-500 palabras"""

    message = client.messages.create(
        model="claude-sonnet-4-20250514",
        max_tokens=1500,
        messages=[{"role": "user", "content": prompt}]
    )

    texto = message.content[0].text

    # Extraer título
    titulo_match = re.search(r'TÍTULO:\s*(.+)', texto)
    titulo = titulo_match.group(1).strip() if titulo_match else tema

    # Extraer resumen
    resumen_match = re.search(r'RESUMEN:\s*(.+?)(?=CONTENIDO:|$)', texto, re.DOTALL)
    resumen = resumen_match.group(1).strip() if resumen_match else ""

    # Limpiar resumen (máximo 180 caracteres para el card)
    resumen_corto = resumen[:180] + "..." if len(resumen) > 180 else resumen

    return {
        "titulo": titulo,
        "resumen": resumen_corto,
        "contenido": texto,
    }


def crear_card_html(titulo: str, resumen: str, categoria: str, fecha: str, minutos: int) -> str:
    """Genera el HTML de una tarjeta de artículo para el blog."""
    emoji = EMOJIS.get(categoria, "📰")
    cat_label = CATEGORIAS_LABELS.get(categoria, categoria.title())

    return f"""
    <article class="articulo-card reveal" data-cat="{categoria}" data-title="{titulo.lower()}">
      <span class="card-emoji">{emoji}</span>
      <span class="card-categoria">{cat_label}</span>
      <h3 class="card-title">{titulo}</h3>
      <p class="card-excerpt">{resumen}</p>
      <div class="card-footer">
        <span class="card-fecha">{fecha}</span>
        <span class="card-min">{minutos} min</span>
      </div>
    </article>"""


def actualizar_blog(blog_path: str = "blog.html"):
    """Función principal: genera artículo y lo inserta en blog.html."""

    # Seleccionar tema de forma rotativa según semana del año
    semana_actual = datetime.date.today().isocalendar()[1]
    tema_idx = semana_actual % len(TEMAS)
    tema = TEMAS[tema_idx]
    categoria = CATEGORIAS.get(tema_idx, "fiscal")

    print(f"🤖 Generando artículo sobre: {tema}")

    # Generar artículo
    articulo = generar_articulo(tema)

    print(f"✅ Artículo generado: {articulo['titulo']}")

    # Fecha y tiempo de lectura
    fecha = datetime.date.today().strftime("%-d %b %Y")
    minutos = random.randint(6, 12)

    # Crear HTML del nuevo card
    nuevo_card = crear_card_html(
        titulo=articulo["titulo"],
        resumen=articulo["resumen"],
        categoria=categoria,
        fecha=fecha,
        minutos=minutos,
    )

    # Leer blog.html actual
    with open(blog_path, "r", encoding="utf-8") as f:
        contenido = f.read()

    # Insertar nuevo artículo ANTES del marcador de cierre del grid
    marcador = '<div class="no-results"'
    if marcador in contenido:
        contenido = contenido.replace(marcador, nuevo_card + "\n\n    " + marcador)
        print("✅ Artículo insertado en el grid del blog")
    else:
        print("⚠️  No se encontró el marcador de inserción en blog.html")
        return False

    # Guardar blog.html actualizado
    with open(blog_path, "w", encoding="utf-8") as f:
        f.write(contenido)

    print(f"🚀 Blog actualizado exitosamente — {fecha}")
    return True


if __name__ == "__main__":
    actualizar_blog()
