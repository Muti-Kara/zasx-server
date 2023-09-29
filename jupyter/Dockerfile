FROM nvcr.io/nvidia/pytorch:23.03-py3

COPY venvs.yml /opt/venvs.yml
COPY create_venvs.py /opt/create_venvs.py

RUN apt-get update && apt-get install -y --no-install-recommends python3-venv && python /opt/create_venvs.py
