FROM python:3.11.0b3-alpine3.16
WORKDIR /opt/app
ADD . /opt/app/
RUN apk update && apk upgrade && apk add make bash
RUN bash
RUN make .PHONY
CMD python clobber/start.py