FROM ubuntu:latest
LABEL authors="jorgeacf"

ENTRYPOINT ["top", "-b"]