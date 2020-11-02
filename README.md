# EMR_API

This Python API provides the functions for the [EMR](https://en.wikipedia.org/wiki/Electronic_health_record) operations for three entities : 

```
1. Admin - can perform CRUD + View operations for Care Providers and Patients.
2. Care Provider - can perform CRUD + View operations for patients, besides adding patient notes.
3. Patient - the entity being managed by the system. 
```

More details on EER and IFD can be tracked under [EMR_Data modelling](https://github.com/Manik-Jain/CSBC_1010_Data_Modelling)

The API has ability to interact with both [MySql](https://www.mysql.com/) (tested with local server) and [MongoDB](https://www.mongodb.com/) (tested with both local and cloud cluster).
The API provides an automated script to create a default database with zero SQL commands executed manually.
Please refer section (Automated default Database creation) for details.

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
The API comes with a built-in [Swagger UI](https://swagger.io/tools/swagger-ui/) that can be used to visualise and test the API methods.
The [Angular9](https://angular.io/) based User Interface is underway, and can be tracked for latest update under [EMR_UI](https://github.com/Manik-Jain/EMR_UI).

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

## Project status

Please clone and pull develop for most recent updates

```
1. git clone https://github.com/Manik-Jain/EMR_API/tree/develop
2. git branch --all
3. git checkout develop
4. git pull develop
```

## Database Commands

Once the repository has been cloned, please execute these SQL commands in Database to create a default user with granted previliges.

```
CREATE USER IF NOT EXISTS emrHashUser@localhost IDENTIFIED BY '045b95b4047406cd995fbdf3c9a3fd95fb496128ea237b1cdc543c96e509b8e9';

GRANT ALL PRIVILEGES ON *.* TO emrHashUser@localhost;

flush privileges;
```

## Automated default Database creation

Once the project has been cloned and the default user has been created in MySql server, the user can perform a one time load database feature that will help to create the following :

```
a) Sequencers
b) Tables
c) Index
d) Views
e) load data in lookup tables
```

To do this, please navigate to initialiseDatabase/initDb.py and provide the database name in Python dictionary : 

```python
DB_NAME = '<your database name goes here>'
```
This name will be used to create default database in the MySql server.

To use the Mongo features, please paste the Mongo Atlas cluster URL provided post step 8 under system requirements.

```python
MONGO_URL = '<your Mongo cluster URL goes here>'
```

Once the steps are done, please run initialiseDB.py script by using the following command from python shell :

```python

python initialiseDB.py
```

## API execution

Once the data has been loaded, the API can be triggered with the following command : 

```python
python launchApp.py
```
This will load the API in [Swagger UI](https://swagger.io/tools/swagger-ui/) at 

```
http://localhost:5000/
```

![Index](https://github.com/Manik-Jain/EMR_API/blob/develop/images/Index.png)
![Image_1](https://github.com/Manik-Jain/EMR_API/blob/develop/images/image_1.png)
![Image_2](https://github.com/Manik-Jain/EMR_API/blob/develop/images/image_2.png)
![Image_3](https://github.com/Manik-Jain/EMR_API/blob/develop/images/Screenshot%202020-11-02%20at%2021.46.43.png)
![Image_4](https://github.com/Manik-Jain/EMR_API/blob/develop/images/image_4.png)

Depending on the entity and operation, the user can perform the tests.

## Permissions
The rights to push to master/develop have been reserved by author : [Manik Jain](https://github.com/Manik-Jain).
Kindly fork the repository and raise a pull request to contribute to the project.

## Future scope

1. Patient will have the right to grant/revoke consent share their EMR information with trusted users over Blockchain
2. A [blockchain based payment API](https://github.com/Manik-Jain/eth-payment-gateway) is underway that will be integrated with the [EMR_UI](https://github.com/Manik-Jain/EMR_UI) so as to enable Ether based bill settlements.
