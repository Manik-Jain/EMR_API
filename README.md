# EMR_API


Kindly checkout develop for most latest changes.

## Database Commands

```
CREATE database EMR_1;

CREATE USER IF NOT EXISTS emrHashUser@localhost IDENTIFIED BY '045b95b4047406cd995fbdf3c9a3fd95fb496128ea237b1cdc543c96e509b8e9';

GRANT ALL PRIVILEGES ON *.* TO emrHashUser@localhost;

flush privileges;
```
