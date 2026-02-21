from transformers import pipeline


class LocalLLM:
    def __init__(self):
        self.generator = pipeline("text-generation", model="microsoft/phi-2")

    def generate(self, prompt):
        result = self.generator(prompt, max_new_tokens=200, do_sample=False)
        return result[0]["generated_text"]
