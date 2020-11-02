QUERIES = {

    'ADD_LOGIN_DETAILS' : "INSERT INTO LOGIN_DETAILS VALUES("
                          "%(id)s, "
                          "%(paswd)s)",

    'FETCH_LOGIN' : '''select ID, 
                            PASSWD 
                        from LOGIN_DETAILS ''',

    'FETCH_ALL_ADMIN' : '''SELECT 
                                EMPLOYEE.ID as ID, 
                                FNAME, 
                                LNAME, 
                                DOB, 
                                EMAIL_ID, 
                                ADMIN.ANNUAL_SALARY as salary, 
                                status 
                            FROM EMPLOYEE 
                            JOIN ADMIN 
                            ON EMPLOYEE.ID = ADMIN.ID 
                            WHERE EMPLOYEE.ISPERMANENT = TRUE ''',

    'DELETE_ADMIN' : '''DELETE FROM ADMIN 
                            WHERE ID = '{}';''',

    'ADD_ADMIN' : '''INSERT INTO ADMIN VALUES (
                        '{}', 
                        70000, 
                        current_timestamp(),
                        current_timestamp())''',

    'ADD_EMPLOYEE' : '''insert into EMPLOYEE VALUES (
                            %(id)s, 
                            %(first_name)s, 
                            %(last_name)s, 
                            STR_TO_DATE(%(dob)s, '%d-%b-%Y'), 
                            %(email)s, 
                            {}, 
                            TRUE, 
                            current_timestamp(),
                            current_timestamp())''',


    'DELETE_EMPLOYEE' : '''UPDATE EMPLOYEE SET 
                                STATUS = FALSE 
                                WHERE ID = '{}';''',

    'FETCH_ALL_CAREPROVIDER' : '''select 
                                    Employee.id, 
                                    fname, 
                                    lname, 
                                    dob, 
                                    email_id, 
                                    status, 
                                    CARE_PROVIDER.per_visit_charges 
                                from employee 
                                join CARE_PROVIDER 
                                on employee.id = CARE_PROVIDER.id 
                                where 
                                    Employee.isPermanent = False''',

    'ADD_CARE_PROVIDER' : '''INSERT INTO CARE_PROVIDER VALUES (
                                '{}', 
                                40, 
                                current_timestamp(),
                                current_timestamp()) ''',

    'DELETE_CARE_PROVIDER' : '''DELETE FROM 
                                        CARE_PROVIDER 
                                WHERE ID = '{}'; ''',

    'UPDATE_CARE_PROVIDER' : '''update CARE_PROVIDER set 
                                        PER_VISIT_CHARGES = %(per_visit_charges)s 
                                where id= %(id)s; ''',

    'FETCH_ALL_PATIENTS' : '''select 
                                patient.id, 
                                patient.firstname, 
                                patient.lastname, 
                                patient.email, 
                                patient.contactNumber, 
                                patient.dob, 
                                patient.consentToShare, 
                                patient.age 
                            from patient''',

    'ADD_PATIENT' : '''insert into patient values(
                                %(id)s, 
                                %(firstName)s, 
                                %(lastName)s, 
                                %(email)s, 
                                %(contactNumber)s, 
                                false, 
                                STR_TO_DATE(%(dob)s, '%d-%b-%Y'), 
                                %(age)s, 
                                current_timestamp(),
                                current_timestamp(), 
                                True) ''',

    'DELETE_PATIENT' : '''update patient 
                                set status = False 
                            where id = '{}';''',

    'UPDATE_PATIENT' : '''update Patient set 
                                firstName = %(firstName)s, 
                                lastName  = %(lastName)s, 
                                email = %(email)s, 
                                contactNumber = %(contactNumber)s,
                                age = %(age)s 
                            where id = '{}'; ''',

    'INIT_PATIENT_HISTORY' : '''insert into PatientMdeicalHistory values (
                                    nextVal(PatientMdeicalHistorySequencer),
                                    '{}',
                                    nextVal(PatientAllergySequencer),
                                    nextVal(PatientIllnessSequencer), 
                                    nextVal(PatientImmunisationSequencer), 
                                    nextVal(PatientLabDetailsSequencer))''',

    'FETCH_PATIENT_ADDRESS' : '''select 
                                    AddressDetails.address_line_1, 
                                    AddressDetails.address_line_2, 
                                    AddressDetails.city, 
                                    AddressDetails.postCode, 
                                    AddressDetails.country 
                                from AddressDetails 
                                where patient_id = '{}';''',

    'ADD_PATIENT_ADDRESS' : '''insert into AddressDetails values(
                                    NEXTVAL(AddressSequencer), 
                                    %(patientId)s, 
                                    %(address_line_1)s, 
                                    %(address_line_2)s, 
                                    %(city)s, 
                                    %(postCode)s, 
                                    %(country)s, 
                                    current_timestamp(), 
                                    current_timestamp())''',

    'UPDATE_ADDRESS' : ''' update AddressDetails set 
                                address_line_1 = %(address_line_1)s,
                                address_line_2  = %(address_line_2)s,
                                city = %(city)s,
                                postCode = %(postCode)s,
                                country = %(country)s
                            where patient_id = %(patientId)s; ''',
    
    'FETCH_PATIENT_NOTES' : '''select 
                                    id,
                                    patientId,
                                    note, 
                                    writtenBy, 
                                    writtenOn
                                from V_Patient_Notes where patientId = '{}'; ''',

    'ADD_PATIENT_NOTE' : '''insert into patientNote values (
                                nextVal(PatientNoteSequencer), 
                                %(patientId)s, 
                                %(note)s, 
                                %(writtenBy)s, 
                                current_timestamp())''',

    'FETCH_PATIENT_ALLERGIES' : '''select id,
                                        allergicTo, 
                                        onMedication 
                                    from AllergyDetail 
                                    where patientId='{}';''',

    'ADD_NEW_ALLERGY' : '''insert into AllergyDetail values (
                                nextVal(PatientAllergySequencer),
                                %(patientId)s,
                                %(allergicTo)s,
                                %(onMedication)s,
                                (select allergyIdentifier 
                                    from PatientMdeicalHistory 
                                    where patientId = '{}'),
                                current_timestamp())''',

    'DELETE_PATIENT_ALLERGY' : '''DELETE FROM 
                                    AllergyDetail 
                                    WHERE ID = {}''',

    'FETCH_PATIENT_ILLNESS_DETAILS' : ''' select 
                                                id,
                                                illness, 
                                                onMedication 
                                            from IllnessDetail 
                                            where patientId='{}'; ''',

    'ADD_NEW_ILLNESS' : '''insert into IllnessDetail values (
                                nextVal(PatientIllnessSequencer),
                                %(patientId)s,
                                %(illness)s,
                                %(onMedication)s,
                                (select illnessIdentifier 
                                    from PatientMdeicalHistory 
                                    where 
                                    patientId = '{}'),
                                current_timestamp())''',

    'FETCH_PATIENT_IMMUNISATION_DETAILS' : ''' select 
                                                    id,
                                                    immunisation, 
                                                    onMedication 
                                                from ImmunisationDetail 
                                                where patientId='{}'; ''',

    'ADD_NEW_IMMUNISATION' : '''insert into ImmunisationDetail values (
	                        nextVal(PatientImmunisationSequencer),
	                        %(patientId)s,
	                        %(immunisation)s,
	                        %(onMedication)s,
	                        (select immunisationIdentifier 
	                            from PatientMdeicalHistory 
	                            where 
	                            patientId = '{}'),
	                        current_timestamp())''',

    'FETCH_PATIENT_LAB_TEST_DETAILS' : ''' select 
                                                id,
                                                testName
                                            from LabTestDetail 
                                            where patientId='{}'; ''',

    'ADD_NEW_LAB_TEST' : '''insert into LabTestDetail values (
                                nextVal(PatientLabDetailsSequencer),
                                %(patientId)s,
                                %(testName)s,
                                (select labDetailIdentifier from PatientMdeicalHistory where patientId = '{}'),
	                            current_timestamp())''',

    'FETCH_ADMISSION_DETAILS' : '''select id, 
                                        admitDate, 
                                        dischargeDate, 
                                        isDischarged 
                                    from PatientAdmission 
                                    where 
                                        patientId='{}';''',

    'ADMIT_PATIENT' : ''' insert into PatientAdmission values (
                                nextVal(AdmitPatientSequencer), 
                                '{}', 
                                current_timestamp(), 
                                '0000-00-00 00:00:00.000000', 
                                FALSE)''',

    'DISCHARGE_PATIENT' : ''' update PatientAdmission 
                                set isDischarged = True 
                            where patientId='{}' 
                                and dischargeDate = '0000-00-00 00:00:00.000000';''',

    'GENERATE_BILL_ID' : 'select nextval(BillingSequencer)',

    'GENERATE_BILL' : '''insert into Bill values (
                            %(id)s, 
                            %(patientId)s, 
                            %(admissionId)s, 
                            %(adminCharges)s, 
                            %(labCharges)s, 
                            %(amount)s, 
                            current_timestamp(),
                            %(etherAmount)s,
                            FALSE,
                            '0000-00-00 00:00:00.000000'
                            );''',

    'FETCH_ALL_BILLS' : '''select id, 
                                patientId, 
                                admissionId, 
                                adminCharges, 
                                labCharges, 
                                amount, 
                                createdOn, 
                                etherAmount, 
                                isPaid 
                            from Bill''',

    'PAY_BILL' : '''update Bill set 
                        isPaid = True 
                    where id = {}''',

    'GET_BILL_ID_BY_PATIENT' : ''' SELECT Bill.id from Bill join PatientAdmission
                                            on Bill.patientId = PatientAdmission.patientId
                                            and Bill.admissionId = PatientAdmission.id
                                            where PatientAdmission.patientId = %(patientId)s
                                            and PatientAdmission.id = %(admissionId)s
                                            and PatientAdmission.isDischarged = FALSE ''',

    'ADD_AUDIT' : '''INSERT INTO audit_trail VALUES (
                        NEXTVAL(AUDIT_TRAIL_SEQUENCER),
                        %(entityId)s,
                        (select id from entity_type where type like %(entityType)s),
                        %(previousValue)s,
                        %(newValue)s,
                        %(changedBy)s,
                        NOW(),
                        (select id from audit_type where label like %(auditType)s)
                    )''',

    'GET_AUDIT_TRAIL' : '''select id,
                                entityId,
                                entityType,
                                attributeUpdated,
                                previousValue,
                                newValue,
                                changedBy,
                                updatedOn 
                            from V_Audit
                            where entityId = '{}';''',

    'UPDATE_EMPLOYEE' : '''UPDATE EMPLOYEE SET 
                                fname=%(first_name)s, 
			                    lname=%(last_name)s, 
			                    dob=STR_TO_DATE(%(dob)s, '%d-%b-%Y'),
			                    email_id = %(email)s,
			                    status = %(status)s
                            where id='{}';''',

    'UPDATE_ADMIN' : '''UPDATE ADMIN SET 
                            update_date = CURRENT_TIMESTAMP() 
                        where id = '{}';''',

    'INIT_PATIENT_CARE' : '''INSERT into PatientCare (id, patientId, careProviderId, admissionId) 
                            values 
                                (nextVal(PatientCareSequencer), 
                                %(patientId)s, 
                                %(careProviderId)s, 
                                (select id from PatientAdmission pa where 
                                patientId = %(patientId)s  and
                                isDischarged = False and
                                dischargeDate = '0000-00-00 00:00:00.000000'));''',

    'UPDATE_PATIENT_CARE_BILLING' : ''' update PatientCare set 
                                    billId = (
                                        select id 
                                        from bill 
                                        where 
                                            patientId = %(patientId)s
                                            and admissionId = %(admissionId)s 
                                            and isPaid = FALSE) 
                                    where patientId = %(patientId)s 
                                    and admissionId = %(admissionId)s ; ''',

    'UPDATE_DEFUALT_FOLLOWUP_DATE' : ''' update patientcare set 
                                        followupDate = (INTERVAL 1 MONTH + CURRENT_DATE()) 
                                        where 
                                            patientId = %(patientId)s 
                                            and 
                                            billId=%(billId)s; ''',

    'UPDATE_FOLLOWUP_DATE' : '''update PatientCare 
                                set followUpDate = STR_TO_DATE(%(followUpDate)s, '%d-%b-%Y')
                                where 
                                    patientId = %(patientId)s and
                                    billId = %(billId)s; '''
}