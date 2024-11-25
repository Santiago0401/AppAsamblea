import plotly.graph_objects as go
import pandas as pd

def generate_visualizations(data, data_pos):

    # Lista de preguntas
    preguntas = ["AutoEval1", "AutoEval2", "AutoEval3", "AutoEval4", "AutoEval5", "AutoEval6", "AutoEval7"]

    figs = []

    names = data[:1]
    data = data[1:]
    names_pos = data_pos[:1]
    data_pos = data_pos[1:]

    # Crear gráficos separados
    for idx, pregunta in enumerate(preguntas):
        fig = go.Figure()

        # Contar las respuestas para cada valor (1 a 10)
        counts = data[pregunta].value_counts().sort_index()
        counts_pos = data_pos[pregunta].value_counts().sort_index()

        # Calcular la proporción para cada valor (1-10)
        proportions = counts / counts.sum()  # Proporción por cada valor
        proportions_pos = counts_pos / counts_pos.sum()  # Proporción por cada valor

        # Añadir las barras apiladas con un hue para cada valor de respuesta
        for i, value in enumerate(range(1, 11)):
            # Si no hay datos para un valor, lo completamos con 0
            proportion = proportions.get(value, 0)

            #print(pregunta+"\n")
            #print(pregunta+"pre")

            fig.add_trace(
                go.Bar(
                    x=["Pre"],  # Colocar la pregunta en el eje X
                    y=[proportion],  # Proporción en el eje Y
                    name=f"Valor {value}",  # Nombre para cada valor
                    marker=dict(
                        color=f"rgba({(i * 30) % 255}, {(i * 60) % 255}, {(i * 90) % 255}, 0.6)",  # Colores diferenciados
                        line=dict(color="black", width=1)  # Contorno negro para cada sección
                    ),
                    hovertemplate=f"Valor: {value}<br>Proporción: %{proportion*100:.1f}<extra></extra>",
                )
            )

        for i, value in enumerate(range(1, 11)):

            # Si no hay datos para un valor, lo completamos con 0
            proportion = proportions_pos.get(value, 0)

            fig.add_trace(
                go.Bar(
                    x=["Pos"],  # Colocar la pregunta en el eje X
                    y=[proportion],  # Proporción en el eje Y
                    name=f"Valor {value}",  # Nombre para cada valor
                    marker=dict(
                        color=f"rgba({(i * 30) % 255}, {(i * 60) % 255}, {(i * 90) % 255}, 0.6)",  # Colores diferenciados
                        line=dict(color="black", width=1)  # Contorno negro para cada sección
                    ),
                    hovertemplate=f"Valor: {value}<br>Proporción: %{proportion*100:.1f}<extra></extra>",
                )
            )

        # Ajustar el diseño del gráfico
        fig.update_layout(
            barmode='stack',  # Apilar las barras para cada valor
            title=dict(
            text=f"{[names[i][0] for i in names][2:10][idx]}",
            font=dict(
                family="Roboto, sans-serif",  # Tipo de letra Roboto
                size=20,  # Tamaño del texto
                color="black"  # Color del texto
            ),  # Ajustar el tamaño del título
            x=0.5,  # Centrar el título
            y=0.95  # Ajustar la posición vertical del título
            ),
            xaxis_title="",
            yaxis_title="Proporción de Respuestas",
            xaxis=dict(tickmode="array", tickvals=["Pre","Pos"]),
            height=600,
            width=1100,
            showlegend=False
        )

        figs.append(fig)

    # Mostrar el gráfico
    return figs
