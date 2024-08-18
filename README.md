# VarSYNC

**VarSYNC** is a Python package for managing user-specific variables with a web interface. It allows users to create, read, update, and delete variables and provides a straightforward API for accessing these variables in Python.

## Features

- **User Registration & Authentication**: Register and log in users.
- **Variable Management**: Create, read, update, and delete user-specific variables.

## Installation

You can install `varsync` from PyPI using pip:

```bash
pip install varsync
```

## Usage

### Register a New User

```python
import varsync

# Register a new user
varsync.register(username="your_username", password="your_password", confirm_password="your_password")
```

### Login

```python
import varsync

# Log in
session = varsync.login(username="your_username", password="your_password")
```

### Variable Management

**Get Variable**

```python
# Get a variable value
value = session.get("variable_name")
print(value)  # Output: value or "Variable not set"
```

**Create Variable**

```python
# Create a new variable
session.create("variable_name", "variable_value")
```

**Edit Variable**

```python
# Edit an existing variable
session.edit("variable_name", "new_value")
```

**Delete Variable**

```python
# Delete a variable
session.delete("variable_name")
```

**List All Variables**

```python
# List all variables
variables = session.list()
print(variables)
```

## Contact

For any questions or support, please contact [sriharan2544@gmail.com](mailto:sriharan2544@gmail.com).

### Notes:

- `Features`: Lists key features of your package.
- `Installation`: Shows how to install the package.
- `Usage`: Provides examples of how to use the package.
- `Configuration`: Instructions to set up database credentials.
- `Contributing`: Guidelines for contributing to the project.
- `License`: Information about the project license.
- `Contact`: Your contact information for support or questions.
