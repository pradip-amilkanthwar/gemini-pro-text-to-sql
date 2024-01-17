import os
import sqlite3

import streamlit as st
from dotenv import load_dotenv

load_dotenv()

import google.generativeai as genai

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))


def get_gemini_responce(question, prompt):
    model = genai.GenerativeModel("gemini-pro")
    response = model.generate_content([prompt[0], question])
    return response.text


def read_sql_query(sql, db):
    conn = sqlite3.connect(db)
    cur = conn.cursor()
    cur.execute(sql)
    rows = cur.fetchall()
    conn.commit()
    conn.close()

    for row in rows:
        print(row)
    return rows


prompt = [
    """
You are an expert in converting EEnglish question to SQL query!
The SQL Database has a name student_info and has following columns - name,class, section, marks\n\nfor example\n\nExample 1 - How many entries of records are present?,
the sql command will be something like this SELECT COUNT(*) FROM student_info;
\n example 2 - Tell me all the students studying in data science class?,
\nThe SQL Command will be like SELECT name FROM student_info WHERE class = 'Data Science'
\n also the sql should not have ''' in start or end and sql word in it

"""
]

st.header("Sample text to sql application")
question = st.text_input("Input : ", key="input")
submit = st.button("Ask The Question")

if submit:
    response = get_gemini_responce(question, prompt)
    print("Returned response is ... ", response)
    data = read_sql_query(response, "student.db")
    st.subheader("The response is ... ")
    for row in data:
        st.header(row)
