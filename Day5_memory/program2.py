# Short term memory

from langchain.chat_models import init_chat_model
from langchain.agents import create_agent
from langchain.messages import HumanMessage
from langgraph.checkpoint.memory import InMemorySaver

# create model connection
model = init_chat_model(model= "qwen2.5:7b", model_provider="ollama")

# create a short term memory for the agent
checkpointer = InMemorySaver()

# create an agent
agent = create_agent(
    # use the InMemorySaver scheme for remembering the information in the memory
    checkpointer=checkpointer,
    model=model,
    system_prompt="You are a helpful assistant"
)

# create a configuration
config = {"configurable": {"thread_id": "session1"}}

while True:
    query = input("> ")
    if query in ['exit','quit']:
        break
    
    # Send the query to agent
    response  = agent.invoke(
        # Send the query message
        {"messages": [HumanMessage(content=query)]},
        
        # Send the session information
        config = config )
        
    # print response
    print(response['messages'][-1].content)
    



