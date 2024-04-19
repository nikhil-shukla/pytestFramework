FROM python:3.12.2-slim

ARG ALLURE_VERSION=2.27.0
ARG CHROME_VERSION="123.0.6312.86-1"
ARG EDGE_VERSION="123.0.2420.65-1"

RUN apt-get update && \
    apt-get install -y \
    openjdk-17-jdk-headless \
    wget \
    gnupg \
    && apt-get clean

RUN wget -O allure-${ALLURE_VERSION}.tgz https://repo.maven.apache.org/maven2/io/qameta/allure/allure-commandline/${ALLURE_VERSION}/allure-commandline-${ALLURE_VERSION}.tgz && \
    tar -zxvf allure-${ALLURE_VERSION}.tgz -C /opt/ && \
    ln -s /opt/allure-${ALLURE_VERSION}/bin/allure /usr/bin/allure && \
    rm allure-${ALLURE_VERSION}.tgz

RUN wget --no-verbose -O /tmp/chrome.deb https://dl.google.com/linux/chrome/deb/pool/main/g/google-chrome-stable/google-chrome-stable_${CHROME_VERSION}_amd64.deb \
    && (dpkg -i /tmp/chrome.deb || apt-get -fy install) \
    && rm /tmp/chrome.deb \
    && sed -i 's|HERE/chrome"|HERE/chrome" --disable-setuid-sandbox --no-sandbox|g' "/opt/google/chrome/google-chrome" \
    && google-chrome --version

RUN wget -q https://packages.microsoft.com/keys/microsoft.asc -O- | apt-key add - \
    && wget -q "https://packages.microsoft.com/repos/edge/pool/main/m/microsoft-edge-dev/microsoft-edge-dev_${EDGE_VERSION}_amd64.deb" -O /tmp/microsoft-edge-dev.deb \
    && dpkg -i /tmp/microsoft-edge-dev.deb || apt-get -f install -y \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

ENV JAVA_HOME=/usr/lib/jvm/java-17-openjdk-amd64
ENV PATH=$JAVA_HOME/bin:$PATH
ENV PATH=/opt/allure-${ALLURE_VERSION}/bin:${PATH}

COPY requirements.txt requirements.txt

RUN pip3 install -r requirements.txt --quiet

CMD ["bash"]
