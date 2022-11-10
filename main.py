# (c) Tiago Tamagusko 2022
from __future__ import annotations

import streamlit as st

from streamlit_option_menu import option_menu
from utils.render_markdown import render_markdown
from utils.coordinates import get_coordinates
from createMap import road_quality_map

# page config
st.set_page_config(
    page_title="Road Quality",
    page_icon=":earth_americas:",
    layout="wide",
    initial_sidebar_state="auto",  # use collapsed to hide sidebar
    menu_items={
        'Get Help': 'mailto:tamagusko@gmail.com',
        'Report a bug': "https://github.com/tamagusko/road-quality/issues",
        'About': "Copyright 2022 [Tiago Tamagusko](https://github.com/tamagusko)"
    }
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
    center_input = st.sidebar.text_input('Search:', 'Europe')
    center = get_coordinates(center_input)
    st.sidebar.caption("World data available. Type a country or continent.")
    # two columns page
    left, right = st.columns(2)
    with left:
        data = "data/world-road-quality.csv"
        road_quality_map(data, center)
        st.caption("Note: Gray countries have no data available.")

    with right:
        render_markdown("home.md")

elif page == "Analysis":
    render_markdown("analysis.md")

elif page == "Data statement":
    render_markdown("data.md")

elif page == "About":
    render_markdown("README.md")

st.caption("© 2022 [Tiago Tamagusko](https://github.com/tamagusko)")
