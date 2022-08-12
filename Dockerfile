FROM huggingface/transformers-gpu:latest

WORKDIR /app

COPY requirements.txt /app/requirements.txt
RUN pip install -r /app/requirements.txt

COPY ./src /app/src

# for FastAPI
ENV LC_ALL=C.UTF-8
ENV LANG=C.UTF-8

# this step takes a few mins, so we'd want to incur the time-cost during docker-build time, rather than during runtime when the container starts
RUN python3 /app/src/download_models.py

EXPOSE 80

# start FastAPI server
CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "80"]
