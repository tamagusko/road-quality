# (c) Tiago Tamagusko 2022
from __future__ import annotations

import streamlit as st
from streamlit_option_menu import option_menu

from createMap import road_quality_map
from utils.coordinates import get_coordinates
from utils.render_markdown import render_markdown

# page config
st.set_page_config(
    page_title="Road Quality",
    page_icon=":earth_americas:",
    layout="wide",
    initial_sidebar_state="auto",  # use collapsed to hide sidebar
    menu_items={
        "Get Help": "mailto:tamagusko@gmail.com",
        "Report a bug": "https://github.com/tamagusko/road-quality/issues",
        "About": "Copyright 2022 [Tiago Tamagusko](https://github.com/tamagusko)",
    },
)

# sidebar
with st.sidebar:
    page = option_menu(
        None,
        ["Home", "Analysis", "Data statement", "About"],
        icons=["house", "justify", "clipboard-data", "file-person"],
        menu_icon="cast",
        default_index=0,
    )

# pages
if page == "Home":
    # sidebar
    center_input = st.sidebar.text_input("Search:", "Europe")
    center = get_coordinates(center_input)
    st.sidebar.caption("Worldwide data available. Type a country or continent.")
    # body
    st.title("World Road Quality")
    data = "data/world-road-quality.csv"
    road_quality_map(data, center)
    st.caption("Note: Gray countries have no data available.")

    render_markdown("pages/home.md")

elif page == "Analysis":
    render_markdown("pages/analysis.md")

elif page == "Data statement":
    render_markdown("data/README.md")

elif page == "About":
    render_markdown("pages/about.md")

st.caption("© 2022 [Tiago Tamagusko](https://github.com/tamagusko)")
