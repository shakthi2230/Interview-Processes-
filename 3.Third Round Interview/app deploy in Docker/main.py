# ---------------------- 1 st Part(PDF to Text )-----------------
from langchain_community.document_loaders import PyPDFLoader 

loader = PyPDFLoader("SAKTHIVEL .pdf")  
pages_content = loader.load_and_split()

# -------------------------2 nd Part (Text to Embeddings as convertion)------------: 
from langchain.embeddings.openai import OpenAIEmbeddings  
from langchain_community.vectorstores import FAISS 

embeddings = OpenAIEmbeddings()
db = FAISS.from_documents(pages_content, embeddings)
db.save_local("faiss_index")
new_db = FAISS.load_local("faiss_index", embeddings, allow_dangerous_deserialization=True)

#------------------------ 3 rd Part(Similar Search From local db)-------------------
query = "sakthivel"
# docs = new_db.similarity_search(query)  # Corrected method name
# print(docs)

#----------------------4 th part(Chat With OpenaI using Langchain)----------------------

from langchain.chains import RetrievalQA
from langchain.chat_models import ChatOpenAI

llm=ChatOpenAI()
qa_chain=RetrievalQA.from_chain_type(llm,retriever=new_db.as_retriever())
# res=qa_chain({"query":"coapps.ai"})
# print(res)
def ask(user_query):
    res=qa_chain({"query":user_query})
    return res["result"]