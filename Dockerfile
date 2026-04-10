# Dockerfile
FROM python:3.12-slim
WORKDIR /app
RUN pip install --no-cache-dir uv
# Pre-install core langchain packages to save time during practice
RUN uv pip install --system langchain langchain-openai langchain_community redis
RUN uv pip install --system beautifulsoup4 requests
RUN uv pip install --system pypdf
