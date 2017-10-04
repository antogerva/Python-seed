FROM polyhx/python-seed

ADD . .

EXPOSE 5030

CMD ["python", "ai.py"]
