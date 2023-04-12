FROM python:3.9-slim

COPY Push2Sharepoint.py /action/

RUN pip install Office365-REST-Python-Client

ENTRYPOINT ["python", "/action/Push2Sharepoint.py"]
