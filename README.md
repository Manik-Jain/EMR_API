# EMR_API

This Python API provides the functions for the [EMR](https://en.wikipedia.org/wiki/Electronic_health_record) operations for three entities : 

```
1. Admin - can perform CRUD + View operations for Care Providers and Patients.
2. Care Provider - can perform CRUD + View operations for patients, besides adding patient notes.
3. Patient - the entity being managed by the system. 
```

The API has ability to interact with both MySql (tested with local server) and MongoDB (tested with both local and cloud cluster).

## System requirements : 

1. Operating System : MacOS / Windows.
2. [Python](https://www.python.org/downloads/) : 3.6 or higher.
3. IDE : Any Python IDE. Recommended : [Anaconda Navigator](https://docs.anaconda.com/anaconda/install/) with PyCharm installed, 
          
4. [XAMPP](https://www.apachefriends.org/download.html) : a local server that will help to connect to Databse. 
          
5. [DBeaver](https://dbeaver.io/download/) : an open source database tool. 
         
6. [MongoDB](https://docs.mongodb.com/manual/tutorial/install-mongodb-on-os-x/) (Optional if using local Mongo instance)  : a NoSql collection based database. 
          
7. [MongoDB compass](https://www.mongodb.com/try/download/compass) (Optional if using local Mongo instance) : Mongo client IDE for local usage. 
8. [Mongo Atlas cluster](https://account.mongodb.com/account/loginn=%2Fv2%2F5f9a0c5e88f39e768ecf1ccd&nextHash=%23metrics%2FreplicaSet%2F5f9a0d7c94d89c1438088962%2Fexplorer%2FloginDetails%2Fusers%2Ffind ) (Optional if using Mongo cloud) : please follow the steps to create a Mongo cloud cluster. 
  At the end, the portal will provide a URL that will help to connect to cluster. Please keep it safe and the next steps will explain how to use it. 

## Project structure

The API has been written in Python v3.7 using [Flask-RESTPlus](https://github.com/python-restx/flask-restx) library.
The API comes with a build-in [Swagger UI](https://swagger.io/tools/swagger-ui/) that can be used to visualise and test the API methods.

## Python packages required

Depending on the version of Python that you are running in your machine, please use pip (for Python v2+) and pip3 (for Python v3+) to have the following packages in your machine:

```python

1. Flask
2. Flask-Cors
3. flask-restplus
4. flask-restx
5. mysql-connector
6. mysql-connector-python
7. pymongo
8. dnspython
9. urllib3

```

## Database Commands

```
CREATE database EMR_1;

CREATE USER IF NOT EXISTS emrHashUser@localhost IDENTIFIED BY '045b95b4047406cd995fbdf3c9a3fd95fb496128ea237b1cdc543c96e509b8e9';

GRANT ALL PRIVILEGES ON *.* TO emrHashUser@localhost;

flush privileges;
```
## Project status

Please clone and pull develop for most recent updates

```
1. git clone https://github.com/Manik-Jain/EMR_API/tree/develop
2. git branch --all
3. git checkout develop
4. git pull develop
```

## Permissions
The rights to push to master/develop have been reserved by author : [Manik Jain](https://github.com/Manik-Jain).
Kindly fork the repository and raise a pull request to contribute to the project.

## Future scope
```
1. Patient will have the right to grant/revoke consent share their EMR information with trusted users over Blockchain

```
