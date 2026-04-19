from pathlib import Path
import json

file_path = Path("data.json")

def main():
    if not file_path.is_file():
        print("data.json not found. Creating data.json...")

        with open(file_path, "w", encoding="utf-8") as f:
            # ensure_ascii=False to allow non-ASCII characters to be written properly
            json.dump({}, f, indent=4, ensure_ascii=False)
    # while True:
    #     pass

if __name__ == "__main__":
    main()