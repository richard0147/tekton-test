# Base image from internal Harbor (mirrors docker.io/library/python)
FROM harbor-sh.haivivi.cn/library/python:3.12-slim

WORKDIR /app

COPY app.py .

ENV PORT=8080
EXPOSE 8080

USER nobody

CMD ["python", "-u", "app.py"]
