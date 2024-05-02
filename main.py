import streamlit as st
import pandas as pd

# Load the datasets
df = pd.read_csv("LeetcodeDATA.csv")
descriptions = pd.read_csv("leetcode_dataset.csv")

# Set page title and favicon
st.set_page_config(page_title='Leetcode Code Snippet', page_icon=":computer:")

# Define the title and introduction
st.title('Leetcode Code Snippet Finder')
st.write("Welcome to the Leetcode Code Snippet Finder! Enter the question number below to get the code snippet and title.")

# Input field for question ID
question_id = st.number_input('Enter the question ID:', min_value=1, max_value=len(df), value=1, step=1)

# Adjust question ID to zero-based indexing
question_index = question_id - 1

# Get the code snippet and title for the selected question
if st.button('Get Code Snippet and Title'):

    # Retrieve title
    title = descriptions.loc[descriptions['id'] == question_id, 'title'].iloc[0]
    st.header(title)
    
    # Retrieve title
    description = descriptions.loc[descriptions['id'] == question_id, 'description'].iloc[0]
    st.header(description)


    # Retrieve code snippet
    code = df.loc[question_index, 'Answer']
    st.header("Code Snippet:")
    st.code(code, language='cpp')  # Assuming the code snippets are in C++

    # Retrieve title
    companies = descriptions.loc[descriptions['id'] == question_id, 'companies'].iloc[0]
    st.title('Asked In:')
    st.write(companies)

    

# Add a footer with additional information or links
st.markdown("---")
st.markdown("Created with ❤ by Zuber and Harsh")
