from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder

memory_prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant that can remember previous conversations and use that information to provide better responses. You do not ask for the information you already have"),

    MessagesPlaceholder(variable_name="history"),

    ("human", "{input}")
])
