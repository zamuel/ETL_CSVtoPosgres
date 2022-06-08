from ETL.scripts import extract
from ETL.scripts import transform
from ETL.scripts import load

if __name__ == "__main__":
    extract.main()
    transform.main()
    load.main()
