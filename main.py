import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import plotly.express as px


header = st.container()
dataset = st.container()
features = st.container()
model = st.container()

### Data Import ###

df= pd.read_csv("data/degrees-that-pay-back.csv")

with st.echo(code_location='below'):
	
	Majors = list(df['Undergraduate Major'].drop_duplicates())
	Percent_Change = list(df["Percent change from Starting to Mid-Career Salary"])

	### Filter Data for Specific Percent Change Range ###
	
	Percent_Change_Slider = st.sidebar.slider("Percent Change from Starting to Mid-Career Salary", min_value=1.0, max_value=100.0, step=10.0, value=25.0)

	df = df[df['Percent change from Starting to Mid-Career Salary'] > Percent_Change_Slider]

	st.dataframe(df.sort_values('Percent change from Starting to Mid-Career Salary', ascending =False).reset_index(drop=True))

	### Plotly Code ###

	fig1 = px.scatter(
		x=df["Undergraduate Major"],
		y=df["Percent change from Starting to Mid-Career Salary"],
	)
	fig1.update_layout(
		xaxis_title="Undergraduate Major",
		yaxis_title="Percent change from Starting to Mid-Career Salary",
	)

with header: 
	st.title('Degrees That Pay')
	st.text('A continuation of our final project. In this project we look into the Percent change from Starting to Mid-Career Salary, of students graduating with popular majors!')

with dataset:
	st.header('Kaggle Dataset')
	st.text('Our team found this dataset on Kaggle')
	st.write(fig1)

with features:
	st.header('Code for this project')


