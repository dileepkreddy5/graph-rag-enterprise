from graph_rag.core.llm.bedrock_client import BedrockClient


class GroundedGenerator:
    def __init__(self, llm_client: BedrockClient):
        self.llm = llm_client

    def build_prompt(self, query: str, retrieval_result: dict):

        graph_context = "\n".join(
            [str(path["nodes"]) for path in retrieval_result["graph_paths"]]
        )

        doc_context = "\n".join(
            [r["text"] for r in retrieval_result["ranked_results"]]
        )

        prompt = f"""
You are an AI assistant answering questions using ONLY the provided evidence.

User Question:
{query}

Knowledge Graph Evidence:
{graph_context}

Retrieved Document Evidence:
{doc_context}

Instructions:
- Use only the evidence provided.
- If the answer cannot be determined, say "I don't know."
- Be concise and factual.
"""

        return prompt

    def generate_answer(self, query: str, retrieval_result: dict):

        prompt = self.build_prompt(query, retrieval_result)
        answer = self.llm.generate(prompt)

        return answer
