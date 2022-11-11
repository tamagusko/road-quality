# (c) Tiago Tamagusko 2022
"""Render markdown file on Streamlit.

Example:
    # Render README.md into app.
    render_markdown(README.md)
    Return:
        print README.md on Streamlit
"""
from __future__ import annotations

import markdown
import streamlit as st


def render_markdown(filename: str) -> None:
    """Render the content on markdown file.

    Args:
        filename: filename (plus path) to markdown file

    Returns:
        print markdown file on Streamlit
    """
    with open(filename, "r") as f:
        text = f.read()
    body = markdown.markdown(text)
    st.markdown(body, unsafe_allow_html=True)
