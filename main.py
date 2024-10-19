import streamlit as st

name = "Todo App By Abu Bakar"
header = "Todo App Using Abu Bakar Software Wala"
button  = "Add Task"

st.title(name)
st.text(header)
input12 = st.text_input("Add Your Task : ")
btn  = st.button(button)

st.write(input12)
