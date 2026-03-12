from flask import Flask, jsonify
import sqlite3

app = Flask(__name__)

def get_db_connection():
    conn = sqlite3.connect('assessment.db')
    conn.row_factory = sqlite3.Row 
    return conn

@app.route('/customer/<int:customer_id>', methods=['GET'])
def get_customer_details(customer_id):
    conn = get_db_connection()
    
    customer = conn.execute('SELECT * FROM customers WHERE id = ?', (customer_id,)).fetchone()
    
    if customer is None:
        return jsonify({'error': 'Customer not found'}), 404

    orders = conn.execute('SELECT * FROM orders WHERE customer_id = ?', (customer_id,)).fetchall()
    conn.close()

    return jsonify({
        'customer': dict(customer),
        'orders': [dict(order) for order in orders]
    })

if __name__ == '__main__':
    app.run(debug=True)