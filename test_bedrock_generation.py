from graph_rag.core.llm.bedrock_client import BedrockClient
from graph_rag.core.llm.grounded_generator import GroundedGenerator
import json

# Simulated retrieval result
retrieval_result = {
    "graph_paths": [
        {"nodes": ["Amazon Neptune", "Bedrock"]},
    ],
    "ranked_results": [
        {
            "text": "Amazon Neptune integrates with Bedrock for AI applications."
        }
    ]
}

query = "How does Amazon Neptune integrate with Bedrock?"

llm = BedrockClient()
generator = GroundedGenerator(llm)

answer = generator.generate_answer(query, retrieval_result)

print("\nClaude Answer:\n")
print(answer)
