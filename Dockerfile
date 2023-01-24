FROM python:slim
ENV TOKEN 
COPY . .
RUN pip install -r requirements.txt
CMD python translate_bot.py
