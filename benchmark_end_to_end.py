import time
import statistics
from build_engine import build_engine
from graph_rag.core.llm.bedrock_client import BedrockClient
from graph_rag.core.llm.grounded_generator import GroundedGenerator


def percentile(data, p):
    sorted_data = sorted(data)
    k = int(len(sorted_data) * p / 100)
    return sorted_data[min(k, len(sorted_data) - 1)]


def run_benchmark():

    engine, query, entities = build_engine()

    llm = BedrockClient()
    generator = GroundedGenerator(llm)

    runs = 8
    total_latencies = []
    retrieval_latencies = []
    generation_latencies = []

    print("Running end-to-end benchmark...\n")

    for i in range(runs):

        start_total = time.time()

        # Retrieval phase
        start_retrieval = time.time()
        retrieval_result = engine.retrieve(query, entities)
        retrieval_ms = retrieval_result["latency"]["total_ms"]
        retrieval_latencies.append(retrieval_ms)

        # Generation phase
        start_generation = time.time()
        generator.generate_answer(query, retrieval_result)
        generation_ms = (time.time() - start_generation) * 1000
        generation_latencies.append(generation_ms)

        total_ms = (time.time() - start_total) * 1000
        total_latencies.append(total_ms)

        print(
            f"Run {i+1}: "
            f"Retrieval={retrieval_ms:.2f} ms | "
            f"Generation={generation_ms:.2f} ms | "
            f"Total={total_ms:.2f} ms"
        )

    # Remove first 2 warmup runs
    total_latencies = total_latencies[2:]
    retrieval_latencies = retrieval_latencies[2:]
    generation_latencies = generation_latencies[2:]

    print("\n=== End-to-End Performance Summary ===")

    print("\nRetrieval:")
    print(f"Mean: {statistics.mean(retrieval_latencies):.2f} ms")
    print(f"P95: {percentile(retrieval_latencies, 95):.2f} ms")

    print("\nGeneration (Claude):")
    print(f"Mean: {statistics.mean(generation_latencies):.2f} ms")
    print(f"P95: {percentile(generation_latencies, 95):.2f} ms")

    print("\nTotal End-to-End:")
    print(f"Mean: {statistics.mean(total_latencies):.2f} ms")
    print(f"P95: {percentile(total_latencies, 95):.2f} ms")


if __name__ == "__main__":
    run_benchmark()
