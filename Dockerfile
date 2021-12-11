FROM python:3.7-slim
COPY . /app
WORKDIR /app
COPY requirements.txt ./requirements.txt
RUN pip install pipenv
RUN pipenv install
RUN pip install -r requirements.txt
EXPOSE 12345
CMD ["pipenv", "run", "python", "app.py"]