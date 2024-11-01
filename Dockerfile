ARG PYTHON_VERSION=3.12
FROM python:${PYTHON_VERSION}

RUN apt-get update && apt-get install -y python3-virtualenv

RUN mkdir /Packages

COPY requirements-dev.txt requirements.txt /Packages/

WORKDIR /Packages

RUN pip install --no-cache -r requirements-dev.txt

COPY . /workspace

WORKDIR /workspace

CMD [ "/bin/bash" ]
