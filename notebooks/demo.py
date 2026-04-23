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
    import asyncio

    import marimo as mo
    import osmnx as ox


@app.cell(hide_code=True)
def _():
    mo.md(r"""
    # Glauco 🧜

    Complementary web app to:

    Riascos-Goyes, Juan Fernando, et al. 2025. ‘Decoding Street Network Morphologies and Their Correlation to Travel Mode Choice’ https://doi.org/10.48550/arXiv.2507.19648.

    This project was submitted in fulfilment of the special project of my internship semester.
    """)
    return


@app.cell
def _():
    place = mo.ui.text(
        placeholder='e.g. "El Poblado, Medellín" or "Carmen de Viboral, Antioquia"',
        full_width=True,
    )
    return (place,)


@app.cell
def _(place):
    if place.value:
        place_graph = ox.graph.graph_from_place(
            place.value,
            network_type="drive",
        )

        place_gdfs = ox.convert.graph_to_gdfs(
            place_graph,
            nodes=False,
        )

        map = place_gdfs.explore(
            column="length",
            cmap="plasma",
            tiles="cartodbdarkmatter",
        )
    return (map,)


@app.cell(hide_code=True)
def _(place):
    mo.md(rf"""
    Search for a city or neighbourhood to see its street network.

    {place}
    """)
    return


@app.cell
def _(map):
    map
    return


if __name__ == "__main__":
    app.run()
