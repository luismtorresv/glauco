import marimo

__generated_with = "0.23.1"
app = marimo.App(app_title="Yet another marimo playground")

with app.setup:
    import geopandas as gp
    import marimo as mo
    import osmnx as ox
    import networkx as nx


@app.cell
def _():
    place_graph = ox.graph.graph_from_place(
        query="El Poblado, Medellín, Antioquia",
        network_type="drive",  # also, how do i only allow shapefiles of street networks?
    )
    return (place_graph,)


@app.cell
def _(place_graph):
    place_graph.graph
    return


@app.cell
def _(place_graph):
    place_graph.edges
    return


@app.cell
def _(place_graph):
    place_graph.number_of_edges()
    return


@app.cell
def _(place_graph):
    edge_centrality = nx.betweenness_centrality(nx.line_graph(place_graph))
    edge_centrality
    return (edge_centrality,)


@app.cell
def _(edge_centrality, place_graph):
    ev = [edge_centrality[edge + (0,)] for edge in place_graph.edges()]
    ev
    return (ev,)


@app.cell
def _(place_graph):
    place_gdfs = ox.convert.graph_to_gdfs(place_graph, edges=True, nodes=False)
    place_gdfs
    return (place_gdfs,)


@app.cell
def _(ev, place_gdfs):
    place_gdfs_new = place_gdfs.assign(key=ev)
    return (place_gdfs_new,)


@app.cell
def _(place_gdfs_new):
    map = place_gdfs_new.explore(column="key", tiles="cartodbdarkmatter")
    map
    return


if __name__ == "__main__":
    app.run()
