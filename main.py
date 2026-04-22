from pathlib import Path
import json
from todo_item import TodoItem

file_path = Path("data.json")


def get_todos_from_json() -> list:
    with open(file_path, "r", encoding="utf-8") as file:
        todos = json.load(file)
    return todos

def write_todos_to_json(todos: list):
    with open(file_path, "w", encoding="utf-8") as file:
        json.dump(todos, file, indent=4, ensure_ascii=False)

def display_todo_item(todo: TodoItem):
    print(f"ID: {todo['id']}")
    print(f"Title: {todo['title']}")
    print(f"Description: {todo['description']}")
    print(f"Status: {todo['status']}")
    print("-" * 20 + "\n")

def display_todo_list(todos: list[TodoItem]):
    if not todos:
        print("No items found.\n")
        return

    for todo in todos:
        display_todo_item(todo)

def add_todo(title: str, description: str, status:str = "todo"):
    if title:
        item = TodoItem(title, description, status)
        
        todos = get_todos_from_json()
        
        todos.append(item.to_dict())

        write_todos_to_json(todos)

        print("Added successfully!\n")
    else:
        print("Title is required\n")

def update_todo(id: str, title: str, description: str, status: str):
    if id and title:
        todos = get_todos_from_json()
        found = False
        for item in todos:
            if id == item['id']:
                if title is not None:
                    item['title'] = title
                if description is not None:
                    item['description'] = description
                if status is not None:
                    item['status'] = status
                found = True
                break
        
        if not found:
            print(f"No item found with ID: {id}\n")
            return
        
        write_todos_to_json(todos)

        print("Updated successfully!\n")
    else:
        print("ID and Title are required\n")



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
            user_input = input("Enter 'add' to add a new todo item\n'update' to edit existing item\n'list' to see items\n'exit' to quit:\n").lower()
            
            if user_input == "exit":
                terminate = True
                print("Exiting...")
            elif user_input == "list":
                todos = get_todos_from_json()
                display_todo_list(todos)

            elif user_input == "add":
                new_item = input("Enter Title and Description separated by | e.g. first item title|first item description:\n")
                title_description = new_item.split(sep="|")
                add_todo(title=title_description[0], description=title_description[1], status="todo")

            elif user_input == "update":
                item = input("Enter ID, Title, Description and Status separated by | e.g. 1234|first item title|first item description|in progress:\n")
                todo_array = item.split(sep="|")
                update_todo(
                    id=todo_array[0],
                    title=todo_array[1],
                    description=todo_array[2],
                    status=todo_array[3]
                )



if __name__ == "__main__":
    main()