FROM python:3.10-slim

RUN mkdir -p /app
COPY ./model.py /app/
COPY ./maint.pickle4 /app/
COPY ./requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt
WORKDIR /app
EXPOSE 8080
CMD [ "model.py" ]
ENTRYPOINT [ "python" ]