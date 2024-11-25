import plotly.graph_objects as go

def generate_visualizations(data_tree):

    data_final_sin_duplicados = data_tree.drop_duplicates(subset=["IMPRESIONES/COMENTARIOS", "CATEGORIA"], keep="first")

    # Datos simulados basados en tu descripción
    lbs = [i for i in data_final_sin_duplicados["CATEGORIA"].unique()]
    pnt = [""] * len(set(data_final_sin_duplicados["CATEGORIA"]))
    cols = ["lightgrey"] * len(set(data_final_sin_duplicados["CATEGORIA"]))

    for i in data_final_sin_duplicados.values:
        lbs.append(i[5])  # Etiqueta del nodo
        pnt.append(i[0])  # Nodo padre

        # Colores
        if i[3] == "ROJO":
            cols.append("red")
        elif i[3] == "AMARILLO":
            cols.append("yellow")
        elif i[3] == "AZUL":
            cols.append("royalblue")
        elif i[3] == "VERDE":
            cols.append("green")

    # Agrupar etiquetas con el mismo color
    # Combina los datos y ordénalos por color para agrupar visualmente
    tree_data = sorted(zip(lbs, pnt, cols), key=lambda x: x[2])  # Ordenar por color
    lbs, pnt, cols = zip(*tree_data)  # Descomprimir listas ordenadas

    # Crear el gráfico de treemap
    fig = go.Figure(go.Treemap(
        labels=lbs,
        parents=pnt,
        marker_colors=cols,
        root_color="white",
        texttemplate="%{label}",  # Asegúrate de que se muestre la etiqueta
        textfont=dict(
            family="Roboto, sans-serif",  # Fuente Roboto
            size=17,         # Tamaño de letra
            color="black"    # Color del texto
        )
    ))

    # Márgenes ajustados
    fig.update_layout(margin=dict(t=50, l=25, r=25, b=25))

    return fig
