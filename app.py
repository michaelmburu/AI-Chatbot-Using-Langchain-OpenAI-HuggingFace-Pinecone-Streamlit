import streamlit as st
from utils import *
#create session state variable
if 'HuggingFace_API_Key' not in st.session_state:
    st.session_state['HuggingFace_API_Key'] = ''

if 'Pinecone_API_Key' not in st.session_state:
    st.session_state['PineCone_API_Key'] = ''

# START UI

st.title("🤖 AI Chatbot Assistance For Your KenyaLaw Org")

#Sidebar
st.sidebar.title("😎🗝")
st.session_state['HuggingFace_API_Key'] = st.sidebar.text_input("What's your HuggingFace API Key?", type="password")
st.session_state['Pinecone_API_Key'] = st.sidebar.text_input("What's your Pinecone API Key?", type="password" )

load_button = st.sidebar.button("Load data to Pinecone", key="load_button")

#If above button is clicked load data to Pinecone
if load_button:
    #Proceed if only API keys are provided
    if st.session_state['HuggingFace_API_Key'] != "" and st.session_state['Pinecone_API_Key'] != "":

        #Fetch data from site
        site_data = get_website_data("http://kenyalaw.org/sitemap.xml")
        st.write("Data pull done...")

        #Split data into chunks
        chunks_data = split_data(site_data)
        st.write("Splitting data done...")

        #Create embeddings instance
        embeddings = create_embeddings()
        st.write("Embeddings instance creation done...")

        #Push data to PineCone
        st.write("Pushing data to PineCone done.....")

        st.sidebar.success("Bazuu, Data nimepush push to PineCone successfuly.")

    else:
        st.sidebar.error("Wueeeeh!!! Ebu nipee API keys zinawork banaa. I can't.")

 # Sidebar functionality end       