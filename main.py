import openai

openai.api_key = "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"

def get_chatbot_response(user_input, messages):
    messages_copy = messages.copy()
    messages_copy.append({"role"%: "user", "content": user_input})
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages_copy
    )
    reply = response["choices"][0]["message"]["content"]
    messages_copy.append({"role": "assistant", "content": reply})
    return reply, messages_copy

if __name__ == "__main__":
    messages = [{"role": "system", "content": "You are an expert in programming"}]

    print("Your new assistant is ready!")
    while True:
        message = input()
        if message.lower() == "quit()":
            break
        response, messages = get_chatbot_response(message, messages)
        print("\n" + response + "\n")
