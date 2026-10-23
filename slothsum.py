!pip install -q ollama
import ollama
prompt = "You are a lazy sloth. Summarize this in exactly two short sentences:\n\n"
text = input("Paste long text: ")
r = ollama.chat(model="gemma3:1b", messages=[{"role": "user", "content": prompt + text}])
print("🦥", r["message"]["content"])
