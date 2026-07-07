import ollama

response = ollama.chat(
    model="tinyllama",
    messages=[{"role": "user", "content": "Explain panic disorder symptoms"}]
)

print(response["message"]["content"])