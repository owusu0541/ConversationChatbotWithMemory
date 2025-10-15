import streamlit as st 
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationChain
from langchain_aws import ChatBedrockConverse
def demo_chatbot():
    demo_llm=ChatBedrockConverse(
        credentials_profile_name='default',
        region_name="us-east-1",
        model="amazon.nova-pro-v1:0",
        temperature=0.1,
        max_tokens=1000)
    return demo_llm

def demo_memory():
    llm_data=demo_chatbot()
    memory=ConversationBufferMemory(llm=llm_data,max_token_limit=2000)
    return memory


def demo_conversation(input_text,memory):
    llm_chain_data=demo_chatbot()
    llm_conversation = ConversationChain(
    llm=llm_chain_data, 
    memory=memory,
    verbose=True
)
#5 Chat response using invoke (Prompt template)
    chat_reply=llm_conversation.invoke(input_text)
    return chat_reply['response']
    

st.title("I am a Conversational Chatbot With Memory :sunglasses:")
#st.sidebar.image("law (2).jpg", width=250)
st.sidebar.title("Profile of the Developer") 
st.sidebar.markdown("""Data Scientist with 3+ years of experience of building and deploying production-grade ML, DL and LLM applications on AWS
and Kubernetes clusters. Skilled in building agentic AI systems and RAG workflows, with proven success in reducing literature
review turnaround time by 50 percent and cutting deployment delivery time by 50% through CI/CD pipelines.
. My research interests include deep learning, machine learning, adversarial machine learning, privacy-preserving machine learning, and data security""")

st.sidebar.subheader("Name: Lawrence Owusu")
st.sidebar.subheader("Email: lawrenceowusu0541@gmail.com")
st.sidebar.subheader("GenAI engineer, Data Scientist, Machine Learning Engineer, Data Analyst")
st.sidebar.subheader("Credentials: BSc, M.S., M.S., PhD candidate, 6X AWS certified, Certified ScrumMaster, SQL Developer.")
st.sidebar.subheader("Technical Skills: Python programming, Pytorch, Keras and Tensorflow, FastAPI, Spark, SQL, AWS, Airflow, Github Actions, Kubernetes, Docker, Git, AWS, Streamlit, Jenkins.")
#st.sidebar.link_button("Link to Publication", "https://doi.org/10.5815/ijisa.2024.05.05")
st.markdown("""I provide intelligent, context-aware responses while remembering key details from your previous messages. It is ideal for exploration of ideas, question and answers and interactive learning.""")

st.divider()


#name = st.text_input("What is your you name ?")

if 'memory' not in st.session_state: 
    st.session_state.memory = demo_memory() 


if 'chat_history' not in st.session_state: 
    st.session_state.chat_history = [] 

for message in st.session_state.chat_history: 
    with st.chat_message(message["role"]): 
        st.markdown(message["text"]) 
     
input_text = st.chat_input("Please, you can start your conversation now") 
if input_text: 
    
    with st.chat_message("user"): 
        st.markdown(input_text) 
    
    st.session_state.chat_history.append({"role":"user", "text":input_text}) 

    chat_response = demo_conversation(input_text=input_text, memory=st.session_state.memory) #** replace with ConversationChain Method name - call the model through the supporting library
    
    with st.chat_message("assistant"): 
        st.markdown(chat_response) 
    
    st.session_state.chat_history.append({"role":"assistant", "text":chat_response}) 