import os
from dotenv import load_dotenv
from langchain import hub
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough
from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_upstage import UpstageGroundednessCheck
from langchain_community.chat_models import ChatOllama
from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
import warnings
warnings.filterwarnings('ignore')

load_dotenv()
filepath = os.getenv("FILE_PATH")

def main():
    loader = PyPDFLoader(filepath)
    docs = loader.load()

    text_splitter = RecursiveCharacterTextSplitter(chunk_size=256, chunk_overlap=64)
    splits = text_splitter.split_documents(docs)
    embeddings_model = HuggingFaceEmbeddings(model_name="sentence-transformers/all-mpnet-base-v2")
    vectorstore = Chroma.from_documents(documents=splits, embedding=embeddings_model)
    retriever = vectorstore.as_retriever()

    llm = ChatOllama(model="llama3.2")

    prompt = hub.pull("rlm/rag-prompt")

    def format_docs(docs):
        return "\n\n".join(doc.page_content for doc in docs)

    rag_chain = (
        {"context": retriever | format_docs, "question": RunnablePassthrough()}
        | prompt
        | llm
        | StrOutputParser()
    )

    groundedness_check = UpstageGroundednessCheck()

    q_list = [
        "What is the outlook for the Korean economy when assessing the risks?", 
        "What are the factors that could pose a threat to the economy?",
        ]
    
    rag_dicts = {}
    for q in q_list:
        rag_dicts[q] = rag_chain.invoke(q)
        print("-----------------------")
        print(f"Question: {q}")
        print(f"Answer: {rag_dicts[q]}")
        request_input = {
            "context": q,
            "answer": rag_dicts[q],
        }
        response = groundedness_check.invoke(request_input)
        print(f"RAG test is {response}")
        print("-----------------------")


if __name__=='__main__':
    main()
