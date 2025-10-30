#!/usr/bin/env python3
"""
Script to create a sample Excel file with product data for testing
"""

import pandas as pd

sample_data = {
    'SKU': ['SKU001', 'SKU002', 'SKU003', 'SKU004', 'SKU005'],
    'Product_Name': [
        'Wireless Mouse',
        'USB-C Cable',
        'Laptop Stand',
        'Bluetooth Keyboard',
        'Webcam HD'
    ],
    'Quantity': [50, 100, 25, 30, 15],
    'Price': [29.99, 12.50, 45.00, 79.99, 89.95]
}

df = pd.DataFrame(sample_data)

df.to_excel('sample_products.xlsx', index=False)
print("✓ Created sample_products.xlsx with 5 sample products")
print("\nSample products:")
print(df.to_string(index=False))
