import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt


st.title('My Data Dashboard')

uploaded_file = st.file_uploader("choose a file")

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.write(df)

    st.write(df.describe())

    st.write(df.dtypes)

    st.write(df.columns)

    st.write(df['age'].value_counts())

    st.write(df['age'].value_counts().plot(kind='bar'))
    st.pyplot()

    st.subheader("filter data")
    columb = df.columns.tollist()
    selected_column = st.selectbox("select column ", columb)
    unique_values = df[selected_column].unique()
    selected_value = st.selectbox("select value", unique_values)

    filtered_df= df[df[selected_column] == selected_value]
    st.write(filtered_df)
    
    st.subheader("plot data")
    x_columb = st.selectbox("select x axis", columb)
    y_columb = st.selectbox("select y axis", columb)

    if st.button("plot"):
        st.line_chart(filtered_df.set_index(x_columb)[y_columb])

else:
    st.write("waiting for file")

     