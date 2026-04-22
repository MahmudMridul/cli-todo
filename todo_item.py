import uuid

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
