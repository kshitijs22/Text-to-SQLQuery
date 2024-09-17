from dotenv import load_dotenv
load_dotenv() ## load all the environemnt variables

import streamlit as st
import os
import sqlite3
from groq import Groq

# STREAMLIT APP
st.set_page_config(page_title="SQL Retrieval by text")
st.header("Retrieve SQL Data using GROQ")
tablename=st.text_input("Table Name",key="tablename")
columnnames=st.text_input("Column Names",key="columnname")
question=st.text_input("Query ",key="input")
db_file = st.file_uploader("Choose a file (.db)",type='db')
submit=st.button("Ask the question")

# Define Your Prompt
prompt=[
    """
    You are an expert in converting English questions to SQL query!
    The SQL database has the name """ + tablename + """ and has the following columns - """ + columnnames +""" \n\n
    For example,\n

    Example 1 - How many entries of records are present?, 
    the SQL command will be something like this SELECT COUNT(*) FROM """+ tablename + """ . In this example tablename is Table name;\n

    Example 2 - Tell me all the students studying in Data Science class?, 
    the SQL command will be something like this SELECT * FROM STUDENT 
    where CLASS="Data Science". In this example, STUDENT is the table name and CLASS is one of the colmns; 
    also the sql code should not have ``` in beginning or end and sql word in output \n

    Example 3 - Based on tablename and columnnames, generate a SQL response for any uploaded db_file.
    """]
## Configure GroqApiKey Key
client=Groq(api_key=os.getenv("GROQ_API_KEY"))

## Function To Load Google Gemini Model and provide queries as response

def get_groq_response(client,question,prompt):
    completion=client.chat.completions.create(
        model='llama3-8b-8192',
        messages=[
            {
                "role":'system',
                'content':prompt
            },
            {
                "role":'user',
                'content':question
            }
        ])
    return completion.choices[0].message.content

## Fucntion To retrieve query from the database

def read_sql_query(sql,db):
    if db:

        # fp.write(db.getvalue())
        conn = sqlite3.connect(db)
        cur=conn.cursor()
        cur.execute(sql)
        rows=cur.fetchall()
        conn.commit()
        conn.close()
        return rows


# if submit is clicked
if submit:
    response=get_groq_response(client,question,prompt[0])
    response1=read_sql_query(response,db_file.name)
    st.subheader(" :blue[RESPONSE] :sunglasses: ")
    for row in response1:
        st.text(row[0])