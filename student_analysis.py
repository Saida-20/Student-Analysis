import pandas as pd
import streamlit as st

st.title("Student Performance Analysis")

df = pd.read_csv("exam_scores.csv")

st.subheader("Dataset Preview")
st.dataframe(df.head())

st.subheader("Dataset Summary")
st.write(df.describe())

#Adding features and interactivity: Buttons
if st.button("Show Dataset"):
	st.dataframe(df)

#add Slider

min_score = st.slider("Select Minimum Score", 0, 80, 50)
filtered_df = df[df["scores"] >= min_score]
st.dataframe(filtered_df)

#File upload
uploaded_file = st.file_uploader("Upload CSV file")

if uploaded_file:
	df = pd.read_csv(uploaded_file)
	st.dataframe(df)

#Visualization options

#Barchart
st.bar_chart(df["name"].value_counts())