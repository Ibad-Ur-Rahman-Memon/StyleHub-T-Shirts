from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.utilities import SQLDatabase
from langchain_experimental.sql import SQLDatabaseChain
from langchain.prompts import PromptTemplate
import os
from dotenv import load_dotenv

load_dotenv()

def get_db_chain():
    # Database connection setup
    db = SQLDatabase.from_uri(
        f"mysql+mysqlconnector://{os.getenv('DB_USER')}:{os.getenv('DB_PASSWORD')}@{os.getenv('DB_HOST')}/{os.getenv('DB_NAME')}",
        sample_rows_in_table_info=1,
        include_tables=['t_shirts']
    )

    # LLM initialization
    llm = ChatGoogleGenerativeAI(
        model="gemini-2.5-flash",
        google_api_key=os.getenv("GOOGLE_API_KEY"),
        temperature=0.1,
        model_kwargs={
            "response_mime_type": "text/plain"  # Ensures text output
        }
    )

    # Prompt template
    mysql_prompt = """You are a helpful assistant for StyleHub T-Shirts. Follow these steps:
    1. Generate a correct MySQL query for the question
    2. Execute the query against the database
    3. Return the answer in natural language

    Example:
    Question: How many Adidas t-shirts?
    SQLQuery: SELECT SUM(stock_quantity) FROM t_shirts WHERE brand = 'Adidas'
    Answer: There are 42 Adidas t-shirts in stock.

    Current Question: {input}
    """

    prompt = PromptTemplate(
        input_variables=["input"],
        template=mysql_prompt
    )

    # Create and return the chain
    return SQLDatabaseChain.from_llm(
        llm,
        db,
        prompt=prompt,
        verbose=False,
        use_query_checker=True,
        return_intermediate_steps=False,
        return_direct=False
    )