FROM python:3.10.7

COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt

VOLUME /app
EXPOSE 5000
ENTRYPOINT [ "python" ]
CMD [ "sources/app.py" ]