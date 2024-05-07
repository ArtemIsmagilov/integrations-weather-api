FROM python:bookworm
WORKDIR /app
COPY ./requirements.txt .
COPY ./.env .
COPY ./weather_api/ ./weather_api/
RUN  pip install --no-cache-dir -r requirements.txt
CMD ["uvicorn", "--factory", "weather_api.main:create_app", "--host", "0.0.0.0", "--port", "8000"]
EXPOSE 8000
