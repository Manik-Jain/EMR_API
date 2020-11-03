config = {
  'user': 'emrHashUser',
  'password': '045b95b4047406cd995fbdf3c9a3fd95fb496128ea237b1cdc543c96e509b8e9',
  'host': '127.0.0.1',
  'raise_on_warnings': True
}

DB_NAME = 'EMR'

MONGO_URL = 'mongodb+srv://root:root@cluster0.qyyno.mongodb.net/EMR?retryWrites=true&w=majority'

SEQUENCERS = {

    'AUDIT_TRAIL_SEQUENCER' : ''' CREATE SEQUENCE IF NOT EXISTS AUDIT_TRAIL_SEQUENCER START WITH 1 INCREMENT BY 1''',
    'ADDRESS_SEQUENCER' : '''CREATE SEQUENCE IF NOT EXISTS AddressSequencer START WITH 1 INCREMENT BY 1 ''',
    'PATIENT_NOTE_SEQUENCER' : '''CREATE SEQUENCE IF NOT EXISTS PatientNoteSequencer START WITH 1 INCREMENT BY 1''',
    'PATIENT_ALLERGY_SEQUENCER' : '''CREATE SEQUENCE IF NOT EXISTS PatientAllergySequencer START WITH 1 INCREMENT BY 1''',
    'PATIENT_ILLNESS_SEQUENCER' : ''' CREATE SEQUENCE IF NOT EXISTS PatientIllnessSequencer START WITH 1 INCREMENT BY 1 ''',
    'PATIENT_IMMUNISATION_SEQUENCER' : ''' CREATE SEQUENCE IF NOT EXISTS PatientImmunisationSequencer START WITH 1 INCREMENT BY 1 ''',
    'PATIENT_DETAIL_SEQUENCER' : ''' CREATE SEQUENCE IF NOT EXISTS PatientLabDetailsSequencer START WITH 1 INCREMENT BY 1''',
    'PATIENT_HISTORY_SEQUENCER' : ''' CREATE SEQUENCE IF NOT EXISTS PatientMdeicalHistorySequencer START WITH 1 INCREMENT BY 1 ''',
    'ADMIT_PATIENT_SEQUENCER' : '''CREATE SEQUENCE IF NOT EXISTS AdmitPatientSequencer START WITH 1 INCREMENT BY 1''',
    'PATIENT_CARE_SEQUENCER' : '''CREATE SEQUENCE IF NOT EXISTS PatientCareSequencer START WITH 1 INCREMENT BY 1''',
    'BillingSequencer' : ''' CREATE SEQUENCE IF NOT EXISTS BillingSequencer START WITH 1 INCREMENT BY 1 ''',
    'LOOKUP_SEQUENCER' : ''' CREATE SEQUENCE IF NOT EXISTS LOOKUP_SEQUENCER START WITH 1 INCREMENT BY 1'''
}

TABLES = {

    'LOGIN_DETAILS' : ''' CREATE TABLE IF NOT EXISTS LOGIN_DETAILS(
                            ID VARCHAR(100) NOT NULL PRIMARY KEY,
                            PASSWD VARCHAR(200) NOT NULL,
                            UNIQUE KEY (ID)
                        );''',

    'ENTITY_TYPE' : '''CREATE TABLE IF NOT EXISTS ENTITY_TYPE (
                        ID INT NOT NULL PRIMARY KEY,
                        TYPE VARCHAR(20) NOT NULL
                    );''',

    'EMPLOYEE' : ''' CREATE TABLE IF NOT EXISTS EMPLOYEE(
                        ID VARCHAR(100) NOT NULL PRIMARY KEY,
                        FNAME VARCHAR(100) NOT NULL,
                        LNAME VARCHAR(100) NOT NULL,
                        DOB DATE NOT NULL,
                        EMAIL_ID VARCHAR(100) NOT NULL,
                        ISPERMANENT BOOLEAN NOT NULL,
                        STATUS Boolean,
                        create_date TimeStamp NOT NULL DEFAULT current_timestamp(),
                        update_date TimeStamp NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp(),
                        UNIQUE KEY (ID)
                    );''',

    'ADMIN' : '''CREATE TABLE IF NOT EXISTS ADMIN(
                        ID VARCHAR(100) NOT NULL,
                        ANNUAL_SALARY FLOAT NOT NULL,
                        create_date TimeStamp NOT NULL DEFAULT current_timestamp(),
                        update_date TimeStamp NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp(),
                        PRIMARY KEY(ID),
                        UNIQUE KEY (ID),
                        CONSTRAINT FOREIGN KEY (ID) REFERENCES EMPLOYEE(ID)
                    );''',

    'CARE_PROVIDER' : '''CREATE TABLE IF NOT EXISTS CARE_PROVIDER(
                            ID VARCHAR(100) NOT NULL,
                            PER_VISIT_CHARGES FLOAT NOT NULL,
                            create_date TimeStamp NOT NULL DEFAULT current_timestamp(),
                            update_date TimeStamp NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp(),
                            PRIMARY KEY(ID),
                            UNIQUE KEY (ID),
                            CONSTRAINT FOREIGN KEY (ID) REFERENCES EMPLOYEE(ID)
                        );''',

    'AUDIT_TYPE' : ''' CREATE TABLE IF NOT EXISTS AUDIT_TYPE (
                            ID INT NOT NULL PRIMARY KEY,
                            LABEL VARCHAR(20) NOT NULL
                        );''',

    'AUDIT_TRAIL' : '''CREATE table IF NOT EXISTS AUDIT_TRAIL (
                            ID INT NOT NULL,
                            ENTITY_ID VARCHAR(100) NOT NULL,
                            ENTITY_TYPE_ID INT NOT NULL,
                            PREVIOUS_VALUE VARCHAR(200),
                            NEW_VALUE VARCHAR(200),
                            CHANGED_BY VARCHAR(200),
                            UPDATED_ON DATETIME,
                            AUDIT_TYPE INT,
                            PRIMARY KEY (ID),
                            CONSTRAINT FK_ENTITY_TYPE_ID FOREIGN KEY (ENTITY_TYPE_ID) REFERENCES ENTITY_TYPE(ID),
                            CONSTRAINT FK_CHANGED_BY FOREIGN KEY (CHANGED_BY) REFERENCES EMPLOYEE(ID),
                            CONSTRAINT FOREIGN KEY(AUDIT_TYPE) REFERENCES AUDIT_TYPE(ID)
                        );''',

    'PATIENT' : '''CREATE TABLE  IF NOT EXISTS PATIENT(
                            ID VARCHAR(100) NOT NULL PRIMARY KEY,
                            firstName VARCHAR(50),
                            lastName VARCHAR(50),
                            email VARCHAR(100),
                            contactNumber INT NOT NULL,
                            consentToShare BOOLEAN NOT NULL default false,
                            dob DATE not null,
                            age int not null,
                            createdOn timestamp not null NOT NULL DEFAULT current_timestamp(),
                            update_date TimeStamp NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp(),
                            status BOOLEAN not null DEFAULT TRUE
                        );''',

    'AddressDetails' : '''create table if not exists AddressDetails (
                            id int not null primary key,
                            patient_id varchar(100) not null,
                            address_line_1 varchar(100) not null,
                            address_line_2 varchar(100),
                            city varchar(100) not null,
                            postCode int(10) not null,
                            country char(50) not null,
                            createdOn timestamp not null NOT NULL DEFAULT current_timestamp(),
                            update_date TimeStamp NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp(),
                            unique key(patient_id),
                            CONSTRAINT foreign key fk_patient_id (patient_id) references patient(id)
                        );''',

    'PATIENTNOTE' : '''create table if not exists patientNote (
                            id int not null primary key,
                            patientId varchar(100) not null,
                            note varchar(100) not null,
                            writtenBy varchar(100) not null,
                            createdOn timestamp not null NOT NULL DEFAULT current_timestamp(),
                            constraint foreign key (patientId) references patient(id),
                            constraint foreign key fk_writtenBy (writtenBy) references care_provider(id)
                        );''',

    'PatientMdeicalHistory' : '''CREATE  table if not exists PatientMdeicalHistory(
                                     id int not null primary key,
                                     patientId varchar(100) not null unique key,
                                     allergyIdentifier int not null unique key,
                                     illnessIdentifier int not null unique key,
                                     immunisationIdentifier int not null unique key,
                                     labDetailIdentifier int not null unique key,
                                     constraint foreign key (patientId) references patient(id)
                                );''',

    'AllergyDetail' : '''create table if not exists AllergyDetail (
                                id int not null primary key,
                                patientId varchar(100) not null,
                                allergicTo varchar(100) not null,
                                onMedication Boolean not null default False,
                                allergyIdentifer int not null,
                                createDate timestamp not null NOT NULL DEFAULT current_timestamp(),
                                constraint foreign key patientId (patientId) references patient(id),
                                constraint foreign key (allergyIdentifer) references PatientMdeicalHistory(allergyIdentifier)
                        );''',

    'IllnessDetail'  : '''create table if not exists IllnessDetail (
                            id int not null primary key,
                            patientId varchar(100) not null,
                            illness varchar(100) not null,
                            onMedication Boolean not null default False,
                            illnessIdentifer int not null,
                            createDate timestamp NOT NULL DEFAULT current_timestamp(),
                            constraint foreign key (patientId) references patient(id),
                            constraint foreign key (illnessIdentifer) references PatientMdeicalHistory(illnessIdentifier)
                        );''',

    'ImmunisationDetail' : '''create table if not exists ImmunisationDetail (
                                id int not null primary key,
                                patientId varchar(100) not null,
                                immunisation varchar(100) not null,
                                onMedication Boolean not null default False,
                                immunisationIdentifier int not null,
                                createDate timestamp NOT NULL DEFAULT current_timestamp(),
                                constraint foreign key (patientId) references patient(id),
                                constraint foreign key (immunisationIdentifier) references PatientMdeicalHistory(immunisationIdentifier)
                            );''',

    'LabTestDetail' : '''create table if not exists LabTestDetail (
                            id int not null primary key,
                            patientId varchar(100) not null,
                            testName varchar(100) not null,
                            labDetailIdentifier int not null,
                            createDate timestamp NOT NULL DEFAULT current_timestamp(),
                            constraint foreign key (patientId) references patient(id),
                            constraint foreign key (labDetailIdentifier) references PatientMdeicalHistory(labDetailIdentifier)
                        );''',

    'PatientAdmission' : '''CREATE table if not exists PatientAdmission (
                            id int not null primary key,
                            patientId varchar(100) not null,
                            admitDate timestamp NOT NULL DEFAULT current_timestamp(),
                            dischargeDate timestamp default '0000-00-00 00:00:00.000000' ON UPDATE current_timestamp(),
                            isDischarged Boolean not null,
                            constraint foreign key (patientId) references patient(id)
                        );''',

    'Bill' : '''CREATE TABLE Bill (
                      id int(11) NOT NULL,
                      patientId varchar(100) NOT NULL,
                      admissionId int(11) DEFAULT NULL,
                      adminCharges float NOT NULL,
                      labCharges float DEFAULT NULL,
                      amount float NOT NULL,
                      createdOn timestamp NOT NULL DEFAULT current_timestamp(),
                      etherAmount float NOT NULL,
                      isPaid tinyint(1) NOT NULL DEFAULT 0,
                      updateDate timestamp NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp(),
                  PRIMARY KEY (id),
                  UNIQUE KEY admissionId (admissionId),
                  CONSTRAINT  FOREIGN KEY (patientId) REFERENCES patient (ID),
                  CONSTRAINT  FOREIGN KEY (admissionId) REFERENCES PatientAdmission (id)
                );''',

    'PatientCare' : '''create table PatientCare(
                            id int not null primary key,
                            patientId varchar(100) not null,
                            careProviderId varchar(100) not null,
                            admissionId int,
                            billId int,
                            visitDate date,
                            followUpDate date,
                            createDate TimeStamp NOT NULL DEFAULT current_timestamp(),
                            updateDate TimeStamp NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp(),
                        CONSTRAINT  FOREIGN KEY (patientId) REFERENCES patient (ID),
                        CONSTRAINT  FOREIGN KEY (admissionId) REFERENCES PatientAdmission (id),
                        CONSTRAINT  FOREIGN KEY (careProviderId) REFERENCES Care_Provider (ID),
                        CONSTRAINT  FOREIGN KEY (billId) REFERENCES Bill (id)
                        );'''
}

INDEXES = {

    'auditTrailIndex' : '''  CREATE INDEX IF NOT EXISTS auditTrailIndex ON AUDIT_TRAIL (ENTITY_ID) ''',
    'employeeIndex' : ''' CREATE INDEX IF NOT EXISTS employeeIndex ON Employee (ID)''',
    'adminIndex' : '''CREATE INDEX IF NOT EXISTS adminIndex ON Admin (ID)''',
    'careProviderIndex' : '''CREATE INDEX IF NOT EXISTS careProviderIndex ON Care_Provider (ID)''',
    'patientHistory' : '''CREATE INDEX IF NOT EXISTS patientHistory ON PatientMdeicalHistory (patientId)''',
    'patientIndex' : '''CREATE INDEX IF NOT EXISTS patientIndex ON Patient (id)'''
}

VIEWS = {
    'V_Audit' : '''CREATE view IF NOT EXISTS V_Audit as
                select at2.id,
                    ENTITY_ID as entityId,
                    et.type  as entityType,
                    at3.LABEL as attributeUpdated,
                    PREVIOUS_VALUE as previousValue,
                    NEW_VALUE as newValue,
                    CONCAT(e2.FNAME, ' ', e2.LNAME) as changedBy,
                    UPDATED_ON as updatedOn
                from AUDIT_TRAIL at2
                join ENTITY_TYPE et
                on et.ID = at2.ENTITY_TYPE_ID
                join AUDIT_TYPE at3 on at3.ID = at2.AUDIT_TYPE
                join employee e2 on e2.id = at2.CHANGED_BY
                ORDER by at2.UPDATED_ON desc;''',

    'V_Patient_Notes' : '''CREATE view IF NOT EXISTS V_Patient_Notes as
                                select patientNote.id,
                                    patientNote.patientId,
                                    patientNote.note,
                                    CONCAT( employee.fname , ' ' ,employee.lname) as writtenBy,
                                    patientNote.createdOn as writtenOn
                                from patientNote
                                join care_provider on patientNote.writtenBy = care_provider.id
                                join employee on employee.id = care_provider.id
                                order by createdOn desc;'''
}

INSERTS = {
    'LOGIN' : '''insert into LOGIN_DETAILS VALUES (
                    'root', 
                    '4813494d137e1631bba301d5acab6e7bb7aa74ce1185d456565ef51d737677b2'
                );''',

    'ENTITY_TYPE_1' : ''' INSERT INTO ENTITY_TYPE VALUES(
                        nextVal(LOOKUP_SEQUENCER), 
                        'ADMIN'
                    ); ''',

    'ENTITY_TYPE_2' : ''' INSERT INTO ENTITY_TYPE VALUES(
                        nextVal(LOOKUP_SEQUENCER), 
                        'CARE_PROVIDER'
                    ); ''',

    'ENTITY_TYPE_3' : ''' INSERT INTO ENTITY_TYPE VALUES(
                        nextVal(LOOKUP_SEQUENCER), 
                        'PATIENT'
                    ); ''',

    'EMLOYEE_1' : '''insert into EMPLOYEE VALUES (
                        '3266dd0a-af55-4775-979e-e35d1',
                        'ROOT',
                        'ROOT',
                         STR_TO_DATE('11-Jan-1992', '%d-%b-%Y'),
                         'root@gmail.com',
                         TRUE,
                         TRUE,
                         current_timestamp(),
                         current_timestamp()
                    );''',

    'EMLOYEE_2' : '''insert into EMPLOYEE VALUES (
                        '3266dd0a-af55-4775-979e',
                        'CARE_PROVIDER',
                        'CARE_PROVIDER',
                         STR_TO_DATE('11-Jan-1992', '%d-%b-%Y'),
                         'careProvider@gmail.com',
                         FALSE,
                         TRUE,
                         current_timestamp(),
                         current_timestamp()
                    );''',

    'ADMIN' : ''' insert into admin VALUES (
                        '3266dd0a-af55-4775-979e-e35d1',
                        89000,
                        current_timestamp(),
                        current_timestamp()
                    );''',

    'CARE_PROVIDER' : '''insert into CARE_PROVIDER VALUES (
                            '3266dd0a-af55-4775-979e',
                            30,
                            current_timestamp(),
                            current_timestamp()
                    );''',

    'AUDIT_TYPE_1' : ''' INSERT INTO AUDIT_TYPE VALUES(nextVal(LOOKUP_SEQUENCER), 'NAME'); ''',
    'AUDIT_TYPE_2' : ''' INSERT INTO AUDIT_TYPE VALUES(nextVal(LOOKUP_SEQUENCER), 'CONTACT_INFO');''',
    'AUDIT_TYPE_3' : ''' INSERT INTO AUDIT_TYPE VALUES(nextVal(LOOKUP_SEQUENCER), 'ADDRESS');''',
    'AUDIT_TYPE_4' : ''' INSERT INTO AUDIT_TYPE VALUES(nextVal(LOOKUP_SEQUENCER), 'DOB');''',
    'AUDIT_TYPE_5' : ''' INSERT INTO AUDIT_TYPE VALUES(nextVal(LOOKUP_SEQUENCER), 'STATUS');''',
    'AUDIT_TYPE_6' : ''' INSERT into AUDIT_TYPE values(nextVal(LOOKUP_SEQUENCER), 'AGE');'''
}