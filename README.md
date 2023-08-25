# XAMP-AUTO-BACKUP

The script index.py helps create a backup of XAMP database at specific time of the day.

## SETUP
1. python veriosn > 3.7 needed.
2. ```
   pip install requirements.txt
   ```
3. Make sure to fill necessary fields in index.py such as user, password, host etc.
4. add mysqldump_cmd in your enivronmental variables by giving path to mysqldump.exe against it.
5. Add .my.cnf file in your root directory with following text in it:
     ```
    [mysqldump]
    user=mysqluser
    password=secret
     ```
7. set desired time in config.ini.
8. add index.py into startup apps in windows so that it starts automatically when pc boots.
