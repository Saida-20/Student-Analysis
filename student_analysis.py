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

#Line Chart
st.line_chart(df["scores"])

#Histogram (Matplotlib)
import matplotlib.pyplot as plt

fig, ax = plt.subplots()
ax.hist(df["scores"])
st.pyplot(fig)

#Improving the App UI
st.sidebar.title("Navigation")
option = st.sidebar.selectbox(
    "Choose View",
    ["Dataset", "Summary", "Visualizations"]
)

if option == "Dataset":
    st.dataframe(df)

elif option == "Summary":
    st.write(df.describe())

elif option == "Visualizations":
    st.bar_chart(df["department"].value_counts())




