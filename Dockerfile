FROM python:3.9

WORKDIR /app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# set timezone to Denmark
RUN ln -sf /usr/share/zoneinfo/Europe/Copenhagen /etc/localtime

CMD [ "python", "./src/main.py" ]