from pathlib import Path
import json
import uuid

file_path = Path("data.json")

class TodoItem:
    def __init__(self, title: str, description: str = "", status: str = "todo"):
        self.id = str(uuid.uuid7())
        self.title = title
        self.description = description
        self.status = status

    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "status": self.status
        }

def display_todo_item(todo: TodoItem):
    print(f"ID: {todo['id']}")
    print(f"Title: {todo['title']}")
    print(f"Description: {todo['description']}")
    print(f"Status: {todo['status']}")
    print("-" * 20)

def display_todo_list(todos: list[TodoItem]):
    if not todos:
        print("No items found.")
        return

    for todo in todos:
        display_todo_item(todo)

def add_todo(title: str, description: str, status:str = "todo"):
    if title:
        item = TodoItem(title, description, status)
        
        with open(file_path, "r", encoding="utf-8") as f:
            todos = json.load(f)
        
        todos.append(item.to_dict())

        with open(file_path, "w", encoding="utf-8") as f:
            json.dump(todos, f, indent=4, ensure_ascii=False)


def main():
    if not file_path.is_file():
        print("data.json not found. Creating data.json...")

        with open(file_path, "w", encoding="utf-8") as f:
            # ensure_ascii=False to allow non-ASCII characters to be written properly
            json.dump([], f, indent=4, ensure_ascii=False)
    else:
        print("Todo List:")
        with open(file_path, "r", encoding="utf-8") as f:
            todos = json.load(f)
            display_todo_list(todos)
        terminate = False
        while not terminate:
            user_input = input("Enter 'add' to add a new todo item or 'exit' to quit: ").lower()
            if user_input == "exit":
                terminate = True
                print("Exiting...")
            elif user_input == "add":
                new_item = input("Enter Title and Description separated by | e.g. first item title|first item description:\n")
                title_description = new_item.split(sep="|")
                add_todo(title=title_description[0], description=title_description[1], status="todo")



if __name__ == "__main__":
    main()