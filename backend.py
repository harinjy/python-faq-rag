from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.embeddings import BedrockEmbeddings
from langchain.indexes import VectorstoreIndexCreator
from langchain_community.vectorstores import FAISS
from langchain_aws import BedrockLLM


def python_index():
    """
    Creates and returns a vector store index from a PDF document.

    This function loads a PDF file, creates embeddings using
    Amazon Bedrock's Titan model, and builds a FAISS vector store index.

    Returns:
        VectorStoreIndexCreator: An index containing the processed PDF content
    """
    loader = PyPDFLoader("faq.pdf")
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=300,
        chunk_overlap=20,
        separators=["\n\n", "\n", " ", ""],
    )

    embeddings = BedrockEmbeddings(
        model_id="amazon.titan-embed-text-v2:0",
        credentials_profile_name="default",
        region_name="us-east-1",
    )

    data_index = VectorstoreIndexCreator(
        vectorstore_cls=FAISS,
        embedding=embeddings,
        text_splitter=text_splitter,
    )
    return data_index.from_loaders([loader])


def query_llm():
    """
    Initializes and returns a Bedrock LLM instance using Claude v2.

    Configures the LLM with specific parameters for token generation,
    temperature, and top_p sampling.

    Returns:
        BedrockLLM: Configured LLM instance for generating responses
    """
    llm = BedrockLLM(
        credentials_profile_name="default",
        model_id="anthropic.claude-v2",
        model_kwargs={
            "max_tokens_to_sample": 1000,
            "temperature": 0.1,
            "top_p": 0.9,
        },
    )
    return llm


def query_index(index, question):
    """
    Queries the vector store index with a given question using the LLM.

    Args:
        index: The vector store index to query against
        question (str): The question to be answered

    Returns:
        str: The generated response from the LLM based on relevant context
    """
    rag_llm = query_llm()
    return index.query(question=question, llm=rag_llm)
