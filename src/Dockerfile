FROM public.ecr.aws/lambda/python:3.11
ENV PYTHONUNBUFFERED=1

COPY requirements.txt ./
RUN pip3 install -r requirements.txt

# Important use /var/task as the working directory
COPY . /var/task

CMD ["app.handler"]
