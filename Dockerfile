FROM python:3.6

# Create app directory
WORKDIR /app

# Install app dependencies
COPY src_python/requirements.txt ./

ENV http_proxy http://PITC-Zscaler-ASPAC-Bangalore3PR.proxy.corporate.ge.com:80
ENV https_proxy http://PITC-Zscaler-ASPAC-Bangalore3PR.proxy.corporate.ge.com:80

RUN pip install -r requirements.txt

# Bundle app source
COPY src_python /app

EXPOSE 8080
CMD [ "python", "server.py" ]