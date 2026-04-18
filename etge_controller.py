import os, sys, json, argparse
from datetime import datetime, timezone

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--archive-root", default="/tmp/etge_archive")
    args = parser.parse_args()

    os.makedirs(args.archive_root, exist_ok=True)
    print(f"[ETGE] Controller initialized at {datetime.now(timezone.utc).isoformat()}")
    print(f"[ETGE] Archive root set to: {args.archive_root}")
    
    # Generate minimal metadata artifact for the runner
    meta_path = os.path.join(args.archive_root, 'triage_metadata.json')
    with open(meta_path, 'w') as f:
        json.dump({"status": "initialized", "runner": "github_actions"}, f)
    
    print(f"[ETGE] Process complete. Artifacts stored in {args.archive_root}")

if __name__ == '__main__':
    main()
