import streamlit as st

# Streamlit 
st.set_page_config(page_title='¡Dibuja lo que quieras!', layout='wide')
st.title('¡Dibuja lo que quieras!')
st.subheader("Utiliza el tablero para hacer arte")

# Add canvas component
# Specify canvas parameters in application
drawing_mode = "freedraw"
stroke_width = st.slider('Selecciona el ancho de línea', 1, 30, 15)
stroke_color = '#FFFFFF' # Set background color to white
bg_color = '#000000'

# Add side bar
add_selectbox = st.sidebar.selectbox(
    "Propiedades del tablero",
    ("freedraw", "line", "circle")
)
