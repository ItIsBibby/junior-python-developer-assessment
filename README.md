# Junior Python Developer Assessment

This repository contains my submission for the Junior Python Developer technical assessment. The project demonstrates a full data lifecycle: initialising a relational database, serving data via a REST API, and performing an ETL process for reporting.

## Project Overview

This project implements a complete data pipeline with the following components:
- **Database Setup**: SQLite database initialization with customer and order data
- **ETL Script**: Extract, Transform, and Load process for active customer orders
- **Flask Web Application**: REST API for accessing and managing data
- **Data Processing**: Pandas-based data transformation and analysis

## Features

- SQLite database with customers and orders tables  
- ETL pipeline that exports active customer orders to CSV  
- Flask web application with multiple endpoints  
- Data transformation and aggregation  
- CSV export functionality  

## Project Structure

```
junior-python-developer-assessment/
├── app.py                  # Flask web application
├── database_setup.py       # Database initialisation and seeding
├── etl_script.py           # ETL process for data extraction and transformation
├── requirements.txt        # Python package dependencies
└── README.md               # This file
```

## Installation

### Prerequisites
- Python 3.7+
- pip (Python package manager)

### Setup Instructions

1. **Clone the repository** (if applicable)
```bash
git clone https://github.com/ItIsBibby/junior-python-developer-assessment.git
cd junior-python-developer-assessment
```

2. **Create a virtual environment** (recommended)
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

## Usage

### Initialise the Database

Run the database setup script to create tables and populate with sample data:

```bash
python database_setup.py
```

This creates an `assessment.db` SQLite database with:
- **customers** table: Customer information with status tracking
- **orders** table: Order details linked to customers

### Set up the API

Launch the web application:

```bash
python app.py
```

The application will be available at `http://localhost:5000/customer/<id>`

### Run the ETL Process

Execute the ETL script to extract active customers' orders and save to CSV:

```bash
python etl_script.py
```

This will:
1. Query active customers and their orders from the database
2. Transform the data (combine first/last names, calculate totals)
3. Export results to `output/active_customers_orders.csv`

## Choices and Reasoning
- SQLite: Chosen for its portability and zero-configuration requirement. It allows for testing without setting up a standalone database server.
- Pandas: Used for the ETL task as it is the industry standard for data manipulation, and handles complex processing more efficiently than standard Python loops.
- Faker: Used to quickly generate realistic sample data, ensuring the application is tested against varied inputs.
- Flask: Selected as the web framework due to its lightweight and modular nature, which is ideal for a single-purpose microservice API.

## Application Flow
**Data Generation**: database_setup.py wipes existing data and creates 50 unique customers with randomized orders.

**API Retrieval**: app.py accepts a GET request, performs a parameterised SQL query (to prevent SQL injection), and aggregates customer and order data into a JSON response.

**ETL Pipeline**: etl_script.py performs a SQL JOIN to extract data, applies logic to filter for "active" status, calculates total order values, and loads the result into a CSV file in the /output directory.

## Future Improvements
If this were a real-world project for the University, here is how it could be evolved:

**1. API Authentication**

Currently, anyone can access the customer data if they know the URL.
Improvement: Implement API Keys or JWT (JSON Web Tokens) to ensure only authorised users or internal systems can query sensitive customer information.

**2. Logging vs. Printing**

Currently, the scripts use print() to show progress.
Improvement: Switch to the standard Python logging library. This would allow the application to save errors to a .log file.

**3. Containerisation (Docker)**

To solve the "it works on my machine" problem.
Improvement: Create a Dockerfile. This would package the Python version, the libraries, and the code into a single "container" that runs exactly the same way on the reviewer's computer as it does on yours.

## Dependencies

| Package | Version | Purpose |
|---------|---------|---------|
| Flask | 3.1.3 | Web framework |
| pandas | 3.0.1 | Data manipulation and analysis |
| Faker | 40.8.0 | Generate fake data for testing |
| numpy | 2.4.3 | Numerical computing |
| sqlite3 | Built-in | Database management |

See `requirements.txt` for the complete list of dependencies.

## Key Components

### database_setup.py
Initialises the SQLite database with:
- Schema creation for customers and orders
- Sample data generation using Faker library
- Indexes for query optimisation

### app.py
Flask web application providing:
- Multiple REST endpoints
- Database connectivity
- Request/response handling

### etl_script.py
ETL pipeline that:
- Connects to the SQLite database
- Joins customer and order data
- Filters for active customers
- Transforms data (name concatenation, total calculations)
- Exports to CSV format

## Output

After running the ETL process, find the exported data at:
```
output/active_customers_orders.csv
```

The CSV includes the following columns:
- `name` - Customer full name
- `product_name` - Product ordered
- `quantity` - Order quantity
- `unit_price` - Price per unit
- `total_order_value` - Quantity × Unit Price

## Development Notes

- Database file: `assessment.db` (created in project root)
- Output directory: `output/` (created automatically if it doesn't exist)
- All SQL queries use parameterised statements to ensure protection against SQL injection
- Data processing uses pandas DataFrames for efficiency

## Author

Created by ItIsBibby as a junior Python developer assessment project.
