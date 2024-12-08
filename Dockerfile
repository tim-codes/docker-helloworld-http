FROM debian:bookworm

LABEL maintainer="tim@exxo.sh"

RUN apt-get update \
    && apt-get upgrade -y \
    && DEBIAN_FRONTEND=noninteractive apt-get install -y python3 \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

COPY serve.py ./
EXPOSE 80
CMD ["python3", "./serve.py"]
