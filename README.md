# 🚀 Enterprise Hybrid Graph-RAG System

An enterprise-grade Hybrid Retrieval-Augmented Generation (Graph-RAG) system combining multi-hop knowledge graph reasoning, semantic vector retrieval, weighted ranking, evaluation metrics, latency instrumentation, and Amazon Bedrock Claude integration.

This project focuses on system design, explainability, evaluation rigor, and production readiness — moving beyond traditional vector-only RAG pipelines.

---

## 🧠 Architecture Overview

This system integrates:

- Multi-hop Knowledge Graph reasoning (Amazon Neptune compatible)
- FAISS-based semantic vector retrieval
- Weighted hybrid ranking (graph + semantic scoring)
- Confidence calibration
- Retrieval evaluation metrics
- Latency instrumentation (stage-wise breakdown)
- Amazon Bedrock Claude 3 for grounded answer synthesis
- Modular domain-driven architecture

---

## 🧠 End-to-End Pipeline

```text
User Query
    ↓
Entity Extraction
    ↓
Multi-Hop Graph Expansion
    ↓
Vector Similarity Retrieval (FAISS)
    ↓
Hybrid Ranking (Graph + Semantic)
    ↓
Structured Prompt Construction
    ↓
Claude 3 (Amazon Bedrock)
    ↓
Grounded Answer
```

This architecture enforces separation between retrieval and generation while preserving explainability and observability.

---

## 🔥 LLM Integration (Amazon Bedrock)

The system integrates Amazon Bedrock (Claude 3 Sonnet) for grounded answer generation.

Key design principles:

- Evidence-constrained prompting
- Knowledge graph + document context injection
- Strict grounding instructions to reduce hallucination
- Retrieval → Generation separation
- Model-agnostic LLM abstraction layer

LLM calls are made via AWS Bedrock Runtime using `boto3`.

---

## 🔎 Hybrid Scoring Strategy

Final ranking score:

```
final_score =
    α * normalized_vector_score
  + β * graph_path_score
```

Graph scoring incorporates:

- Hop-based decay
- Path weighting
- Deduplicated reasoning paths
- Multi-entity expansion

This ensures structural reasoning complements semantic similarity.

---

## 📊 Retrieval Evaluation Framework

Implemented metrics:

- Precision@K
- Recall@K
- Mean Reciprocal Rank (MRR)
- Graph Coverage Score

This enables measurable retrieval quality rather than heuristic-only evaluation.

---

## ⚡ Latency Instrumentation

Stage-wise performance tracking:

- Graph expansion latency
- Vector search latency
- Ranking latency
- Total end-to-end latency

Example:

```json
"latency": {
  "total_ms": 42.82,
  "graph_ms": 18.75,
  "vector_ms": 24.05,
  "ranking_ms": 0.02
}
```

This enables observability and performance optimization.

---

## 📈 Sample Output

Below is an example of structured, explainable output returned by the Hybrid Retrieval Engine:

```json
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
```

### 🔎 What This Demonstrates

- Explicit reasoning paths (multi-hop graph expansion)
- Hybrid ranking transparency (graph + semantic scoring)
- Confidence calibration
- Stage-wise latency instrumentation
- Structured output suitable for production APIs
- Grounded answer generation using Bedrock Claude

This architecture prioritizes explainability, measurable retrieval quality, and performance observability.

---

## 🏗 Project Structure

```
graph_rag/
│
├── core/
│   ├── graph/
│   ├── vector/
│   ├── retrieval/
│   ├── ranking/
│   ├── llm/
│   └── evaluation/
│
├── ingestion/
├── config/
├── tests/
```

The system follows modular domain separation:

- Retrieval layer
- Ranking layer
- LLM layer
- Evaluation layer
- Observability layer

---

## 🛠 Technologies Used

- Python
- FAISS
- Amazon Neptune (Gremlin)
- AWS Bedrock
- Claude 3 Sonnet
- boto3
- Pydantic
- Docker-ready structure

---

## 🎯 Key Differentiators

Unlike standard RAG implementations, this system:

- Combines structured graph reasoning with semantic retrieval
- Produces explainable reasoning traces
- Implements measurable evaluation metrics
- Instruments latency across pipeline stages
- Separates retrieval from generation
- Integrates cloud-native LLM infrastructure

---

## 🚀 Future Enhancements

- FastAPI production API
- Docker containerization
- CI/CD pipeline
- Benchmark dataset integration
- Cost and token usage tracking
- Multi-model support abstraction

---

## 📌 About

Enterprise Hybrid Graph-RAG system with multi-hop reasoning, weighted hybrid ranking, evaluation metrics, latency instrumentation, and Amazon Bedrock Claude integration.
