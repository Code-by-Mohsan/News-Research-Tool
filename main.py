#os is a python libaray which intract with oprating system(laptop etc.) to perform various system level tasks like accessing
#invironment variables (e.g., reading database credentials, API keys) 
import os

#The streamlit library is a popular Python library used for creating interactive web applications UI specifically designed 
# for data science and machine learning projects. 
import streamlit as st

#Save and load Python objects (e.g., FAISS index , lists, dictionaries, or custom classes)
import pickle

#The time module in Python provides a variety of time-related functions that allow you to work with time measurements, 
# delays, and timestamps
import time

#Langchian is a framework that Provide tools for text loading, processing, embedding, and querying
from langchain import OpenAI



#RetrievalQAWithSourcesChain class is useful for building a question-answering system that not only provides answers but also 
# gives the sources for those answers, leveraging vector search(FAISS) and LLMs for robust and accurate responses.
from langchain.chains import RetrievalQAWithSourcesChain


#Large documents are split into chunks for efficient embedding generation and querying.
#ensures logical splitting (e.g., sentences, paragraphs, spaces, full stop)
from langchain.text_splitter import RecursiveCharacterTextSplitter


#This loader extracts the textual content from web pages. Necessary for handling unstructured HTML data.
from langchain.document_loaders import UnstructuredURLLoader


#Embedding===Numerical representations of text that capture its semantic meaning.
#Enable similarity search, making it possible to find relevant chunks.
#OpenAIEmbeddings====Pre-trained, state-of-the-art embeddings optimized for NLP tasks
from langchain.embeddings import OpenAIEmbeddings

#A library for similarity search using vector embeddings (sementic search).
from langchain.vectorstores import FAISS

from dotenv import load_dotenv
load_dotenv()  # take environment variables from .env (especially openai api key)
openai_api_key = os.getenv("OPENAI_API_KEY")
if not openai_api_key:
    st.error("API Key is missing. Please check your .env file.")
    
    
    

st.title("NewsBot: News Research Tool 📈")
st.sidebar.title("News Article URLs")

urls = []
for i in range(3):
    url = st.sidebar.text_input(f"URL {i+1}")
    urls.append(url)

process_url_clicked = st.sidebar.button("Process URLs")
file_path = "faiss_store_openai.pkl"

main_placeholder = st.empty()
llm = OpenAI(openai_api_key=openai_api_key, temperature=0.9, max_tokens=500)

if process_url_clicked:
    # load data
    loader = UnstructuredURLLoader(urls=urls)
    main_placeholder.text("Data Loading...Started...✅✅✅")
    data = loader.load()
    # split data
    text_splitter = RecursiveCharacterTextSplitter(
        separators=['\n\n', '\n', '.', ','],
        chunk_size=1000
    )
    main_placeholder.text("Text Splitter...Started...✅✅✅")
    docs = text_splitter.split_documents(data)
    # create embeddings and save it to FAISS index
    embeddings = OpenAIEmbeddings()
    vectorstore_openai = FAISS.from_documents(docs, embeddings)
    main_placeholder.text("Embedding Vector Started Building...✅✅✅")
    time.sleep(2)

    # Save the FAISS index to a pickle file
    with open(file_path, "wb") as f:
        pickle.dump(vectorstore_openai, f)

query = main_placeholder.text_input("Question: ")
if query:
    if os.path.exists(file_path):
        with open(file_path, "rb") as f:
            vectorstore = pickle.load(f)
            chain = RetrievalQAWithSourcesChain.from_llm(llm=llm, retriever=vectorstore.as_retriever())
            result = chain({"question": query}, return_only_outputs=True)
            # result will be a dictionary of this format --> {"answer": "", "sources": [] }
            st.header("Answer")
            st.write(result["answer"])

            # Display sources, if available
            sources = result.get("sources", "")
            if sources:
                st.subheader("Sources:")
                sources_list = sources.split("\n")  # Split the sources by newline
                for source in sources_list:
                    st.write(source)




