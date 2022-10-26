FROM python
WORKDIR /app
COPY requerimientos.txt .
RUN pip install -r requerimientos.txt
COPY . .
CMD ["uvicorn", "--host", "0.0.0.0","main:app"]
EXPOSE 8000