# /// script
# requires-python = ">=3.14"
# dependencies = [
#     "marimo>=0.23.2",
#     "osmnx>=2.1.0",
# ]
# ///

import marimo

__generated_with = "0.23.1"
app = marimo.App(width="medium", app_title="Demo")


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Demo
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    It's my first time using marimo. I want to create interactive elements first, as I need to know if this would suit my web app needs just fine.
    """)
    return


@app.cell
def _():
    import marimo as mo
    import osmnx as ox

    return mo, ox


@app.cell
def _(mo):
    place = mo.ui.text(placeholder="Search for a city")
    place
    return (place,)


@app.cell
def _(ox, place):
    G = ox.graph.graph_from_place(place.value, network_type="drive")
    G
    return (G,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Could this be?
    """)
    return


@app.cell
def _(G, ox):
    fig, ax = ox.plot.plot_figure_ground(G, color="blue")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    This is more akin to what I want:
    """)
    return


@app.cell
def _(G, ox):
    ox.plot.plot_graph(G, node_size=0, show=False, edge_color="white")

    return


if __name__ == "__main__":
    app.run()
