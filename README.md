## Python project setup
   #### Here we are trying to setup the E-Commerce application in python, we will define complete project architecture
#### 1. Create Project Folder
```
mkdir ecommerce-backend
cd ecommerce-backend

```
#### 2. Initialize Git (Optional)
```
git init
```
#### 3. Create a Virtual Environment
```
python -m venv venv
```
#### 4. Add Dependencies
```
Create "requirements.txt"  file inside root folder which will be used to install the depedencies.

We need to add all the depedenciesin thisfile and once we have all the detail there,we need to run the below single commnadand that will install all in one go.

>> pip install -r requirements.txt
```

### Setup the sql server user (i'm using sql server in this case)
#### Run below script to create user in sql server database.
```

USE master;
GO
CREATE LOGIN <UserName> WITH PASSWORD = '<Give Password>';
GO
USE EcommerceDb;
GO
CREATE USER <UserName> FOR LOGIN <UserName>;
ALTER ROLE db_owner ADD MEMBER <UserName>;

```
