## Project Management Tool

### A command-line project management system for managing users, projects, and tasks using Python OOP, JSON storage, and argparse-based CLI commands

### Features

    -Create and manage users
    -Assign projects to users
    -Add tasks to projects
    -Mark tasks as complete
    -Persistent storage using JSON files
    -Command-line interface using argparse
    -Object-oriented design with relationships:
    -User → Projects (one-to-many)
    -Project → Tasks (one-to-many)

### Project Structure

```sh
project/
│
├── main.py
├── requirements.txt
│
├── models/
│   ├── person.py
│   ├── user.py
│   ├── project.py
│   └── task.py
│
├── utils/
│   └── storage.py
│
├── data/
│   ├── users.json
│   ├── projects.json
│   └── tasks.json
│
└── README.md
```

### Setup Instructions

1. **Clone the repository:**

    ```sh
    ❯ git clone https://github.com/newmorin2/proj-management-CLI-tool
    ```

2. **Navigate to the project directory:**

    ```sh
    ❯ cd PYTHON-SUMMATIVE-CLI-LAB
    ```

3. **Create virtual environment:**

python -m venv venv
source venv/bin/activate   # Mac/Linux
venv\Scripts\activate      # Windows

4. **Install dependencies:**
    ```sh
       ❯ pip install -r requirements.txt
    ```

### How to run the CLI tool
- Run all commands using:
```sh
    python main.py <command> [arguments]
```
- Example:
```sh
    python main.py add-user "John Doe" john@example.com
```

### Known issues/limitations

    -No authentication or user login system
    -No database integration (uses local JSON files only)
    -IDs are auto-incremented per session (may reset if JSON is cleared)
    -No validation for duplicate emails or names
    -Task-to-project and project-to-user relationships are stored via IDs only (not fully relational enforcement)

### Contributing
- Newton Mwangi