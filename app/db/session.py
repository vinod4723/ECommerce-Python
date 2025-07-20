from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import urllib

params = urllib.parse.quote_plus(
    "DRIVER={ODBC Driver 17 for SQL Server};"
    "SERVER=****;"
    "DATABASE=EcommerceDb;"
    "UID=****;"
    "PWD=****"
)

# Create SQLAlchemy engine
engine = create_engine(f"mssql+pyodbc:///?odbc_connect={params}")

# SessionLocal class to interact with the database
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
