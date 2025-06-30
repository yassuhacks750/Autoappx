FROM sailvessel/ubuntu:latest
WORKDIR /app
COPY . .
RUN apt-get update && \
    apt-get install --no-install-recommends -y --fix-missing \
    python3 \
    python3-pip \
    python3-dev \
    python3-venv \
    ffmpeg \
    aria2 \
    && rm -rf /var/lib/apt/lists/*
RUN wget https://www.masterapi.tech/get/linux/pkg/download/appxdl
RUN mv appxdl /usr/local/bin/appxdl
RUN chmod +x /usr/local/bin/appxdl
RUN python3 -m venv /venv && \
    /venv/bin/pip install -r master.txt
ENV PATH="/usr/local/bin:/venv/bin:$PATH"
CMD ["python3", "main.py"]
