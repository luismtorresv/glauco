import marimo

__generated_with = "0.23.1"
app = marimo.App(app_title="Leafmap Playground")


@app.cell
def _():
    import marimo as mo
    import leafmap

    return (leafmap,)


@app.cell
def _(leafmap):
    m = leafmap.Map(
        center=[6.200161, -75.578748],
        zoom=17,
    )
    return (m,)


@app.cell
def _(m):
    m.add_basemap("Esri.NatGeoWorldMap")
    m.add_basemap("HYBRID")
    return


@app.cell
def _(m):
    m.add_tile_layer(
        url="https://mt1.google.com/vt/lyrs=y&x={x}&y={y}&z={z}",
        name="Google Satellite",
        attribution="Googol",
    )
    return


@app.cell
def _(leafmap):
    med_url = "https://www.medellin.gov.co/servidormapas/services/ServiciosImagen/Ortofoto_Medellin_2024/ImageServer/WMSServer"
    _m = leafmap.Map(
        center=[6.200161, -75.578748],
        zoom=17,
    )
    _m.add_wms_layer(
        url=med_url,
        layers="Ortofoto_Medellin_2024",
        name="Ortofoto Medellín 2024",
        format="image/png",
        shown=True,
    )
    _m
    return


@app.cell
def _(m):
    m
    return


if __name__ == "__main__":
    app.run()
