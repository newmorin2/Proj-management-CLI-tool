from models.user import User
from models.project import Project
from models.task import Task


def test_user_creation():
    user = User("John", "john@example.com")
    assert user.name == "John"
    assert user.email == "john@example.com"
    assert isinstance(user.projects, list)


def test_add_project_to_user():
    user = User("John", "john@example.com")
    project = Project("App", "Build app", "2026-09-01")

    user.add_project(project)

    assert len(user.projects) == 1
    assert user.projects[0].title == "App"


def test_project_add_task():
    project = Project("App", "Build app", "2026-09-01")
    task = Task("Login page", "John")

    project.add_task(task)

    assert len(project.tasks) == 1
    assert project.tasks[0].title == "Login page"


def test_task_complete():
    task = Task("Login page", "John")
    task.mark_complete()

    assert task.status == "Complete"