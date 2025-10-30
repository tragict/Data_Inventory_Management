#!/usr/bin/env python3
"""
Inventory Management System
Imports data from Excel and tracks products with SKUs, quantities, and prices
"""

import pandas as pd
import os
from tabulate import tabulate
from datetime import datetime


class InventoryManager:
    def __init__(self, data_file='inventory_data.xlsx'):
        self.data_file = data_file
        self.inventory = pd.DataFrame(columns=['SKU', 'Product_Name', 'Quantity', 'Price'])
        self.load_inventory()
    
    def load_inventory(self):
        """Load inventory from Excel file if it exists"""
        if os.path.exists(self.data_file):
            try:
                self.inventory = pd.read_excel(self.data_file)
                print(f"✓ Loaded inventory from {self.data_file}")
            except Exception as e:
                print(f"Error loading inventory: {e}")
                self.inventory = pd.DataFrame(columns=['SKU', 'Product_Name', 'Quantity', 'Price'])
        else:
            print(f"No existing inventory file found. Starting fresh.")
    
    def save_inventory(self):
        """Save inventory to Excel file"""
        try:
            self.inventory.to_excel(self.data_file, index=False)
            print(f"✓ Inventory saved to {self.data_file}")
            return True
        except Exception as e:
            print(f"Error saving inventory: {e}")
            return False
    
    def import_from_excel(self, file_path):
        """Import products from an Excel file"""
        try:
            new_data = pd.read_excel(file_path)
            
            required_columns = ['SKU', 'Product_Name', 'Quantity', 'Price']
            if not all(col in new_data.columns for col in required_columns):
                print(f"Error: Excel file must contain columns: {', '.join(required_columns)}")
                return False
            
            for _, row in new_data.iterrows():
                sku = row['SKU']
                if sku in self.inventory['SKU'].values:
                    idx = self.inventory[self.inventory['SKU'] == sku].index[0]
                    self.inventory.loc[idx] = row
                    print(f"Updated existing product: {sku}")
                else:
                    self.inventory = pd.concat([self.inventory, pd.DataFrame([row])], ignore_index=True)
                    print(f"Added new product: {sku}")
            
            self.save_inventory()
            print(f"\n✓ Successfully imported {len(new_data)} products from {file_path}")
            return True
        except Exception as e:
            print(f"Error importing from Excel: {e}")
            return False
    
    def view_inventory(self, filter_sku=None, filter_name=None):
        """Display inventory in a formatted table"""
        if self.inventory.empty:
            print("\nInventory is empty.")
            return
        
        df = self.inventory.copy()
        
        if filter_sku:
            df = df[df['SKU'].str.contains(filter_sku, case=False, na=False)]
        
        if filter_name:
            df = df[df['Product_Name'].str.contains(filter_name, case=False, na=False)]
        
        if df.empty:
            print("\nNo products found matching the filter criteria.")
            return
        
        total_value = df['Quantity'].astype(float) * df['Price'].astype(float)
        
        df['Price'] = df['Price'].apply(lambda x: f"${x:.2f}")
        
        print("\n" + "="*80)
        print("INVENTORY")
        print("="*80)
        print(tabulate(df, headers='keys', tablefmt='grid', showindex=False))
        print(f"\nTotal Products: {len(df)}")
        print(f"Total Inventory Value: ${total_value.sum():.2f}")
        print("="*80 + "\n")
    
    def add_product(self, sku, product_name, quantity, price):
        """Add a new product to inventory"""
        if sku in self.inventory['SKU'].values:
            print(f"Error: Product with SKU '{sku}' already exists. Use update instead.")
            return False
        
        new_product = pd.DataFrame([{
            'SKU': sku,
            'Product_Name': product_name,
            'Quantity': quantity,
            'Price': price
        }])
        
        self.inventory = pd.concat([self.inventory, new_product], ignore_index=True)
        self.save_inventory()
        print(f"✓ Added product: {sku} - {product_name}")
        return True
    
    def update_product(self, sku, quantity=None, price=None):
        """Update quantity or price for a product"""
        if sku not in self.inventory['SKU'].values:
            print(f"Error: Product with SKU '{sku}' not found.")
            return False
        
        idx = self.inventory[self.inventory['SKU'] == sku].index[0]
        
        if quantity is not None:
            self.inventory.at[idx, 'Quantity'] = quantity
            print(f"✓ Updated quantity for {sku} to {quantity}")
        
        if price is not None:
            self.inventory.at[idx, 'Price'] = price
            print(f"✓ Updated price for {sku} to ${price:.2f}")
        
        self.save_inventory()
        return True
    
    def search_product(self, search_term):
        """Search for products by SKU or name"""
        df = self.inventory[
            (self.inventory['SKU'].str.contains(search_term, case=False, na=False)) |
            (self.inventory['Product_Name'].str.contains(search_term, case=False, na=False))
        ]
        
        if df.empty:
            print(f"\nNo products found matching '{search_term}'")
            return
        
        df_display = df.copy()
        df_display['Price'] = df_display['Price'].apply(lambda x: f"${x:.2f}")
        
        print("\n" + "="*80)
        print(f"SEARCH RESULTS FOR: '{search_term}'")
        print("="*80)
        print(tabulate(df_display, headers='keys', tablefmt='grid', showindex=False))
        print(f"\nFound {len(df)} product(s)")
        print("="*80 + "\n")
    
    def export_to_excel(self, file_path):
        """Export current inventory to Excel file"""
        try:
            self.inventory.to_excel(file_path, index=False)
            print(f"✓ Inventory exported to {file_path}")
            return True
        except Exception as e:
            print(f"Error exporting to Excel: {e}")
            return False
    
    def delete_product(self, sku):
        """Delete a product from inventory"""
        if sku not in self.inventory['SKU'].values:
            print(f"Error: Product with SKU '{sku}' not found.")
            return False
        
        product_name = self.inventory[self.inventory['SKU'] == sku]['Product_Name'].values[0]
        self.inventory = self.inventory[self.inventory['SKU'] != sku]
        self.save_inventory()
        print(f"✓ Deleted product: {sku} - {product_name}")
        return True


def display_menu():
    """Display the main menu"""
    print("\n" + "="*80)
    print("INVENTORY MANAGEMENT SYSTEM")
    print("="*80)
    print("1. View All Inventory")
    print("2. Search Product")
    print("3. Add New Product")
    print("4. Update Product (Quantity/Price)")
    print("5. Delete Product")
    print("6. Import from Excel")
    print("7. Export to Excel")
    print("8. Exit")
    print("="*80)


def main():
    """Main program loop"""
    manager = InventoryManager()
    
    while True:
        display_menu()
        choice = input("\nEnter your choice (1-8): ").strip()
        
        if choice == '1':
            manager.view_inventory()
        
        elif choice == '2':
            search_term = input("Enter SKU or product name to search: ").strip()
            if search_term:
                manager.search_product(search_term)
        
        elif choice == '3':
            print("\n--- Add New Product ---")
            sku = input("Enter SKU: ").strip()
            product_name = input("Enter Product Name: ").strip()
            try:
                quantity = int(input("Enter Quantity: ").strip())
                price = float(input("Enter Price: ").strip())
                manager.add_product(sku, product_name, quantity, price)
            except ValueError:
                print("Error: Invalid quantity or price format.")
        
        elif choice == '4':
            print("\n--- Update Product ---")
            sku = input("Enter SKU to update: ").strip()
            if sku in manager.inventory['SKU'].values:
                print("Leave blank to skip updating a field")
                quantity_input = input("Enter new Quantity: ").strip()
                price_input = input("Enter new Price: ").strip()
                
                quantity = int(quantity_input) if quantity_input else None
                price = float(price_input) if price_input else None
                
                manager.update_product(sku, quantity, price)
            else:
                print(f"Product with SKU '{sku}' not found.")
        
        elif choice == '5':
            print("\n--- Delete Product ---")
            sku = input("Enter SKU to delete: ").strip()
            confirm = input(f"Are you sure you want to delete '{sku}'? (yes/no): ").strip().lower()
            if confirm == 'yes':
                manager.delete_product(sku)
        
        elif choice == '6':
            print("\n--- Import from Excel ---")
            file_path = input("Enter Excel file path: ").strip()
            if os.path.exists(file_path):
                manager.import_from_excel(file_path)
            else:
                print(f"Error: File '{file_path}' not found.")
        
        elif choice == '7':
            print("\n--- Export to Excel ---")
            file_path = input("Enter output file path (e.g., export.xlsx): ").strip()
            if not file_path.endswith('.xlsx'):
                file_path += '.xlsx'
            manager.export_to_excel(file_path)
        
        elif choice == '8':
            print("\nThank you for using Inventory Management System!")
            break
        
        else:
            print("\nInvalid choice. Please enter a number between 1 and 8.")


if __name__ == "__main__":
    main()
