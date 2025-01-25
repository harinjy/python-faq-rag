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

> [!NOTE]
>
> The system uses Amazon Bedrock for embeddings and language model inference. Ensure you have the necessary permissions and credits for using these services.

## Tutorial: Understanding the application

### Core Concepts

1. **Retrieval-Augmented Generation (RAG)**
- `RAG` combines the power of large language models with specific knowledge retrieval
- Instead of relying solely on the model's training data, RAG retrieves relevant information from your FAQ document
- This ensures more accurate and context-specific responses

2. **Key Components**
- Document Processing: Your FAQ document is split into smaller chunks for efficient processing
- `Vector Database (FAISS)`: Converts text chunks into numerical representations (embeddings) for similarity search
- `LangChain`: Orchestrates the workflow between document processing, retrieval, and generation
- `Amazon Bedrock`: Provides the foundation models for embeddings and text generation

### How It Works

1. **Document Indexing**
- The system reads your FAQ.pdf file
- The document is split into manageable chunks
- Each chunk is converted into embeddings using Amazon Bedrock
- These embeddings are stored in a FAISS vector database

2. **Query Processing**
- When you ask a question, it's converted into an embedding
- The system searches the FAISS database for similar content
- Relevant FAQ sections are retrieved

3. **Response Generation**
- Retrieved FAQ sections are sent to the language model
- The model generates a contextual response using both the question and retrieved content
- The response is displayed in the Streamlit interface

### Best Practices

1. **Document Preparation**
- Structure your FAQ document clearly
- Use consistent formatting
- Include diverse questions and detailed answers

2. **Query Formation**
- Ask clear, specific questions
- One question at a time works best
- Include relevant context in your question

3. **System Maintenance**
- Regularly update your FAQ document
- Monitor system performance
- Keep dependencies up to date