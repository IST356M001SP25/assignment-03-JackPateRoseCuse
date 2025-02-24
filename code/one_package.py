'''
Write a streamlit to input one string of package data. 
It should use the `packaging.py` module to parse the string 
and output the package info as it appears. 
Calculate the total package size and display that.

see one_package.png for a screenshot
'''

import streamlit as st
from packaging import parse_packaging, calc_total_units, get_unit

st.title("Process One Package")

pkg = st.text_input("Enter package data:")

if pkg:
    parsed_pkg = parse_packaging(pkg)
    total = calc_total_units(parsed_pkg)
    unit = get_unit(parsed_pkg)
    st.text(parsed_pkg)
    for item in parsed_pkg:
        name = list(item.keys())[0]
        size = list(item.values())[0]
        st.info(f"{name} ➡️ {size}")
    st.success(f"Total 📦 Size: {total} {unit}")

