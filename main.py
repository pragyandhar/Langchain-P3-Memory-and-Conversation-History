from chain import build_chain
import uuid

def main():
    print("======= Personal Assistant with Memory =======")
    print("---- Type 'exit' to quit ----")

    chain = build_chain() # 1. Build your chain

    session_id = str(uuid.uuid4())

    while True:
        user_input = input("You: ").strip()

        if user_input.lower() == "exit":
            print("Goodbye!")
            break
        
        response = chain.invoke(
            {"input": user_input},
            config={"configurable": {"session_id": session_id}}
        )

        print(f"Assistant: {response}")



if __name__ == "__main__":
    main()
