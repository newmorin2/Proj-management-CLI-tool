class Task:
    id_counter = 1

    def __init__(self, title, assigned_to):
        self.id = Task.id_counter
        Task.id_counter += 1

        self.title = title
        self.assigned_to = assigned_to
        self.status = "Pending"

    def mark_complete(self):
        self.status = "Complete"

    def __str__(self):
        return (
            f"Task {self.id}: {self.title} | "
            f"Assigned To: {self.assigned_to} | "
            f"Status: {self.status}"
        )
    
    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "assigned_to": self.assigned_to,
            "status": self.status
    }

    @classmethod
    def from_dict(cls, data):
        user = cls(data["name"], data["email"])
        user.id = data["id"]
        return user