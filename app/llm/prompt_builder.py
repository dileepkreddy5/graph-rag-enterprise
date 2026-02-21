def build_prompt(query, graph_context, vector_context):
    graph_text = ", ".join(graph_context)

    vector_text = "\n".join([item["text"] for item in vector_context])

    prompt = f"""
You are an AI assistant answering questions using structured knowledge graph context
and semantic document retrieval.

User Question:
{query}

Knowledge Graph Context:
{graph_text}

Retrieved Document Context:
{vector_text}

Instructions:
- Use only the provided context.
- Be precise and factual.
- If unsure, say you don't know.

Answer:
"""
    return prompt
