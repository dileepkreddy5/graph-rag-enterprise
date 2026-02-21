from graph_rag.core.evaluation.retrieval_metrics import RetrievalMetrics

# Simulated retrieved docs
retrieved = [
    "Amazon Neptune integrates with Bedrock for AI applications.",
    "Amazon Bedrock provides foundation models.",
]

# Simulated ground truth
relevant = ["Amazon Neptune integrates with Bedrock for AI applications."]

metrics = RetrievalMetrics()

precision = metrics.precision_at_k(relevant, retrieved, k=2)
recall = metrics.recall_at_k(relevant, retrieved, k=2)
mrr = metrics.mean_reciprocal_rank(relevant, retrieved)

print("\nEvaluation Metrics:")
print("Precision@2:", precision)
print("Recall@2:", recall)
print("MRR:", mrr)
