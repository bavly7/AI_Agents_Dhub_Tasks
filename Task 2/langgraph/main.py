from agent.graph import graph_app

def main():
    print("==================================================")
    print("🤖 Custom LangGraph Agent is Ready! (Type 'exit' to quit)")
    print("==================================================\n")

    while True:
        # 1. استقبال طلب المستخدم
        user_input = option = input("👤 You: ")
        
        # 2. أمر الخروج من البرنامج
        if user_input.lower() in ['exit', 'quit']:
            print("\n🤖 Agent: Goodbye! Have a great day.")
            break
            
        if not user_input.strip():
            continue
            
        try:
            print("\n⏳ Thinking and processing...")
            

            result = graph_app.invoke({"messages": [("user", user_input)]})
            

            final_response = result['messages'][-1].content
            if hasattr(final_response, "content"):
                response_content = final_response.content
            elif isinstance(final_response, dict):
                response_content = final_response.get("content", str(final_response))
            else:
                response_content = str(final_response)
            print("\n" + "="*50)
            print("🤖 Agent Response:")
            print("="*50)
            print(response_content)
            print("="*50 + "\n")
            
        except Exception as e:
            print(f"\n⚠️ System Error: {str(e)}\n")

if __name__ == "__main__":
    main()