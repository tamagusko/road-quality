# (c) Tiago Tamagusko 2022
"""Render markdown file on Streamlit.

Usage:
    render_markdown(filename.md)
    Return:
        print markdown file on Streamlit

Example:
    # Render README.md
    render_markdown(README.md)
    Return:
        print README.md on Streamlit
"""
from __future__ import annotations

import markdown
import streamlit as st


def render_markdown(filename: str) -> None:
    """Create something great.

    Args:
        param1: filename (plus path) to markdown file

    Returns:
        print markdown file on Streamlit
    """
    # render the content on markdown file
    with open(filename, "r") as f:
        text = f.read()
    body = markdown.markdown(text)
    st.markdown(body, unsafe_allow_html=True)
