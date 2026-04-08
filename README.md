# Python AI-Lab (Podman + uv + LM Studio)

A professional, lightweight containerized environment for practicing LangChain and LLM orchestration. This setup bridges local LLMs (via LM Studio) and cloud LLMs (OpenAI) while maintaining a clean host machine.

## 🏗️ Architecture

- **Python 3.12-slim**: Core runtime with `uv` for package management.

- **Redis 7-alpine**: Local vector/memory store.

- **LM Studio (Host)**: Runs local models (Granite-3B) via an 
OpenAI-compatible API.

- **Network**: Host-mode networking for seamless communication between container and host services.

## 🚀 Setup

1. **Build the image:**
    ```bash
    podman build -t py-lab-base .
    ```

2. **Configure Environment:**
Create a .env file in the root directory (sample including in the repo):
    ```text
    OPENAI_API_KEY=sk-your-key
    LM_STUDIO_URL=http://localhost:1234/v1
    REDIS_URL=redis://localhost:6379
    ```

3. **Start the Lab:**
    ```bash
    podman-compose up -d
    ```

4. **Enter the Lab:**
    ```bash
    podman exec -it py-lab_py-lab_1 bash
    ```

- **Start the container - (with out compose):**
Mounts your current directory to /app so code changes persist
    ```bash
    podman run -it --rm --name py-lab -v .:/app:Z py-lab-base bash
    ```
## 🤖 LLM Workflow

### Local LLM (LM Studio)

1. Open LM Studio on your host.

2. Load granite-3b-code-instruct-128k. **(see command)**

3. Go to Local Server -> Start Server (Ensure "Allow LAN Connections" is ON). **(see command)**

4. Podman Compose **(see command)**

5. Pod Bash **(see command)**

6. Run Python script **(see run)**

## Usage in Python
Both local and cloud models use the same langchain-openai library:
```python
from langchain_openai import ChatOpenAI

# Cloud GPT-5 Nano
gpt5 = ChatOpenAI(model="gpt-5-nano")

# Local Granite
granite = ChatOpenAI(
    base_url="http://localhost:1234/v1",
    api_key="lm-studio"
)
```

## 📦 Dependency Management

We use uv for high-performance package management inside the container:

```bash
# Add new libraries
uv pip install langchain-openai redis

# Run scripts
python hello-llm.py

```

## 📝 Commands & Troubleshooting

- **Start Service:** podman-compose up -d

- **Stop Services:** podman-compose down

- **Pod Bash:** podman exec -it <conatiner-name> bash

- **Verify Redis:** python ping-redis.py

- **Check Environment:** env | grep -E 'OPENAI|LM_STUDIO'

- **Networking:** Using network_mode: host allows the container to see LM Studio at localhost:1234.

- **LM Studio - Load/Unload Model:** lms load/unload <model-name>

- **LM Studio - Start/Stop Server:** lms start/stop server



## ▶️ Run
Execute your practice scripts using uv:
```bash
python main.py

# OR
uv run main.py
```


