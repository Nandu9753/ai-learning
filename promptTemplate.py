from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate,PromptTemplate
from decouple import config
KEY = config('OPEN_API_KEY')
llm = ChatOpenAI(api_key=KEY)
# example 1 
# prompt = ChatPromptTemplate.from_messages([
#     ("system", "You are a world class technical documentation writer."),
#     ("user", "{input}")
# ])
# noInput = prompt.format(input='create resume')
# response = llm.invoke(noInput)
# print(response.content)

# example 2 prompt template
# oneInputPrompt = PromptTemplate.from_template("please explaine {language} with example")

# formattedOneInputPrompt = oneInputPrompt.format(language="go")
# print("No Input Prompt: ", formattedOneInputPrompt)
# response = llm.invoke(formattedOneInputPrompt)
# print("Response: ", response.content)

# # Example 3 - Prompt having Multiple Input Variable

# multipleInputPrompt = PromptTemplate.from_template(
#     "what is difference in {topic1} and {topic2}?")
# formattedMultipleInputPrompt = multipleInputPrompt.format(
#     topic1="session", topic2="cockies")
# response = llm.invoke(formattedMultipleInputPrompt)
# print("Response: ", response.content)

# Example 4 - PromptTemplate - No input variable manually

template = "Tell me a {language} {topic} trick"
promptTemplate = PromptTemplate.from_template(template)
print("Prompt Template: ", promptTemplate)
print("Prompt Template Input Variables: ", promptTemplate.input_variables)
formattedPromptTemplate = promptTemplate.format(
    language="python",
    topic="array"
)

print("Formatted Prompt Template: ", formattedPromptTemplate)
response = llm.invoke(formattedPromptTemplate)
print("Response: ", response)
