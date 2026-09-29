import streamlit as st
from langchain_core.messages import HumanMessage, AIMessage, ToolMessage
from graph import agent_graph

st.set_page_config(page_title="AI Wedding Planner", page_icon="💍")
st.title("💍 AI Wedding Planner Agent")
st.markdown("Chat with our AI to find and book your perfect wedding hall!")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []
    # Optional: Start the conversation with an AI greeting
    initial_response = agent_graph.invoke({"messages": [HumanMessage(content="Hi")]})
    st.session_state.messages.extend(initial_response["messages"])

# Display chat history (filtering out internal Tool messages for a clean UI)
for msg in st.session_state.messages:
    if isinstance(msg, HumanMessage):
        st.chat_message("user").write(msg.content)
    elif isinstance(msg, AIMessage) and msg.content:
        st.chat_message("assistant").write(msg.content)
    # We skip displaying ToolMessage directly to keep the chat clean

# User Input
if prompt := st.chat_input("Type your message here..."):
    # Display user message
    st.chat_message("user").write(prompt)
    
    # Add to state and invoke graph
    new_human_msg = HumanMessage(content=prompt)
    st.session_state.messages.append(new_human_msg)
    
    with st.spinner("Thinking..."):
        # We pass the full history to the graph so it remembers the context
        state = {"messages": st.session_state.messages}
        response_state = agent_graph.invoke(state)
        
        # Update session state with the new messages (including tool calls and AI responses)
        st.session_state.messages = response_state["messages"]
        
        # Display the final AI response
        final_ai_msg = response_state["messages"][-1]
        if final_ai_msg.content:
            st.chat_message("assistant").write(final_ai_msg.content)