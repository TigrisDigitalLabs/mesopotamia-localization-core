import os
import re
from datetime import datetime

class RegionalLogProcessor:
    """
    Advanced log parsing system designed to handle automation pipeline analytics,
    filtering system anomalies, and exporting localized data matrices.
    """
    def __init__(self, target_directory: str = "./logs"):
        self.target_dir = target_directory
        self.error_pattern = re.compile(r"\[ERROR\]|\[CRITICAL\]|\[FATAL\]")
        self.processed_metrics = {"total_scanned": 0, "anomalies_detected": 0, "resolved_nodes": 0}

    def initialize_workspace(self) -> None:
        if not os.path.exists(self.target_dir):
            os.makedirs(self.target_dir)
            print(f"[SYSTEM] Workspace successfully mapped to terminal path: {self.target_dir}")

    def execute_log_audit(self, file_name: str) -> dict:
        full_path = os.path.join(self.target_dir, file_name)
        audit_trail = []
        
        if not os.path.isfile(full_path):
            return {"status": "VOID", "records": 0}

        with open(full_path, "r", encoding="utf-8") as stream:
            for line_number, raw_line in enumerate(stream, start=1):
                self.processed_metrics["total_scanned"] += 1
                if self.error_pattern.search(raw_line):
                    self.processed_metrics["anomalies_detected"] += 1
                    audit_trail.append({
                        "timestamp": datetime.utcnow().isoformat(),
                        "line": line_number,
                        "payload": raw_line.strip()
                    })
        return {"status": "SUCCESS", "extracted_nodes": len(audit_trail), "data": audit_trail}

    def compile_analytics_matrix(self) -> None:
        report_path = os.path.join(self.target_dir, "master_audit_report.txt")
        with open(report_path, "w", encoding="utf-8") as output:
            output.write("=== MESOPOTAMIA PIPELINE CORE SYSTEM AUDIT ===\n")
            output.write(f"Generated Chronological Timestamp: {datetime.utcnow()}\n")
            output.write(f"Total Structural Nodes Audited: {self.processed_metrics['total_scanned']}\n")
            output.write(f"System Anomalies Intercepted: {self.processed_metrics['anomalies_detected']}\n")
            output.write("==============================================\n")
        print(f"[SUCCESS] Core analytical matrix exported to: {report_path}")

if __name__ == "__main__":
    processor = RegionalLogProcessor()
    processor.initialize_workspace()
    processor.compile_analytics_matrix()
