# Full env and program
FROM python:3.6-alpine
WORKDIR /app
COPY . .
RUN pip install --no-cache-dir -r requirements.txt
EXPOSE 9000
CMD python main.py