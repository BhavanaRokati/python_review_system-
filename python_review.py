# -*- coding: utf-8 -*-
"""python_review.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1Rx7fTUqQU4F4Sby2ZzZrT2cBlsxzL5ef
"""


import streamlit as st
import google.generativeai as genai



genai.configure(api_key="AIzaSyBkxnuIbA8tw7Q8zIdB_ZQqyhdTrWrsr2Q")
sys_prompt = """
You are an advanced Python code reviewer. Your task is to analyze the given Python code, identify potential bugs, logical errors, and areas of improvement, and suggest fixes.

Your response should be structured as follows:
1. **Issues Detected**: List any errors, inefficiencies, or improvements needed.
2. **Fixed Code**: Provide the corrected version of the code.
3. **Explanation**: Explain why the changes were made in a concise manner.

If the code is already optimal, acknowledge it and suggest best practices.
"""

def code_review(code):
    """Function to send user code to Google Gemini AI for review."""
    model = genai.GenerativeModel("models/gemini-2.0-pro-exp",system_instruction=sys_prompt)  # Use latest Gemini model
    user_prompt = f"Review the following Python code and provide feedback on potential bugs, improvements, and fixes:\n\n{code}"

    response = model.generate_content(user_prompt)

    return response.text  #

# Streamlit UI
st.title("Python Code Reviewer ")

st.write("Submit your Python code for automated review and receive bug reports with suggested fixes.")

# User input for Python code
code_input = st.text_area("Enter your Python code:", height=200)

if st.button("Review Code"):
    if code_input.strip():
        with st.spinner("Analyzing your code with Google AI..."):
            feedback = code_review(code_input)
        st.subheader("Code Review Report 📋")
        #st.text_area("Review Output", feedback, height=300)
        st.markdown(feedback)
    else:
        st.warning("Please enter some Python code before submitting.")
