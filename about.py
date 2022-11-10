# (c) Tiago Tamagusko 2022
from __future__ import annotations

import markdown
import streamlit as st


def about():
    # content on README.md file
    with open('README.md', 'r') as f:
        text = f.read()
    body = markdown.markdown(text)
    st.markdown(body, unsafe_allow_html=True)
