import time
import statistics
from build_engine import build_engine

def percentile(data, p):
    sorted_data = sorted(data)
    k = int(len(sorted_data) * p / 100)
    return sorted_data[min(k, len(sorted_data) - 1)]


def run_benchmark():
    engine, query, entities = build_engine()

    runs = 20
    latencies = []

    print("Running retrieval benchmark...\n")

    for i in range(runs):
        result = engine.retrieve(query, entities)
        latencies.append(result["latency"]["total_ms"])
        print(f"Run {i+1}: {result['latency']['total_ms']} ms")

    # Remove first 3 runs (warm-up)
    latencies = latencies[3:]

    print("\n=== Retrieval Performance Summary ===")
    print(f"Mean Latency: {statistics.mean(latencies):.2f} ms")
    print(f"Median Latency: {statistics.median(latencies):.2f} ms")
    print(f"P95 Latency: {percentile(latencies, 95):.2f} ms")
    print(f"Min Latency: {min(latencies):.2f} ms")
    print(f"Max Latency: {max(latencies):.2f} ms")


if __name__ == "__main__":
    run_benchmark()
