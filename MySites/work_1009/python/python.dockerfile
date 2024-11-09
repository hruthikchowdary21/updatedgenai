FROM python:3.11-alpine

COPY scripts/ /app/
CMD tail -f /dev/null