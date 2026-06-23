



# Nexus
  
Module to connect to Nexus API, allowing to read/write data and listen to real-time events.  

*Read this in other languages: [English](Manual_Nexus.md), [Português](Manual_Nexus.pr.md), [Español](Manual_Nexus.es.md)*
  
![banner](imgs/BANNER_NEXUS.jpg)
## How to install this module
  
To install the module in Rocketbot Studio, it can be done in two ways:
1. Manual: __Download__ the .zip file and unzip it in the modules folder. The folder name must be the same as the module and inside it must have the following files and folders: \__init__.py, package.json, docs, example and libs. If you have the application open, refresh your browser to be able to use the new module.
2. Automatic: When entering Rocketbot Studio on the right margin you will find the **Addons** section, select **Install Mods**, search for the desired module and press install.  


## Description of the commands

### Connect to Nexus
  
Establishes a session with the Nexus API using an API Key.
|Parameters|Description|example|
| --- | --- | --- |
|Base URL|Rocketview server base URL (e.g. https//rocketview.myrb.io).|https://rocketview.myrb.io|
|API Key|API Key generated in the Nexus app settings.|rv_xxxxxxxxxxxxxxxx|
|Session name|Unique name to identify this connection session.|default|
|Result variable|Variable where True will be stored if the connection is successful.|result|

### List Tables
  
Returns all tables available for this API Key.
|Parameters|Description|example|
| --- | --- | --- |
|Session name|Session name used when connecting.|default|
|Result variable|Variable where the list of tables will be stored.|tables|

### Get Table
  
Returns the definition of a single table by ID.
|Parameters|Description|example|
| --- | --- | --- |
|Table ID|ID of the table to retrieve.|table-id-here|
|Session name|Session name used when connecting.|default|
|Result variable|Variable where the table definition will be stored.|table|

### Create Table
  
Creates a new table.
|Parameters|Description|example|
| --- | --- | --- |
|Table definition (JSON)|JSON object with the table name and columns.|{"name": "products", "columns": []}|
|Session name|Session name used when connecting.|default|
|Result variable|Variable where the created table will be stored.|new_table|

### Update Table
  
Updates table metadata (name, columns).
|Parameters|Description|example|
| --- | --- | --- |
|Table ID|ID of the table to update.|table-id-here|
|Updated data (JSON)|JSON object with the fields to update.|{"name": "new_name"}|
|Session name|Session name used when connecting.|default|
|Result variable|Variable where the updated table will be stored.|updated_table|

### Delete Table
  
Permanently deletes a table and all its rows.
|Parameters|Description|example|
| --- | --- | --- |
|Table ID|ID of the table to delete.|table-id-here|
|Session name|Session name used when connecting.|default|
|Result variable|Variable where True will be stored if the table was deleted.|result|

### Update Cell
  
Updates a single cell value in a row.
|Parameters|Description|example|
| --- | --- | --- |
|Table ID|ID of the table.|table-id-here|
|Row ID|ID of the row to update.|row-id-here|
|Column name|Name of the column to update.|price|
|New value|The new value for the cell.|99.99|
|Session name|Session name used when connecting.|default|
|Result variable|Variable where the response will be stored.|updated_row|

### Get Rows
  
Retrieves rows from a Nexus table.
|Parameters|Description|example|
| --- | --- | --- |
|Table ID|ID of the Nexus table to read from.|table-id-here|
|Limit (optional)|Maximum number of rows to return. Default 100.|100|
|Offset (optional)|Number of rows to skip. Default 0.|0|
|Session name|Session name used when connecting.|session|
|Result variable|Variable where the list of rows will be stored.|rows|

### Insert Row
  
Inserts a new row into a Nexus table.
|Parameters|Description|example|
| --- | --- | --- |
|Table ID|ID of the table where the row will be inserted.|table-id-here|
|Row data (JSON)|JSON object with the column/value pairs to insert.|{"field1": "value1", "price": 99.99}|
|Session name|Session name used when connecting.|session|
|Result variable|Variable where the inserted row (with its ID) will be stored.|new_row|

### Update Row
  
Updates an existing row by its ID.
|Parameters|Description|example|
| --- | --- | --- |
|Row ID|ID of the row to update.|row-id-here|
|Updated data (JSON)|JSON object with the fields to update.|{"price": 199.99, "stock": 5}|
|Session name|Session name used when connecting.|session|
|Result variable|Variable where the updated row will be stored.|updated_row|

### Delete Row
  
Deletes a row by its ID.
|Parameters|Description|example|
| --- | --- | --- |
|Row ID|ID of the row to delete.|row-id-here|
|Session name|Session name used when connecting.|session|
|Result variable|Variable where True will be stored if the row was deleted.|result|

### Delete All Rows
  
Erases all rows from a table without deleting the table itself.
|Parameters|Description|example|
| --- | --- | --- |
|Table ID|ID of the table to clear.|table-id-here|
|Session name|Session name used when connecting.|default|
|Result variable|Variable where True will be stored on success.|result|

### List Queries
  
Returns all saved queries available for this API Key.
|Parameters|Description|example|
| --- | --- | --- |
|Session name|Session name used when connecting.|default|
|Result variable|Variable where the list of queries will be stored.|queries|

### Execute Query
  
Executes a saved query in Nexus with optional parameters.
|Parameters|Description|example|
| --- | --- | --- |
|Query ID|ID of the query to execute.|query-id-here|
|Parameters (JSON, optional)|JSON object with dynamic parameters for the query.|{"search": "laptop", "minPrice": 100}|
|Session name|Session name used when connecting.|session|
|Result variable|Variable where the query result data will be stored.|query_result|
