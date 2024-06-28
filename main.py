from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from decouple import config
KEY = config('OPEN_API_KEY')
llm = ChatOpenAI(api_key=KEY)
response = llm.invoke("how to create software?")
print(response)

# prompt template
prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a world class technical documentation writer."),
    ("user", "{input}")
])