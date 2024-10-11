FROM python:3.10-slim
RUN mkdir /app
WORKDIR /app
COPY . .
RUN pip install Flask
EXPOSE 5000
CMD [ "python","app.py" ]