# /// script
# requires-python = ">=3.14"
# dependencies = [
#     "marimo>=0.23.2",
#     "osmnx>=2.1.0",
# ]
# ///

import marimo

__generated_with = "0.23.1"
app = marimo.App(width="full", app_title="Glauco")

with app.setup:
    import geopandas as gp
    import marimo as mo
    import osmnx as ox
    import networkx as nx


@app.cell(hide_code=True)
def _():
    mo.md(rf"""
    # Glauco 🧜

    Complementary web app to the bachelor thesis of Riascos-Goyes, Juan Fernando, et al. 2025. ‘Decoding Street Network Morphologies and Their Correlation to Travel Mode Choice’ https://doi.org/10.48550/arXiv.2507.19648.

    This project was submitted in fulfilment of the special project of my internship semester.
    """)
    return


@app.cell(hide_code=True)
def _():
    mo.md(r"""
    ## Input

    You may upload a GeoJSON file of the desired street network or type in your query in the search box to automatically retrieve it.
    """)
    return


@app.cell
def _():
    place_query = mo.ui.text_area(
        placeholder='e.g. "El Poblado, Medellín" or "Carmen de Viboral, Antioquia"',
        full_width=True,
    )

    geojson_file = mo.ui.file(
        kind="area",
        multiple=True,
        filetypes=[".shp", ".shx", ".prj", ".dbf", ".cpg"],
    )
    return geojson_file, place_query


@app.cell
def _(geojson_file, place_query):
    mo.hstack(
        [
            mo.vstack(
                [mo.md("Search with Nominatim"), place_query],
                align="center",
            ),
            mo.vstack(
                [mo.md("Upload your own file"), geojson_file],
                align="center",
            ),
        ],
        align="start",
        gap=1,
    )
    return


@app.cell
def _():
    _place_graph = ox.graph.graph_from_bbox(
        [-75.61192, 6.2241, -75.58624, 6.24517],  # this is close to my house
        network_type="drive",  # also, how do i only allow shapefiles of street networks?
    )
    _place_gdfs = ox.convert.graph_to_gdfs(_place_graph, nodes=False)
    edge_centrality = nx.closeness_centrality(_place_graph)

    ev = [edge_centrality[edge + (0,)] for edge in _place_graph.edges()]

    import matplotlib.colors as colors
    import matplotlib.cm as cm
    norm = colors.Normalize(vmin=min(ev)*0.8, vmax=max(ev))
    cmap = cm.ScalarMappable(norm=norm, cmap=cm.inferno)
    ec = [cmap.to_rgba(cl) for cl in ev]

    _map = _place_gdfs.explore(cmap=ec, tiles="cartodbdarkmatter")
    _map
    return


@app.cell
def _(geojson_file, place_query):
    place_gdfs = None

    if place_query.value and geojson_file.value:
        exit()

    if place_query.value:
        place_graph = ox.graph.graph_from_place(
            place_query.value,
            network_type="drive",
        )
        place_gdfs = ox.convert.graph_to_gdfs(
            place_graph,
            nodes=False,
        )
        nx.betweenness_centrality(place_graph)
    elif geojson_file.value:
        for file in geojson_file.value:
            with open(file.name, "wb") as f:
                f.write(file.contents)
        name = geojson_file.value[0].name.rpartition(".")[0] + ".shp"
        place_gdfs = gp.read_file(name)

    if place_query.value or geojson_file.value:
        map = place_gdfs.explore(
            cmap="plasma",
            tiles="cartodbdarkmatter",
        )
    return (map,)


@app.cell(hide_code=True)
def _():
    mo.md(r"""
    ## Results
    """)
    return


@app.cell
def _(map):
    map
    return


if __name__ == "__main__":
    app.run()
