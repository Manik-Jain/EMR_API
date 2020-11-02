CREATE USER IF NOT EXISTS emrHashUser@localhost IDENTIFIED BY '045b95b4047406cd995fbdf3c9a3fd95fb496128ea237b1cdc543c96e509b8e9';
GRANT ALL PRIVILEGES ON *.* TO emrHashUser@localhost;
flush privileges;

----------------- LOGIN_DETAILS -------------
CREATE TABLE IF NOT EXISTS LOGIN_DETAILS(
	ID VARCHAR(100) NOT NULL PRIMARY KEY,
	PASSWD VARCHAR(200) NOT NULL,
	UNIQUE KEY (ID)
);

insert into LOGIN_DETAILS VALUES ('root', '4813494d137e1631bba301d5acab6e7bb7aa74ce1185d456565ef51d737677b2');
commit;

------------ENTITY_TYPE---------------------

CREATE TABLE IF NOT EXISTS ENTITY_TYPE (
    ID INT NOT NULL PRIMARY KEY,
    TYPE VARCHAR(20) NOT NULL
);

--ALTER TABLE ENTITY_TYPE ADD PRIMARY KEY(ID);

INSERT INTO ENTITY_TYPE VALUES(1, 'ADMIN');
INSERT INTO ENTITY_TYPE VALUES(2, 'CARE_PROVIDER');
INSERT INTO ENTITY_TYPE VALUES(3, 'PATIENT');
COMMIT;

----------------- EMPLOYEE -------------
CREATE TABLE IF NOT EXISTS EMPLOYEE(
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
);

--alter table employee add column status Boolean;
--alter table employee add column create_date TimeStamp NOT NULL DEFAULT current_timestamp();
--alter table employee add column update_date TimeStamp NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp();

insert into EMPLOYEE VALUES ('3266dd0a-af55-4775-979e-e35d1',
                               'ROOT',
                               'ROOT',
                               STR_TO_DATE('11-Jan-1992', '%d-%b-%Y'),
                               'root@gmail.com',
                                TRUE,
                                TRUE,
                                current_timestamp(),
                                current_timestamp());
commit;


----------------- ADMIN -------------
CREATE TABLE IF NOT EXISTS ADMIN(
	ID VARCHAR(100) NOT NULL,
	ANNUAL_SALARY FLOAT NOT NULL,
	create_date TimeStamp NOT NULL DEFAULT current_timestamp(),
    update_date TimeStamp NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp(),
	PRIMARY KEY(ID),
	UNIQUE KEY (ID),
	CONSTRAINT FOREIGN KEY (ID) REFERENCES EMPLOYEE(ID)
);

--alter table admin add column create_date TimeStamp NOT NULL DEFAULT current_timestamp();
--alter table admin add column update_date TimeStamp NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp();

insert into admin VALUES ('3266dd0a-af55-4775-979e-e35d1',
                           89000,
                           current_timestamp(),
                           current_timestamp());

----------------- CARE_PROVIDER -------------
CREATE TABLE IF NOT EXISTS CARE_PROVIDER(
	ID VARCHAR(100) NOT NULL,
	PER_VISIT_CHARGES FLOAT NOT NULL,
	create_date TimeStamp NOT NULL DEFAULT current_timestamp(),
	update_date TimeStamp NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp(),
	PRIMARY KEY(ID),
	UNIQUE KEY (ID),
	CONSTRAINT FOREIGN KEY (ID) REFERENCES EMPLOYEE(ID)
);

--alter table CARE_PROVIDER add column create_date TimeStamp NOT NULL DEFAULT current_timestamp();
--alter table CARE_PROVIDER add column update_date TimeStamp NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp();
insert into CARE_PROVIDER VALUES ('3266dd0a-af55-4775-979e',
                                    30,
                                    current_timestamp(),
                                    current_timestamp());

--------------- AUDIT_TRAIL------------------
create sequence AUDIT_TRAIL_SEQUENCER START WITH 1 INCREMENT BY 1;

CREATE TABLE IF NOT EXISTS AUDIT_TYPE (
    ID INT NOT NULL PRIMARY KEY,
    LABEL VARCHAR(20) NOT NULL
);

INSERT INTO AUDIT_TYPE VALUES(1, 'NAME');
INSERT INTO AUDIT_TYPE VALUES(2, 'CONTACT_INFO');
INSERT INTO AUDIT_TYPE VALUES(3, 'ADDRESS');
INSERT INTO AUDIT_TYPE VALUES(4, 'DOB');
INSERT INTO AUDIT_TYPE VALUES(5, 'STATUS');
INSERT into AUDIT_TYPE values(6, 'AGE');

CREATE table IF NOT EXISTS audit_trail (
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
);

--ALTER TABLE AUDIT_TRAIL ADD COLUMN UPDATED_ON DATETIME;
--ALTER TABLE AUDIT_TRAIL ADD COLUMN AUDIT_TYPE INT;
--ALTER TABLE AUDIT_TRAIL ADD FOREIGN KEY(AUDIT_TYPE) REFERENCES AUDIT_TYPE(ID);

---------------------PATIENT--------------
CREATE TABLE  IF NOT EXISTS Patient(
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
);

insert into patient values('1', 'patient', '1', 'pateint1@gmail.com', '0752405000', false);

--alter table Patient add column dob DATE not null;
--alter table Patient add column age int not null;
--alter table Patient add column createdOn timestamp not null NOT NULL DEFAULT current_timestamp();
--alter table Patient add column update_date TimeStamp NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp();
--alter table Patient add column status BOOLEAN not null DEFAULT TRUE;

---------------------ADDRESS DETAIL--------------
create sequence AddressSequencer START WITH 1 INCREMENT BY 1;

create table if not exists AddressDetails (
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
);

--alter table AddressDetails add column createdOn timestamp not null NOT NULL DEFAULT current_timestamp();
--alter table AddressDetails add column update_date TimeStamp NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp();

insert into AddressDetails values(NEXTVAL(AddressSequencer), '1', '49 Avenuve', 'Residhome Aparthotel', 'paris', 92400, 'France',current_timestamp(), current_timestamp());

-----------patient_note------------
create sequence PatientNoteSequencer START WITH 1 INCREMENT BY 1;

create table if not exists patientNote (
	id int not null primary key,
	patientId varchar(100) not null,
	note varchar(100) not null,
	writtenBy varchar(100) not null,
	createdOn timestamp not null NOT NULL DEFAULT current_timestamp(),
	constraint foreign key (patientId) references patient(id),
	constraint foreign key fk_writtenBy (writtenBy) references care_provider(id)
);

--alter table patientNote add foreign key fk_writtenBy (writtenBy) references care_provider(id);
--insert into patientNote values (nextVal(PatientNoteSequencer), '1', 'vitals normal', '7', current_timestamp());
--insert into patientNote values (nextVal(PatientNoteSequencer), '1', 'can be discharged', '7', current_timestamp());

--select patientNote.id,
--		patientNote.note,
--		CONCAT( employee.fname , ' ' ,employee.lname) as writtenBy,
--		patientNote.createdOn as writtenOn
--from patientNote
--	join care_provider on patientNote.writtenBy = care_provider.id
--	join employee on employee.id = care_provider.id
--where patientNote.patientId = '1'
--order by createdOn desc;

-----------Patient history------------

create sequence PatientAllergySequencer START WITH 1 INCREMENT BY 1;
create sequence PatientIllnessSequencer START WITH 1 INCREMENT BY 1;
create sequence PatientImmunisationSequencer START WITH 1 INCREMENT BY 1;
create sequence PatientLabDetailsSequencer START WITH 1 INCREMENT BY 1;
create sequence PatientMdeicalHistorySequencer START WITH 1 INCREMENT BY 1;

CREATE  table if not exists PatientMdeicalHistory(
     id int not null primary key,
     patientId varchar(100) not null unique key,
     allergyIdentifier int not null unique key,
     illnessIdentifier int not null unique key,
     immunisationIdentifier int not null unique key,
     labDetailIdentifier int not null unique key,
     constraint foreign key (patientId) references patient(id)
);

--------------Allergy Detail---------------
create table if not exists AllergyDetail (
    id int not null primary key,
    patientId varchar(100) not null,
    allergicTo varchar(100) not null,
    onMedication Boolean not null default False,
    allergyIdentifer int not null,
    createDate timestamp not null NOT NULL DEFAULT current_timestamp(),
    constraint foreign key patientId (patientId) references patient(id),
    constraint foreign key (allergyIdentifer) references PatientMdeicalHistory(allergyIdentifier)
);

--alter table AllergyDetail add column createDate timestamp not null NOT NULL DEFAULT current_timestamp();

insert into AllergyDetail values (
	nextVal(PatientAllergySequencer),
	'1',
	'strawberry',
	False,
	(select allergyIdentifier from PatientMdeicalHistory where patientId = '1'),
	current_timestamp()
);

create table if not exists IllnessDetail (
    id int not null primary key,
    patientId varchar(100) not null,
    illness varchar(100) not null,
    onMedication Boolean not null default False,
    illnessIdentifer int not null,
    createDate timestamp NOT NULL DEFAULT current_timestamp(),
    constraint foreign key (patientId) references patient(id),
    constraint foreign key (illnessIdentifer) references PatientMdeicalHistory(illnessIdentifier)
);

create table if not exists ImmunisationDetail (
    id int not null primary key,
    patientId varchar(100) not null,
    immunisation varchar(100) not null,
    onMedication Boolean not null default False,
    immunisationIdentifier int not null,
    createDate timestamp NOT NULL DEFAULT current_timestamp(),
    constraint foreign key (patientId) references patient(id),
    constraint foreign key (immunisationIdentifier) references PatientMdeicalHistory(immunisationIdentifier)
    );

create table if not exists LabTestDetail (
    id int not null primary key,
    patientId varchar(100) not null,
    testName varchar(100) not null,
    labDetailIdentifier int not null,
    createDate timestamp NOT NULL DEFAULT current_timestamp(),
    constraint foreign key (patientId) references patient(id),
    constraint foreign key (labDetailIdentifier) references PatientMdeicalHistory(labDetailIdentifier)
);


---------------Patient Admission and Discharge----------------
create sequence AdmitPatientSequencer START WITH 1 INCREMENT BY 1;

CREATE table if not exists PatientAdmission (
    id int not null primary key,
    patientId varchar(100) not null,
    admitDate timestamp NOT NULL DEFAULT current_timestamp(),
    dischargeDate timestamp default '0000-00-00 00:00:00.000000' ON UPDATE current_timestamp(),
    isDischarged Boolean not null,
    constraint foreign key (patientId) references patient(id)
);

--insert into PatientAdmission values (nextVal(AdmitPatientSequencer), '1', current_timestamp(), '0000-00-00 00:00:00.000000', FALSE);

-----------------PatientCare----------------
create Sequence PatientCareSequencer START WITH 1 INCREMENT BY 1;

create table PatientCare(
    id int not null primary key,
    patientId varchar(100) not null,
    careProviderId varchar(100) not null,
    admissionId int,
    billId int,
    visitDate date,
    followUpDate date,
    createDate TimeStamp NOT NULL DEFAULT current_timestamp(),
    updateDate TimeStamp NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp(),
constraint foreign key (patientId) references patient(id),
constraint foreign key (admissionId) references PatientAdmission(id),
constraint foreign key (careProviderId) references Care_Provider(id),
constraint foreign key (billId) references Bill(id)
);

--INSERT into PatientCare (id, patientId, careProviderId, admissionId) values
--	(nextVal(PatientCareSequencer), '1', '7', (select id from PatientAdmission pa where
--	patientId = '1' and
--	isDischarged = False and
--	dischargeDate = '0000-00-00 00:00:00.000000')
--);

---------------INDEX------------------

CREATE INDEX IF NOT EXISTS auditTrailIndex ON AUDIT_TRAIL (ENTITY_ID);
CREATE INDEX IF NOT EXISTS employeeIndex ON Employee (ID);
CREATE INDEX IF NOT EXISTS adminIndex ON Admin (ID);
CREATE INDEX IF NOT EXISTS careProviderIndex ON Care_Provider (ID);
CREATE INDEX IF NOT EXISTS patientHistory ON PatientMdeicalHistory (patientId);
CREATE INDEX IF NOT EXISTS patientIndex ON Patient (id);

---------------VIEWS------------------
CREATE view V_Audit as
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
    ORDER by at2.UPDATED_ON desc;

CREATE view V_Patient_Notes as
       select patientNote.id,
		patientNote.patientId,
       patientNote.note,
       CONCAT( employee.fname , ' ' ,employee.lname) as writtenBy,
       patientNote.createdOn as writtenOn
       from patientNote
       join care_provider on patientNote.writtenBy = care_provider.id
       join employee on employee.id = care_provider.id
       order by createdOn desc;