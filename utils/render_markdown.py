# (c) Tiago Tamagusko 2022
from __future__ import annotations

import markdown
import streamlit as st


def render_markdown(filename: str) -> None:
    # render the content on markdown file
    with open(filename, 'r') as f:
        text = f.read()
    body = markdown.markdown(text)
    st.markdown(body, unsafe_allow_html=True)
