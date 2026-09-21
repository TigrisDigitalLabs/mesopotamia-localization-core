import time
import random
from typing import List, Dict, Any

class SystemPerformanceMonitor:
    """
    Automated network performance analyzer tracking operational availability,
    latency anomalies, and runtime verification protocols for system endpoints.
    """
    def __init__(self, endpoints: List[str]):
        self.endpoints = endpoints
        self.telemetry_archive: Dict[str, List[Dict[str, Any]]] = {url: [] for url in endpoints}

    def execute_ping_cycle(self, iterations: int = 5) -> None:
        print(f"[MONITOR] Initializing latency telemetry across {len(self.endpoints)} target clusters.")
        
        for cycle in range(1, iterations + 1):
            for node in self.endpoints:
                simulated_latency = round(random.uniform(12.4, 345.8), 2)
                is_operational = simulated_latency < 300.0
                status_node = "ONLINE" if is_operational else "DEGRADED"
                
                metrics_payload = {
                    "cycle_id": cycle,
                    "response_time_ms": simulated_latency,
                    "operational_integrity": status_node,
                    "execution_timestamp": time.time()
                }
                self.telemetry_archive[node].append(metrics_payload)
            time.sleep(0.1)

    def evaluate_system_health(self) -> Dict[str, Any]:
        global_summary = {}
        for node, logs in self.telemetry_archive.items():
            latencies = [log["response_time_ms"] for log in logs]
            average_speed = round(sum(latencies) / len(latencies), 2)
            failures = sum(1 for log in logs if log["operational_integrity"] == "DEGRADED")
            
            global_summary[node] = {
                "mean_latency_ms": average_speed,
                "packet_anomalies": failures,
                "node_rating": "STABLE" if failures == 0 else "ATTENTION_REQUIRED"
            }
        return global_summary

if __name__ == "__main__":
    monitored_nodes = [
        "https://mesopotamia-core.org",
        "https://mesopotamia-core.org",
        "https://mesopotamia-core.org"
    ]
    
    analyzer = SystemPerformanceMonitor(monitored_nodes)
    analyzer.execute_ping_cycle(iterations=3)
    health_matrix = analyzer.evaluate_system_health()
    
    print("\n=== SYSTEM ARCHITECTURE HEALTH REPORT ===")
    for endpoint, metrics in health_matrix.items():
        print(f"Node: {endpoint}")
        print(f" -> Latency Profile: {metrics['mean_latency_ms']} ms")
        print(f" -> Status Vector: {metrics['node_rating']}\n")
