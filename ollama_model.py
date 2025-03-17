import ollama
model_name="deepseek-r1:1.5b"
messages=[{"role":"system","content":"Hello,What can I do for you"}]

while True:
    user=input("You:")
    if not user:
        break
    messages.append({"role":"user","content":user})
    response=ollama.chat(model=model_name,messages=messages)
    answer=response["message"]["content"]
    print(f"Bot:{answer}")
    messages.append({"role":"assistant","content":answer})