import streamlit as str
from langchain_community.utilities import SQLDatabase
from langchain_experimental.sql import SQLDatabaseChain
from langchain_google_genai import ChatGoogleGenerativeAI  # <-- Updated import
import os
from dotenv import load_dotenv

load_dotenv()  # Automatically loads GOOGLE_API_KEY from the .env file

# Set up Streamlit Page Configuration
str.set_page_config(page_title="Gemini SQL Query Generator", page_icon="🤖")
str.title("🤖 Talk to Your SQL Database (Powered by Gemini)")
str.write("Ask questions in plain English, and Gemini will write & execute the SQL query!")

# 1. Verify the Google API Key is present
google_key = os.getenv("GOOGLE_API_KEY") 

if not google_key:
    str.error("Please add your GOOGLE_API_KEY to the .env file.")
else:
    try:
        # 2. Connect to the SQLite Database
        db = SQLDatabase.from_uri("sqlite:///ecommerce.db")

        # 3. Initialize Gemini Model (Using gemini-2.5-flash for speed and low latency)
        llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash", temperature=0)

        # 4. Create the LangChain SQL Chain
        db_chain = SQLDatabaseChain.from_llm(llm, db, verbose=True)

        # 5. User Interface Chat Input
        user_question = str.text_input(
            "Ask a question about the data:", 
            placeholder="e.g., Which product generated the highest revenue?"
        )

        if user_question:
            with str.spinner("Gemini is analyzing the database..."):
                # Run the query through the Gemini SQL chain
                response = db_chain.run(user_question)
                
                str.success("Done!")
                str.subheader("Answer:")
                str.write(response)
                
    except Exception as e:
        str.error(f"An error occurred: {e}")