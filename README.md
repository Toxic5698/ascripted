# ascripted

Project for manage information in attorney office.


# development launch
1. clone repository
2. create venv
3. install requirements
   1. pip install -r requirements.txt
4. create database
   1. psql -U postgres
   2. CREATE DATABASE ascripted;
   3. ALTER DATABASE ascripted OWNER TO postgres;
5. run manage.py migrate
6. run server
