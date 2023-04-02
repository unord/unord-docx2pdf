FROM python:3.11

# Install libreoffice
RUN apt-get update && \
    apt-get install -y libreoffice

ENV PYTHONUNBUFFERED=1
WORKDIR /app
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
COPY . .

# set timezone to Denmark
RUN ln -sf /usr/share/zoneinfo/Europe/Copenhagen /etc/localtime

CMD [ "python", "./src/main.py" ]