from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.embeddings import BedrockEmbeddings
from langchain.indexes import VectorstoreIndexCreator
from langchain_community.vectorstores import FAISS
from langchain_aws import BedrockLLM


def python_index():

    loader = PyPDFLoader("faq.pdf")
    documents = loader.load_and_split()

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
    rag_llm = query_llm()
    return index.query(question=question, llm=rag_llm)
