# (c) Tiago Tamagusko 2022
"""Create map with road quality data."""
from __future__ import annotations

import folium
import geopandas as gpd
import pandas as pd
from streamlit_folium import folium_static


def road_quality_map(data: str, center: list) -> None:
    """Create a map with road quality data.

    Args:
        data: csv file (plus path) with road quality data.
        center: Center (lat, lon) of the map.

    Returns:
        Map with road quality data.
    """
    # download geojson data
    df_world = gpd.read_file(gpd.datasets.get_path("naturalearth_lowres"))

    df = pd.read_csv(data, encoding="utf-8")

    # filter countries with data
    countries = list(df.name)
    gdf = df_world[df_world["name"].isin(countries)]

    # rename name column to country
    df = df.rename(columns={"name": "country"})
    gdf = gdf.rename(columns={"name": "country"})

    # countries with no data
    no_data = df_world[~df_world["name"].isin(countries)]

    # clean geo data
    gdf = gdf[["country", "continent", "geometry"]]
    # add road quality data to geo data
    gdf = pd.merge(gdf, df, how="right", on=["country"])
    # clean data
    gdf = gdf.dropna()

    # create map
    Map = folium.Map(location=center, tiles="CartoDB Positron", zoom_start=4)
    cp = folium.Choropleth(
        geo_data=gdf,
        name="choropleth",
        data=df,
        columns=["country", "quality_road"],
        key_on="feature.properties.country",
        fill_color="RdYlBu",
        fill_opacity=0.8,
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

    # add tooltip values
    folium.GeoJsonTooltip(["country", "quality_road"]).add_to(cp.geojson)

    folium.LayerControl().add_to(Map)
    folium_static(Map)
