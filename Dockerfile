FROM python:3.12
WORKDIR /app
COPY . .
RUN pip install --no-cache-dir openenv-core fastapi uvicorn pydantic requests openai
EXPOSE 7860
CMD ["uvicorn", "server.app:app", "--host", "0.0.0.0", "--port", "7860"]