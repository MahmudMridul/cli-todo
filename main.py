from pathlib import Path
import json
import uuid

file_path = Path("data.json")

class TodoItem:
    def __init__(self, title: str, description: str = "", completed: bool = False):
        self.id = str(uuid.uuid7())
        self.title = title
        self.description = description
        self.completed = completed

def main():
    if not file_path.is_file():
        print("data.json not found. Creating data.json...")

        with open(file_path, "w", encoding="utf-8") as f:
            # ensure_ascii=False to allow non-ASCII characters to be written properly
            json.dump({}, f, indent=4, ensure_ascii=False)
    else:
        while True:
            print("Showing todo list:")


if __name__ == "__main__":
    main()