import os
import json
import argparse
from pathlib import Path
from datetime import datetime, timezone

def main():
    parser = argparse.ArgumentParser(description="ETGE Research Orchestrator")
    parser.add_argument("--archive-root", required=True, help="Path to the artifact storage")
    args = parser.parse_args()

    # 1. Initialize environment
    archive_path = Path(args.archive_root)
    archive_path.mkdir(parents=True, exist_ok=True)
    print(f"[ETGE Controller] Initialized at {datetime.now(timezone.utc).isoformat()}")
    print(f"[ETGE Controller] Archive root: {archive_path.absolute()}")

    # 2. Orchestration Logic: Scan for division artifacts
    print("\n--- SCANNING FOR DIVISION STATUSES ---")
    found_artifacts = list(archive_path.rglob("*.json"))
    
    if not found_artifacts:
        print("No artifacts found yet. Waiting for pipeline execution.")
    else:
        for art_path in found_artifacts:
            try:
                with open(art_path, 'r') as f:
                    data = json.load(f)
                division = data.get('division', 'Unknown')
                status = data.get('status', 'PENDING')
                review_req = data.get('HUMAN_REVIEW_REQUIRED', True)
                print(f"Division: {division:<20} | Status: {status} | Review Needed: {review_req}")
            except Exception as e:
                print(f"Error reading {art_path.name}: {e}")

    # 3. Finalization
    print("\n[ETGE Controller] Orchestration cycle complete.")

if __name__ == '__main__':
    main()
