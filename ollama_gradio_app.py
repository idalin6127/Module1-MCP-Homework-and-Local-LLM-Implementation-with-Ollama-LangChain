from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough
from langchain_ollama import ChatOllama
import gradio as gr

# Step 1: Define the prompt
prompt = PromptTemplate.from_template("What is the capital of {topic}?")

# Step 2: Define the model
model = ChatOllama(model="llama2")  # 本地 Ollama 模型

# Step 3: Create the LCEL Chain
chain = (
    {"topic": RunnablePassthrough()}
    | prompt
    | model
    | StrOutputParser()
)

# Step 4: Define Gradio interface function
def query_ollama(user_input):
    return chain.invoke(user_input)

# Step 5: Create Gradio interface
demo = gr.Interface(
    fn=query_ollama,
    inputs=gr.Textbox(lines=1, placeholder="Enter a country name..."),
    outputs=gr.Textbox(label="Capital City"),
    title="LLM Local Chat - Ollama + LangChain + Gradio",
    description="Ask 'What is the capital of X?' and see how local llama2 replies."
)

# Step 6: Launch the UI
demo.launch()
