#------------------------------------------------
# Librerias a utilizar
import pandas as pd 
import streamlit as st
from pandas import read_excel
from PIL import Image
import altair as alt
#------------------------------------------------
# Configuración de página
#st.set_page_config(
#    page_title="Resultados- RBI streamly Cool App",
#    page_icon="🧊",
#    layout="wide",
#    initial_sidebar_state="expanded",
#)
#------------------------------------------------
# Archivos a importar
Data_RBI = pd.read_excel('Resultados_RBI.xls', sheet_name='Data')
df = pd.DataFrame(Data_RBI)
image1 = Image.open('Pagina_principal.JPG')
#------------------------------------------------
# Menu de la aplicación
Menu = st.sidebar.radio(
    "🖥️ Aplicación Resultados RBI",
    ('🏠 Página de inicio', '⚙️ Dashboard 1 - Equipos de planta', '🛢️ Dashboard 2 - Ductos de transporte'))
if Menu == '🏠 Página de inicio':
	html_temp = """
	<div style="background-color:rgb(37, 36, 64) ;padding:10px">
	<h2 style="color:white;text-align:center;">MEKINNOVA</h2>
	</div>
	"""
	st.markdown(html_temp, unsafe_allow_html=True)
	st.image(image1, caption='Python-Streamlit',use_column_width=True)
if Menu == '⚙️ Dashboard 1 - Equipos de planta':

	st.sidebar.title('Configuraciones')
	selectbox = st.sidebar.selectbox(
		    "Seleccione el campo de análisis",
		    ("pof","final_ca", "financial_cost", "pof_cat", "FC_cat", "CA_cat", "fin_risk_cat", "area_risk_cat"), index=0)
	selectbox_filtro_equipo = st.sidebar.selectbox(
		    "Seleccione el tipo de equipo",
		    ('pipe','tank650','vessel' ), index=0)

	st.title('Demo Dashboard - Equipos de planta')
	
	df = pd.DataFrame(Data_RBI)
	df_base = st.checkbox('Data base', value=False, key=None)
	if df_base ==True:
		st.write(df)
	df2=df.describe()
	df_estadisticas = st.checkbox('Estadísticas Data Base', value=False, key=None)
	if df_estadisticas ==True:
		st.write(df2)

	analisis_globales = st.checkbox('Análisis globales', value=False, key=None)
	if analisis_globales ==True:
	
		grafico= alt.Chart(df).mark_point().encode(
			x = 'No',
			y = selectbox,
			tooltip=['No',selectbox] 
			).interactive()
		histograma = alt.Chart(df).mark_bar(color='green').encode(
		 		alt.X(selectbox, bin=True),
		 		y='count()',
		 		tooltip=['count()'] 
		).interactive().properties()
		st.altair_chart(grafico | histograma)


	analisis_filtro = st.checkbox('Análisis comparativo', value=False, key=None)
	if analisis_filtro ==True:

		df1_mask = df['equipment_type'] == selectbox_filtro_equipo
		filtered1_df = df[df1_mask]
		st.write(filtered1_df)



		grafico_filtrado= alt.Chart(filtered1_df).mark_point().encode(
			x = 'No',
			y = selectbox,
			tooltip=['No',selectbox] 
			).interactive()

		histograma_filtrado = alt.Chart(filtered1_df).mark_bar(color='green').encode(
		 		alt.X(selectbox, bin=True),
		 		y='count()',
		 		tooltip=['count()'] 
		).interactive().properties()

		st.altair_chart(grafico_filtrado | histograma_filtrado)

	otros_parametros = st.checkbox('Otros metodos de configuracion y parámetros en streamlit', value=False, key=None)
	if otros_parametros ==True:


		if st.button('Botón'):
		   st.write('Este boton permite condicionar graficos y parametros de la aplicación')

		options = st.multiselect(
		    'multiseleccion',
		    ['Green', 'Yellow', 'Red', 'Blue'],
		    ['Yellow', 'Red'])
		st.write('Has seleccionado los colores:', options)

		age = st.slider('How old are you?', 0, 130, 25)
		st.write("I'm ", age, 'years old')

		values = st.slider(
		    'Select a range of values',
		    0.0, 100.0, (25.0, 75.0))
		st.write('Values:', values)


		color = st.select_slider(
		    'Select a color of the rainbow',
		    options=['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet'])
		st.write('My favorite color is', color)


		start_color, end_color = st.select_slider(
		    'Select a range of color wavelength',
		    options=['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet'],
		    value=('red', 'blue'))
		st.write('You selected wavelengths between', start_color, 'and', end_color)


		number = st.number_input('Insert a number')
		st.write('The current number is ', number)



		import numpy as np

		color = st.color_picker('Pick A Color', '#00f900')
		st.write('The current color is', color)




		col1, col2, col3 = st.beta_columns(3)

		with col1:
		   st.header("A cat")
		   st.image("https://static.streamlit.io/examples/cat.jpg", use_column_width=True)

		with col2:
		   st.header("A dog")
		   st.image("https://static.streamlit.io/examples/dog.jpg", use_column_width=True)

		with col3:
		   st.header("An owl")
		   st.image("https://static.streamlit.io/examples/owl.jpg", use_column_width=True)



		col1, col2 = st.beta_columns([3, 1])
		data = np.random.randn(10, 1)

		col1.subheader("A wide column with a chart")
		col1.line_chart(data)

		col2.subheader("A narrow column with the data")
		col2.write(data)