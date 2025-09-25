FROM python

WORKDIR /app

COPY requirements.txt ./
RUN pip install -r requirements.txt

COPY . .

EXPOSE 8000
CMD ["fastapi", "run", "main.py", "--host","0.0.0.0","--port","8000"]
