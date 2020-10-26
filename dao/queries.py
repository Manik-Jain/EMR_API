QUERIES = {

    'ADD_LOGIN_DETAILS' : "INSERT INTO LOGIN_DETAILS VALUES(%(id)s, %(paswd)s)",
    'FETCH_ALL_ADMIN' : "SELECT EMPLOYEE.ID as ID, FNAME, LNAME, DOB, EMAIL_ID, ADMIN.ANNUAL_SALARY as salary, status FROM EMPLOYEE JOIN ADMIN ON EMPLOYEE.ID = ADMIN.ID WHERE EMPLOYEE.ISPERMANENT = TRUE",
    'DELETE_ADMIN' : "DELETE FROM ADMIN WHERE ID = '{}'",

    'ADD_ADMIN' : "INSERT INTO ADMIN VALUES ('{}', 70000, current_timestamp(),current_timestamp())",
    'ADD_EMPLOYEE' : "insert into EMPLOYEE VALUES (%(id)s, %(first_name)s, %(last_name)s, STR_TO_DATE(%(dob)s, '%d-%b-%Y'), %(email)s, {}, TRUE, current_timestamp(),current_timestamp())",
    'DELETE_EMPLOYEE' : "UPDATE EMPLOYEE SET STATUS=FALSE WHERE ID = '{}'",

    'FETCH_ALL_CAREPROVIDER' : "select Employee.id, fname, lname, dob, email_id, status, CARE_PROVIDER.per_visit_charges from employee join CARE_PROVIDER on employee.id = CARE_PROVIDER.id where Employee.isPermanent = False",
    'ADD_CARE_PROVIDER' : "INSERT INTO CARE_PROVIDER VALUES ('{}', 40, current_timestamp(),current_timestamp())",
    'DELETE_CARE_PROVIDER' : "DELETE FROM CARE_PROVIDER WHERE ID = '{}'"

}