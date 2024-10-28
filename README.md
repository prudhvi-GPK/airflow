# Airflow Project: File Move and ETL DAGs
This project demonstrates a basic ETL pipeline using Apache Airflow, including file movement and ETL processes. The pipeline uses Airflow DAGs to move files, extract data from source files, transform it, and load it into a PostgreSQL database.

## Project Structure
├── dags/
│   ├── dp.py       # DAG for moving files
│   └── etl.py             # DAG for ETL operations
├── plugins/
│   └── custom_operators/      # Custom operators (if any)
├── data/
│   ├── source/                   # Raw data files
│   └── dest/             # Processed data files
├── README.md                  # Project documentation
└── requirements.txt           # Python dependencies
# Features

- **File Move DAG**: Moves files from a source to a destination directory within Airflow.
- **ETL DAG**: Extracts data from raw files, applies transformations, and loads the data into a PostgreSQL database.
- **Customizable**: Modify source and destination paths, transformation logic, and load configurations as per project needs.

# Prerequisites

- **Apache Airflow**: Follow [Airflow's installation guide](https://airflow.apache.org/docs/apache-airflow/stable/start.html) to set up.
- **PostgreSQL**: Ensure PostgreSQL is installed and configured with an accessible database for this project.

   **Database Configuration:**
   - Database name: `airflow`
   - User: `postgres`
   - Password: `**********`
   
   Update these values in Airflow’s connections section as required.

- **Python Dependencies**: Install required dependencies with:
  ```bash
  pip install -r requirements.txt


DAG Details
File Move DAG (dp.py)
This DAG performs the following steps:

Move Files: Moves files from the data/raw/ folder to data/processed/.
ETL DAG (etl.py)
This DAG performs a typical ETL process:

Extract: Reads data from files in the data/processed/ directory.
Transform: Applies data transformations, such as data cleansing or calculations.
Load: Inserts the transformed data into the PostgreSQL database.
Usage
Access Airflow UI: Navigate to http://localhost:8080 in your browser to access the Airflow UI.
Trigger the DAGs: Trigger the DAGs from the Airflow UI and monitor their progress.
Logs: Logs for each task instance can be accessed through the Airflow UI, providing details for debugging and monitoring.
Customization
Modify DAG Parameters: Update parameters like source and destination paths in the DAG definitions.
Transformation Logic: Customize the transformation step within etl_dag.py to fit your data requirements.
License
This project is licensed under the MIT License. See the LICENSE file for more information.
