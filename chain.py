from prompt import memory_prompt
from dotenv import load_dotenv

from langchain_openai import ChatOpenAI
from langchain_core.runnables.history import RunnableWithMessageHistory
from langchain_core.output_parsers import StrOutputParser
from langchain_community.chat_message_histories import ChatMessageHistory

load_dotenv()

store = {}

# Function that returns history for your sessions
def get_memory_history(key: str) -> ChatMessageHistory:
    if key not in store:
        store[key] = ChatMessageHistory()
    return store[key]

def build_chain():
    llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0.9) # 1. Create your LLM
    chain = memory_prompt | llm | StrOutputParser() # 2. Create your chain
    chain_with_memory = RunnableWithMessageHistory( # 3. Wrap your chain with RunnableWithMessageHistory, passing in your chain and the function to get the history
        chain, 
        get_memory_history,
        input_messages_key="input",
        history_messages_key="history"
    )
    return chain_with_memory # 4. Return
