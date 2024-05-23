from langchain_community.llms import Ollama

def get_llm_response(query):
    # Initialize the Ollama LLM with the specified model
    llm = Ollama(model="gemma:2b")
    # Query the LLM with the user's input and return the response
    response = llm.invoke(query)
    return response
