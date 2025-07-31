import streamlit as st
from db_helper import get_db_chain

st.set_page_config(page_title="StyleHub T-Shirts Database Q&A", page_icon="👕")

st.title("StyleHub T-Shirts: Database Q&A 👕")
st.markdown("Ask questions about our t-shirt inventory and get instant answers!")

question = st.text_input("Enter your question about t-shirts:")

if st.button("Get Answer") and question:
    with st.spinner("Searching our database..."):
        try:
            chain = get_db_chain()
            # Modified execution to match expected input format
            response = chain.run(question)

            st.subheader("Answer")
            st.success(response)

        except Exception as e:
            st.error(f"Error processing your question: {str(e)}")
            st.info("Please try rephrasing your question or ask something else.")