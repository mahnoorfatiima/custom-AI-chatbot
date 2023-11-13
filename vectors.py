import os
from llama_index import SimpleDirectoryReader, GPTVectorStoreIndex, LLMPredictor, ServiceContext, PromptHelper
from langchain.chat_models import ChatOpenAI
import gradio as gr


os.environ["OPENAI_API_KEY"] = '<YOUR-API-KEY>'

def init_index():
    max_input_size = 4096
    num_outputs = 512
    chunk_size_limit = 400

    prompt_helper = PromptHelper(max_input_size, num_outputs, chunk_overlap_ratio= 0.1, chunk_size_limit=chunk_size_limit)
    llm_predictor = LLMPredictor(llm=ChatOpenAI(temperature=0.7, model_name="gpt-3.5-turbo", max_tokens=num_outputs))

    dir_path = os.path.join(os.path.dirname(__file__), 'dir')
    documents = SimpleDirectoryReader(dir_path).load_data()

    service_context = ServiceContext.from_defaults(llm_predictor=llm_predictor, prompt_helper=prompt_helper)
    index = GPTVectorStoreIndex.from_documents(documents, service_context=service_context)

    index.storage_context.persist("index")
    return index

def chatbot(input_text):
    documents = SimpleDirectoryReader('index').load_data()
    index = GPTVectorStoreIndex.from_documents(documents)

    query_engine = index.as_query_engine()
    response = query_engine.query(input_text)

    return response.response


iface = gr.Interface(fn=chatbot,
                     inputs=gr.components.Textbox(lines=7, placeholder="Enter your question here"),
                     outputs="text",
                     title="AI ChatBot for Icon: Your Knowledge Companion",
                     description="Ask any question about Icon Product")
index = init_index()
iface.launch(share=True)
