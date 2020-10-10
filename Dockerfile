FROM python:3.7.6
ENV PORT 8081
COPY ./requirements.txt /bot/requirements.txt
WORKDIR /bot
RUN pip install -r requirements.txt
COPY ./bot/alkobot.py /bot/alkobot.py
ENTRYPOINT ["python"]
CMD ["alkobot.py"]
