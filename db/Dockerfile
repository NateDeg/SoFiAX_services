FROM library/postgres:15.3
RUN apt-get update && apt-get upgrade -y && apt-get install -y postgresql-contrib vim
RUN apt-get install -y postgresql-15-postgis-3
RUN apt-get install -y postgresql-15-pgsphere
RUN echo "en_US.UTF-8 UTF-8"> /etc/locale.gen
RUN locale-gen
COPY *.sql /docker-entrypoint-initdb.d/