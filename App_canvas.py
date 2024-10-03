import streamlit as st
from streamlit_drawable_canvas import st_canvas

# Streamlit 
st.set_page_config(page_title='¡Dibuja lo que quieras!', layout='wide')
st.title('¡Dibuja lo que quieras!')
st.subheader("Utiliza el tablero para hacer arte")

# Add canvas component
# Specify canvas parameters in application
drawing_mode = "freedraw"
stroke_color = '#FFFFFF' # Set background color to white
bg_color = '#000000'

# Add side bar
with st.sidebar
    stroke_width = st.slider('Selecciona el ancho de línea', 1, 30, 15)
   
# Create a canvas component
canvas_result = st_canvas(
    fill_color="rgba(255, 165, 0, 0.3)",  # Fixed fill color with some opacity
    stroke_width=stroke_width,
    stroke_color=stroke_color,
    background_color=bg_color,
    height=500,
    width=500,
    key="canvas",
)


   
