# (c) Tiago Tamagusko 2022
from __future__ import annotations

import streamlit as st

from about import about
from fatalities import fatalities
from quality import quality

# page config
st.set_page_config(
    page_title='Road Vizualization', page_icon=':earth_americas:',
    layout='wide', initial_sidebar_state='auto', menu_items=None,
)
page = 'Road Quality'  # Home

# basemap selection
basemap = st.sidebar.selectbox(
    'Base map:', (
        'CartoDB positron',
        'OpenStreetMap',
        'Stamen Terrain',
        'Stamen Toner',
        'CartoDB dark_matter',
    ),
)

# add horizontal line
with st.sidebar:
    st.write('---')

page = st.sidebar.selectbox(
    'Page:', ('Road Quality', 'Traffic Fatalities (Europe)', 'About'),
)

# pages
if page == 'Road Quality':
    quality(basemap)

elif page == 'Traffic Fatalities (Europe)':
    fatalities(basemap)

elif page == 'About':
    about()
