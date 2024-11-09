FROM alpine:3.19

COPY baseversion.json /tmp/
ENV OS_VERSION="alpine:3.19"
RUN apk update && \
    apk add bash

CMD tail -f /dev/null