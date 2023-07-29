```markdown
# daily_task_manager

`daily_task_manager` is a Python package that helps you manage your daily tasks at work. It provides a command-line interface (CLI) with various functionalities to add, display, search, and delete tasks, calculate total duration, and export the tasks to a CSV file.

## Installation

You can install `daily_task_manager` using `pip`:

```bash
pip install daily-task-manager
```

## Usage

After installation, you can use the `daily_task_manager` command to interact with the package. Here are the available options:

1. **Add Task:** Allows you to add a new task to the timesheet.

2. **Display Task History:** Displays all the tasks in the timesheet in a tabular format.

3. **Search Tasks:** Searches for tasks based on the provided search criteria (Project Name or Date).

4. **Delete a Task:** Deletes a task from the timesheet based on the date and project name.

5. **Calculate Total Duration:** Calculates and displays the total duration of all tasks in the timesheet.

6. **Export to CSV:** Exports the entire timesheet to a CSV file.

7. **Exit:** Exits the Daily Task Manager application.

To run the package, simply execute the `daily_task_manager` command in your terminal:

```bash
daily_task_manager
```

### Input Validation

The package enforces mandatory fields and performs input validation to ensure correct data entry. When adding a task, the following fields are mandatory:

- Project Name: A non-empty project name is required.
- Task: A non-empty task description is required.
- Duration: A positive integer (duration in minutes) is required.
- Date: A valid date in the format 'YYYY-MM-DD' is required.

### Dependencies

The package relies on the `tabulate` library to display tasks in a tabular format.

## Development

To contribute to this project or view the source code, visit the GitHub repository: [https://github.com/sanket-parte/daily-task-manager](https://github.com/sanket-parte/daily-task-manager)

### Package Structure

The `daily_task_manager` package has the following structure:

```
daily_task_manager/
├── daily_task_manager/
│   ├── __init__.py
│   ├── script.py
├── setup.py
├── README.md
├── MANIFEST.in (optional)
```

- The `daily_task_manager` directory is the main package containing the `script.py` file and the package's initialization file `__init__.py`.

- The `script.py` file contains the main functionality of the package, including the CLI and the tasks management functions.

### Example CSV Files

The package organizes task data into month-wise CSV files. These CSV files are stored in the `task_data` folder. Each CSV file contains tasks recorded for that specific month.