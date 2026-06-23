



# Nexus
  
Module to connect to Nexus API, allowing to read/write data and listen to real-time events.  

*Read this in other languages: [English](README.md), [Português](README.pr.md), [Español](README.es.md)*

## How to install this module
  
To install the module in Rocketbot Studio, it can be done in two ways:
1. Manual: __Download__ the .zip file and unzip it in the modules folder. The folder name must be the same as the module and inside it must have the following files and folders: \__init__.py, package.json, docs, example and libs. If you have the application open, refresh your browser to be able to use the new module.
2. Automatic: When entering Rocketbot Studio on the right margin you will find the **Addons** section, select **Install Mods**, search for the desired module and press install.  


## Overview


1. Connect to Nexus  
Establishes a session with the Nexus API using an API Key.

2. List Tables  
Returns all tables available for this API Key.

3. Get Table  
Returns the definition of a single table by ID.

4. Create Table  
Creates a new table.

5. Update Table  
Updates table metadata (name, columns).

6. Delete Table  
Permanently deletes a table and all its rows.

7. Update Cell  
Updates a single cell value in a row.

8. Get Rows  
Retrieves rows from a Nexus table.

9. Insert Row  
Inserts a new row into a Nexus table.

10. Update Row  
Updates an existing row by its ID.

11. Delete Row  
Deletes a row by its ID.

12. Delete All Rows  
Erases all rows from a table without deleting the table itself.

13. List Queries  
Returns all saved queries available for this API Key.

14. Execute Query  
Executes a saved query in Nexus with optional parameters.  




----
### OS

- windows
- mac
- linux
- docker

### Dependencies
- [**requests**](https://pypi.org/project/requests/)
### License
  
![MIT](https://img.shields.io/github/license/instaloader/instaloader.svg)  
[MIT](https://opensource.org/license/mit)