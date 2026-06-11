import argparse

from models.user import User
from models.project import Project
from models.task import Task

from utils.storage import load_data, save_data

USERS_FILE = "data/users.json"
PROJECTS_FILE = "data/projects.json"
TASKS_FILE = "data/tasks.json"

def get_users():
    return load_data(USERS_FILE)


def get_projects():
    return load_data(PROJECTS_FILE)


def get_tasks():
    return load_data(TASKS_FILE)

def add_user(args):
    users = get_users()

    user = User(args.name, args.email)
    users.append(user.to_dict())

    save_data(USERS_FILE, users)

    print(f"User added: {user}")

def list_users(args):
    users = get_users()

    if not users:
        print("No users found")
        return

    for u in users:
        print(f"{u['id']} - {u['name']} ({u['email']})")

def add_project(args):
    projects = get_projects()

    project = Project(args.title, args.description, args.due_date)
    project_data = project.to_dict()
    project_data["user_id"] = args.user_id

    projects.append(project_data)

    save_data(PROJECTS_FILE, projects)

    print(f"Project added: {project}")

def list_projects(args):
    projects = get_projects()

    if not projects:
        print("No projects found")
        return

    for p in projects:
        print(f"{p['id']} - {p['title']} (Due: {p['due_date']})")

def add_task(args):
    tasks = get_tasks()

    task = Task(args.title, args.assigned_to)
    task_data = task.to_dict()
    task_data["project_id"] = args.project_id

    tasks.append(task_data)

    save_data(TASKS_FILE, tasks)

    print(f"Task added: {task}")

def complete_task(args):
    tasks = get_tasks()

    for t in tasks:
        if t["id"] == args.task_id:
            t["status"] = "Complete"

    save_data(TASKS_FILE, tasks)

    print(f"Task {args.task_id} marked as complete")

def main():
    parser = argparse.ArgumentParser(description="Project Management Tool")

    subparsers = parser.add_subparsers(dest="command")

    # add-user
    user_parser = subparsers.add_parser("add-user")
    user_parser.add_argument("name")
    user_parser.add_argument("email")
    user_parser.set_defaults(func=add_user)

    # list-users
    list_users_parser = subparsers.add_parser("list-users")
    list_users_parser.set_defaults(func=list_users)

    # add-project
    project_parser = subparsers.add_parser("add-project")
    project_parser.add_argument("user_id", type=int)
    project_parser.add_argument("title")
    project_parser.add_argument("description")
    project_parser.add_argument("due_date")
    project_parser.set_defaults(func=add_project)

    # list-projects
    list_projects_parser = subparsers.add_parser("list-projects")
    list_projects_parser.set_defaults(func=list_projects)

    # add-task
    task_parser = subparsers.add_parser("add-task")
    task_parser.add_argument("project_id", type=int)
    task_parser.add_argument("title")
    task_parser.add_argument("assigned_to")
    task_parser.set_defaults(func=add_task)

    # complete-task
    complete_parser = subparsers.add_parser("complete-task")
    complete_parser.add_argument("task_id", type=int)
    complete_parser.set_defaults(func=complete_task)

    args = parser.parse_args()

    if hasattr(args, "func"):
        args.func(args)
    else:
        parser.print_help()


if __name__ == "__main__":
    main()