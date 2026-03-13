import sqlite3
import pandas as pd
import os

def run_etl_process():
    if not os.path.exists('output'):
        os.makedirs('output')

    conn = sqlite3.connect('assessment.db')
    
    query = """
    SELECT 
        c.first_name, 
        c.surname, 
        o.product_name, 
        o.quantity, 
        o.unit_price
    FROM customers c
    JOIN orders o ON c.id = o.customer_id
    WHERE c.status = 'active'
    """
    
    df = pd.read_sql_query(query, conn)
    conn.close()

    if df.empty:
        print("No active customers found to export.")
        return

    df['name'] = df['first_name'] + " " + df['surname']
    
    df['total_order_value'] = df['quantity'] * df['unit_price']
    
    final_df = df[['name', 'product_name', 'quantity', 'unit_price', 'total_order_value']]

    output_path = os.path.join('output', 'active_customers_orders.csv')
    final_df.to_csv(output_path, index=False)
    
    print(f"ETL process complete. File saved to: {output_path}")

if __name__ == "__main__":
    run_etl_process()