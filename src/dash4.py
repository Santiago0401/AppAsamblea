import pandas as pd
import numpy as np
import plotly.graph_objects as go

def generate_visualizations():

    # Crear el diccionario de descripciones de temas para el hover text
    descripciones = {
        "Acciones y planes concretos": "Los participantes resaltan la importancia de que, tras la asamblea, se generen acciones y planes específicos y tangibles. No desean resultados generales o abstractos, sino propuestas concretas.",
        "Divulgación de resultados": "Se propone que tanto los resultados como el proceso de la asamblea sean ampliamente divulgados. Esto incluye informar sobre lo que se discutió, las decisiones tomadas y cómo se llegó a ellas.",
        "Definición de temas futuros": "Los participantes discuten la necesidad de establecer claramente los temas que se abordarán en futuras asambleas. Se sugiere que la elección y priorización se base en las necesidades de la comunidad.",
        "Seguimiento y evaluación": "Se enfatiza la importancia de crear mecanismos de seguimiento y control para las decisiones y acciones acordadas. Los participantes desean informes periódicos sobre el avance.",
        "Participación de autoridades": "Se plantea que para generar mayor confianza, es esencial que las autoridades y líderes gubernamentales se involucren activamente en el proceso.",
        "Comunicación comunitaria": "Se resalta la necesidad de socializar los resultados y procesos de la asamblea con toda la comunidad, incluyendo juntas de acción comunal y organizaciones locales."
    }

    # Crear datos simulados de transiciones entre temas
    data = {
        'tema_fragmento_actual': [
            "Acciones y planes concretos", "Acciones y planes concretos", "Divulgación de resultados",
            "Divulgación de resultados", "Definición de temas futuros", "Seguimiento y evaluación",
            "Participación de autoridades", "Comunicación comunitaria", "Comunicación comunitaria",
            "Seguimiento y evaluación", "Participación de autoridades", "Definición de temas futuros"
        ],
        'tema_fragmento_siguiente': [
            "Divulgación de resultados", "Seguimiento y evaluación", "Definición de temas futuros",
            "Comunicación comunitaria", "Participación de autoridades", "Participación de autoridades",
            "Comunicación comunitaria", "Seguimiento y evaluación", "Divulgación de resultados",
            "Definición de temas futuros", "Seguimiento y evaluación", "Comunicación comunitaria"
        ],
        'duracion': [5, 4, 6, 8, 4, 5, 5, 6, 4, 5, 7, 5]
    }

    df = pd.DataFrame(data)

    # Calcular el tiempo total hablado por tema
    tiempo_por_tema = {}
    for tema in np.unique(df.tema_fragmento_actual):
        tiempo_tema = df[df.tema_fragmento_actual == tema]['duracion'].sum()
        tiempo_por_tema[tema] = tiempo_tema

    # Obtener valores únicos para los nodos
    valores_unicos = np.unique(np.concatenate([df.tema_fragmento_actual, df.tema_fragmento_siguiente]))
    node_indices = {node: idx for idx, node in enumerate(valores_unicos)}

    # Crear etiquetas con el tiempo total
    labels = [f"{tema}\n({tiempo_por_tema.get(tema, 0)} min)" for tema in valores_unicos]

    # Crear índices para source y target
    indices_source = [node_indices[tema] for tema in df.tema_fragmento_actual]
    indices_target = [node_indices[tema] for tema in df.tema_fragmento_siguiente]

    # Definir posiciones x,y para una disposición más circular manualmente
    x_positions = [0.1, 0.3, 0.35, 0.5, 0.75, 0.9]
    y_positions = [0.5, 0.8, 0.2, 0.5, 0.8, 0.2]

    # Crear el diagrama Sankey
    fig = go.Figure(data=[go.Sankey(
        arrangement='snap',
        node = dict(
            pad = 20,
            thickness = 30,
            line = dict(color = "black", width = 0.5),
            label = labels,  # Usando las nuevas etiquetas con tiempo
            color = ["#1f77b4", "#ff7f0e", "#2ca02c", "#d62728", "#9467bd", "#8c564b"],
            x = x_positions,
            y = y_positions,
            customdata = [descripciones[tema] for tema in valores_unicos],
            hovertemplate = "Tema: %{label}<br>Descripción: %{customdata}<extra></extra>"
        ),
        link = dict(
            source = indices_source,
            target = indices_target,
            value = df.duracion,
            hovertemplate = "De: %{source.label}<br>A: %{target.label}<extra></extra>"  # Removido el tiempo de las aristas
        )
    )])

    # Actualizar el diseño
    fig.update_layout(
        title_text="Flujo de Temas en el Debate",
        font_size=12,
        height=800,
        width=1300,
        hoverlabel=dict(
            bgcolor="white",
            font_size=15,
            font_family="Arial"
        )
    )

    # Crear el diccionario de descripciones de temas para el hover text
    descripciones = {
        "Metáfora de la casa": "Se emplea la imagen de una casa con diferentes espacios (sala, comedor, estudio, sala de estar) para simbolizar las distintas etapas y formas de participación ciudadana. Cada espacio representa un momento específico del proceso participativo.",
        "Identificación de actores": "Se identifican los actores que podrían ser invitados a participar, clasificándolos en actores públicos (alcaldías locales, secretarías distritales, entes de control, etc.) y actores privados (ciudadanía, juntas de acción comunal, academia, medios de comunicación).",
        "Asignación de funciones": "Se definen las funciones específicas de cada espacio: sala para consultas, comedor para concertación, estudio para seguimiento y sala de estar para rendición de cuentas.",
        "Criterios de reuniones": "Se establecen indicaciones sobre cómo deben llevarse a cabo las reuniones en cada espacio, considerando aspectos como frecuencia, duración, uso de lenguaje claro y horarios flexibles.",
        "Secuencia participación": "Se discute sobre cuál debe ser el orden de involucramiento de los actores, con énfasis en comenzar con la comunidad y las juntas de acción comunal.",
        "Resultados esperados": "Se determinan los resultados mínimos que se esperan de cada reunión, como lograr consensos, acuerdos claros y satisfacción de lo hablado.",
        "Construcción consensos": "A través de la deliberación y participación activa, se trabaja para llegar a acuerdos sobre la organización y objetivos del proceso participativo."
    }

    # Crear datos simulados de transiciones entre temas
    data = {
        'tema_fragmento_actual': [
            "Metáfora de la casa", "Metáfora de la casa", "Identificación de actores",
            "Identificación de actores", "Asignación de funciones", "Asignación de funciones",
            "Criterios de reuniones", "Secuencia participación", "Resultados esperados",
            "Construcción consensos", "Secuencia participación", "Resultados esperados",
            "Criterios de reuniones", "Construcción consensos"
        ],
        'tema_fragmento_siguiente': [
            "Identificación de actores", "Asignación de funciones", "Asignación de funciones",
            "Secuencia participación", "Criterios de reuniones", "Resultados esperados",
            "Secuencia participación", "Resultados esperados", "Construcción consensos",
            "Criterios de reuniones", "Construcción consensos", "Secuencia participación",
            "Construcción consensos", "Resultados esperados"
        ],
        'duracion': [15, 12, 10, 8, 13, 9, 11, 14, 10, 12, 8, 7, 9, 11]
    }

    df = pd.DataFrame(data)

    # Calcular el tiempo total hablado por tema
    tiempo_por_tema = {}
    for tema in np.unique(df.tema_fragmento_actual):
        tiempo_tema = df[df.tema_fragmento_actual == tema]['duracion'].sum()
        tiempo_por_tema[tema] = tiempo_tema

    # Obtener valores únicos para los nodos
    valores_unicos = np.unique(np.concatenate([df.tema_fragmento_actual, df.tema_fragmento_siguiente]))
    node_indices = {node: idx for idx, node in enumerate(valores_unicos)}

    # Crear etiquetas con el tiempo total
    labels = [f"{tema}\n({tiempo_por_tema.get(tema, 0)} min)" for tema in valores_unicos]

    # Crear índices para source y target
    indices_source = [node_indices[tema] for tema in df.tema_fragmento_actual]
    indices_target = [node_indices[tema] for tema in df.tema_fragmento_siguiente]

    # Definir posiciones x,y para una disposición que refleje el flujo del proceso
    x_positions = [0.45, 0.1, 0.5, 0.7, 0.9, 0.2, 0.7]
    y_positions = [0.3, 0.3, 0.65, 0.3, 0.5, 0.7, 0.7]

    # Crear el diagrama Sankey
    fig2 = go.Figure(data=[go.Sankey(
        arrangement='snap',
        node = dict(
            pad = 20,
            thickness = 30,
            line = dict(color = "black", width = 0.5),
            label = labels,
            color = ["#e377c2", "#1f77b4", "#ff7f0e", "#2ca02c", "#d62728", "#9467bd", "#8c564b"],
            x = x_positions,
            y = y_positions,
            customdata = [descripciones[tema] for tema in valores_unicos],
            hovertemplate = "Tema: %{label}<br>Descripción: %{customdata}<extra></extra>"
        ),
        link = dict(
            source = indices_source,
            target = indices_target,
            value = df.duracion,
            hovertemplate = "De: %{source.label}<br>A: %{target.label}<extra></extra>"
        )
    )])

    # Actualizar el diseño
    fig2.update_layout(
        title_text="Flujo de Temas en el Debate - Metáfora de la Casa y Proceso Participativo",
        font_size=12,
        height=800,
        width=1300,
        hoverlabel=dict(
            bgcolor="white",
            font_size=12,
            font_family="Arial"
        )
    )

    return fig, fig2
