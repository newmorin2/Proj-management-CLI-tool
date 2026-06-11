from models.user import User
from models.project import Project
from models.task import Task

user = User("Newton", "newton@example.com")

project = Project(
    "StudyLink",
    "Study group management system",
    "2026-09-01"
)

task = Task("Build Login Page", "Newton")

project.add_task(task)
user.add_project(project)

print(user)
print(project)
print(task)