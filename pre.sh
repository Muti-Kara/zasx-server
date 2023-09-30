openssl req -x509 -nodes -days 3650 -newkey rsa:2048 -keyout ./nginx/certs/selfsigned.key -out ./nginx/certs/selfsigned.crt -config ./nginx/san.cnf
