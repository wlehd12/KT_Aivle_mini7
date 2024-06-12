from langchain.memory import ConversationBufferMemory

def memory_save(message):
    memory = ConversationBufferMemory(memory_key='chat_history', return_messages=True)
    for msg in message:
        memory.save_context({"input": msg[0]},
                        {"output": msg[1]})
    return memory