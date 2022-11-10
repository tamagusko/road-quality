# (c) Tiago Tamagusko 2022
from __future__ import annotations

import folium
import pandas as pd
import geopandas as gpd

from streamlit_folium import folium_static


def road_quality_map(data: str, center: list) -> None:
    # download geojson data
    df_world = gpd.read_file(gpd.datasets.get_path("naturalearth_lowres"))

    df = pd.read_csv(data, encoding="utf-8")

    # filter countries with data
    countries = list(df.name)
    gdf = df_world[df_world["name"].isin(countries)]

    # countries with no data
    no_data = df_world[~df_world["name"].isin(countries)]

    # clean geo data
    gdf = gdf[["name", "continent", "geometry"]]

    # create map
    Map = folium.Map(location=center, tiles="CartoDB Positron", zoom_start=4)
    folium.Choropleth(
        geo_data=gdf,
        name="choropleth",
        data=df,
        columns=["name", "quality_road"],
        key_on="feature.properties.name",
        fill_color="RdYlBu",
        fill_opacity=0.7,
        line_opacity=0.2,
        legend_name="Quality of road infrastructure (1 = extremely poor; 7 = extremely good)",
    ).add_to(Map)

    # fill countries with no data (gray)
    folium.GeoJson(
        data=no_data,
        style_function=lambda feature: {
            "fillColor": "gray",
            "fillOpacity": 0.5,
            "color": "gray",
            "weight": 1,
        },
    ).add_to(Map)

    folium.LayerControl().add_to(Map)
    folium_static(Map)
