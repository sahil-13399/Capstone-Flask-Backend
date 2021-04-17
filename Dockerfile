FROM python:3.7.2-slim
COPY . /Capstone_Flask
WORKDIR /Capstone_Flask
RUN pip3 install --upgrade pip setuptools wheel
RUN pip3 install -r requirements.txt
EXPOSE 5000
ENTRYPOINT [ "python3" ]
CMD [ "app.py" ]