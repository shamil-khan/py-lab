# Python Py-Lab (Podman + uv)

A lightweight, containerized environment for practicing Python using **Podman** to keep the host machine clean and **uv** for lightning-fast package management.

## 🚀 Setup

1. **Build the image:**
```bash
podman build -t py-lab-base .
```

2. **Start the container:**
Mounts your current directory to /app so code changes persist
```bash
podman run -it --rm --name py-lab -v .:/app:Z py-lab-base bash
```

## 📦 Install
Use uv to manage your libraries inside the container:
```bash
# Initialize a new project (if needed)
uv init

# Add a library (e.g., requests)
uv add requests

# Synchronize dependencies
uv sync
```

## 📝 Saving Commands

Keep a log of commands you learn here:

- uv add [package] — Adds a dependency to pyproject.toml.

- uv run [script.py] — Runs a script within the managed environment.

- uv lock — Updates the lockfile.


## ▶️ Run
Execute your practice scripts using uv:
```bash
python main.py

# OR
uv run main.py
```


