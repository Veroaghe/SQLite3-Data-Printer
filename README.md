# SQLite3-Data-Printer

This Data Printer is meant to be used with SQLite3 in Python. 
The function inside prints out a selection, you've made with the cursor in the database, in a standardized way. 
The comments in the file contain more info on how the data will be printed out. 

Import the function into the file where you're using SQLite 3 to select data from a database.

```python
from dataPrinter import data_printer
```

Select the columns and rows you want to view with the cursor and enter the cursor as an argument into the data_printer function. Example:

```python
import sqlite3
from dataPrinter import data_printer

conn = sqlite3.connect('database.db')
c = conn.cursor()

c.execute("SELECT * FROM table)
data_printer(c)
```
