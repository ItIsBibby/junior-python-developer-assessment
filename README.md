# Junior Python Developer Assessment

A Python-based assessment project that demonstrates data processing, database management, and web application development skills.

## Project Overview

This project implements a complete data pipeline with the following components:
- **Database Setup**: SQLite database initialization with customer and order data
- **ETL Script**: Extract, Transform, and Load process for active customer orders
- **Flask Web Application**: REST API for accessing and managing data
- **Data Processing**: Pandas-based data transformation and analysis

## Features

✓ SQLite database with customers and orders tables  
✓ ETL pipeline that exports active customer orders to CSV  
✓ Flask web application with multiple endpoints  
✓ Data transformation and aggregation  
✓ CSV export functionality  

## Project Structure

```
junior-python-developer-assessment/
├── app.py                  # Flask web application
├── database_setup.py       # Database initialization and seeding
├── etl_script.py          # ETL process for data extraction and transformation
├── requirements.txt       # Python package dependencies
└── README.md             # This file
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

### Initialize the Database

Run the database setup script to create tables and populate with sample data:

```bash
python database_setup.py
```

This creates an `assessment.db` SQLite database with:
- **customers** table: Customer information with status tracking
- **orders** table: Order details linked to customers

### Run the ETL Process

Execute the ETL script to extract active customers' orders and save to CSV:

```bash
python etl_script.py
```

This will:
1. Query active customers and their orders from the database
2. Transform the data (combine first/last names, calculate totals)
3. Export results to `output/active_customers_orders.csv`

### Start the Flask Application

Launch the web application:

```bash
python app.py
```

The application will be available at `http://localhost:5000`

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
Initializes the SQLite database with:
- Schema creation for customers and orders
- Sample data generation using Faker library
- Indexes for query optimization

### etl_script.py
ETL pipeline that:
- Connects to the SQLite database
- Joins customer and order data
- Filters for active customers
- Transforms data (name concatenation, total calculations)
- Exports to CSV format

### app.py
Flask web application providing:
- Multiple REST endpoints
- Database connectivity
- Request/response handling

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
- All SQL queries use parameterized statements for security
- Data processing uses pandas DataFrames for efficiency

## License

This is an assessment project. Please refer to your organization's guidelines for usage and distribution.

## Author

Created by ItIsBibby as a junior Python developer assessment project.