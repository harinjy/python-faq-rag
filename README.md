# PythonFAQUsingRAG

## Description
This project implements a Python FAQ (Frequently Asked Questions) system using Retrieval-Augmented Generation (RAG). It utilizes LangChain, Amazon Bedrock, and FAISS for the backend, with a Streamlit-based frontend for user interaction.

## Setup
1. Ensure you have Python installed on your system.
2. Install the required dependencies:
   ```
   pip install langchain langchain_community langchain_text_splitters langchain_aws streamlit faiss-cpu
   ```
3. Set up AWS credentials with access to Amazon Bedrock services.
4. Place your FAQ document named "faq.pdf" in the project root directory.

## Usage
1. Run the Streamlit application:
   ```
   streamlit run frontend.py
   ```
2. Open the provided URL in your web browser.
3. Enter your question in the text area.
4. Click the "ASK" button to get a response from the FAQ system.

Note: The system uses Amazon Bedrock for embeddings and language model inference. Ensure you have the necessary permissions and credits for using these services.