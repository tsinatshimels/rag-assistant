from langchain_community.llms import Ollama  
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.chains import RetrievalQA
from langchain_community.vectorstores import Chroma
from langchain_community.document_loaders import TextLoader

# 1. Load documents
loader = TextLoader("data/sample.txt")
docs = loader.load()

# 2. Split docs into chunks
splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
splits = splitter.split_documents(docs)

# 3. Create embeddings locally 
embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")

# 4. Create a vector store 
vectorstore = Chroma.from_documents(documents=splits, embedding=embeddings)

# 5. Initialize the LOCAL LLM with Ollama
#    This replaces the ChatOpenAI part.
llm = Ollama(model="llama3")

# 6. Create the RetrievalQA chain 
qa_chain = RetrievalQA.from_chain_type(
    llm=llm,
    chain_type="stuff",
    retriever=vectorstore.as_retriever()
)

# 7. Query loop
print("RAG Assistant is ready! Ask your questions. Type 'quit' to exit.\n")
while True:
    query = input("You: ")
    if query.lower() == "quit":
        break
    # Use .invoke as before
    response = qa_chain.invoke({"query": query})
    print("Assistant:", response['result'], "\n")