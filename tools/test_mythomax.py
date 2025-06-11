from llama_cpp import Llama

# Model path — update this to your Mythomax model location
model_path = "C:/Users/cnorthington/JUDY_AI/models/mythomax-l2-13b.Q6_K.gguf"

llm = Llama(model_path=model_path)

def mythomax_infer(user_message):
    response = llm(
        user_message,
        max_tokens=128,
        stop=["\n"]
    )
    return response['choices'][0]['text'].strip()

if __name__ == "__main__":
    print("Starting Mythomax test. Type 'exit' to quit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["exit", "quit"]:
            break
        reply = mythomax_infer(user_input)
        print(f"Judy: {reply}")
