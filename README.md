# EMR_API

This Python API provides the functions for the EMR (https://en.wikipedia.org/wiki/Electronic_health_record) operations for three entities : 

```
1. Admin - can perform CRUD + View operations for Care Providers and Patients.
2. Care Provider - can perform CRUD + View operations for patients, besides adding patient notes.
3. Patient - the entity being managed by the system. 
```

The API has ability to interact with both MySql (tested with local server) and MongoDB (tested with both local and cloud cluster).

## System requirements : 
```
1. Operating System : MacOS / Windows (preferred : MacOS)
2. Python : 3.6 or higher
3. IDE : Anaconda Navigator with PyCharm installed, 
          can be downloaded from : https://docs.anaconda.com/anaconda/install/
4. XAMPP : a local server that will help to connect to Databse. 
          Can be downloaded from : https://www.apachefriends.org/download.html
5. DBeaver : an open source database tool. 
          Can be downloaded from : https://dbeaver.io/download/
6. MongoDB (Optional if using local Mongo instance)  : a NoSql collection based database. 
          can be downloaded from : https://docs.mongodb.com/manual/tutorial/install-mongodb-on-os-x/
7. MongoDB compass (Optional if using local Mongo instance) : Mongo client IDE for local usage. 
          Can be downloaded from : https://www.mongodb.com/try/download/compass
8. Mongo Atlas cluster (Optional if using Mongo cloud) : please follow the steps on 
  https://account.mongodb.com/account/loginn=%2Fv2%2F5f9a0c5e88f39e768ecf1ccd&nextHash=%23metrics%2FreplicaSet%2F5f9a0d7c94d89c1438088962%2Fexplorer%2FloginDetails%2Fusers%2Ffind to create a Mongo cloud cluster. 
  At the end, the portal will provide a URL that will help to connect to cluster. Please keep it safe and the next steps will explain how to use it. 
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
1. git clone 
2. git branch --all
3. git checkout develop
4. git pull develop
```

## Permissions
The rights to push to master/develop have been reserved by author : [Manik Jain] (https://github.com/Manik-Jain)
Kindly fork the repository and raise a pull request to contribute to the project.

## Future scope
```
1. Patient will have the right to grant/revoke consent share their EMR information with trusted users over Blockchain

```
