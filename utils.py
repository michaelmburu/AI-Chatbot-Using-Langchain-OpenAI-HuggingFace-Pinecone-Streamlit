from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.vectorstores import Pinecone
from langchain.embeddings.sentence_transformer import SentenceTransformerEmbeddings
import Pinecone
import asyncio
from langchain.document_loaders.sitemap import SitemapLoader

#Function to fetch data from website
def get_website_data(sitemap_url)
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loader = SitemapLoader(sitemap_url)
    docs = loader.load()

    return docs

#Function to split data into smaller chunks
def split_data(docs):
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200, length_function = len)
    docs_chunks = text_splitter.split_documents(docs)
    return docs_chunks

#Function to creating embeddings instance
def create_embeddings():
    #Huggingface embeddings
    embeddings = SentenceTransformerEmbeddings(model_name="all-MiniLM-L6-v2")
    return embeddings

#Function to push data to PineCone
def push_to_pinecone(pinecone_apikey, pinecone_environment, pincode_index_name, embeddings, docs):
    pinecone.init(api_key = pinecone_apikey, environment = pinecone_environment)