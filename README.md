📈 Sample Output

Below is an example of structured, explainable output returned by the Hybrid Retrieval Engine:

{
    "query": "How does Amazon Neptune integrate with Bedrock?",
    "entities": [
        "Amazon Neptune",
        "Bedrock"
    ],
    "top_result": {
        "text": "Amazon Neptune integrates with Bedrock for AI applications.",
        "vector_score": 0.0,
        "graph_score": 1.0,
        "final_score": 0.4
    },
    "confidence": 0.4,
    "latency": {
        "total_ms": 42.82,
        "graph_ms": 18.75,
        "vector_ms": 24.05,
        "ranking_ms": 0.02
    },
    "graph_paths": [
        {
            "nodes": ["Amazon Neptune", "Amazon Bedrock"],
            "hop_count": 1,
            "score": 1.0
        },
        {
            "nodes": ["Amazon Neptune", "Bedrock"],
            "hop_count": 1,
            "score": 1.0
        }
    ]
}
🔎 What This Demonstrates

• Explicit reasoning paths (multi-hop graph expansion)
• Hybrid ranking transparency (graph + semantic scores)
• Confidence calibration
• Stage-wise latency instrumentation
• Structured output suitable for production APIs

This design ensures explainability, debuggability, and measurable retrieval quality — beyond standard RAG  implementations.
