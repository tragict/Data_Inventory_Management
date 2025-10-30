# Inventory Management System

## Overview
A Python-based inventory management system that imports data from Excel files and tracks products with SKUs, quantities, and prices. The system provides a command-line interface for managing inventory operations including viewing, searching, adding, updating, and exporting product data.

**Current State**: Fully functional with all core features implemented and tested.

## Recent Changes
- **October 30, 2025**: Initial implementation of inventory management system
  - Created main inventory manager with Excel integration
  - Implemented CRUD operations for products
  - Added search and filter functionality
  - Created sample data and test suite
  - All tests passing successfully

## Features
### Core Functionality
- **Import from Excel**: Load product data from Excel files (XLSX format)
- **Product Tracking**: Manage products with SKU, name, quantity, and price
- **View Inventory**: Display all products in formatted tables with total value calculation
- **Search**: Find products by SKU or product name
- **Add Products**: Create new inventory items
- **Update Products**: Modify quantities and prices
- **Delete Products**: Remove items from inventory
- **Export to Excel**: Save current inventory to Excel files
- **Filter Views**: View products filtered by SKU or name

### Data Persistence
- All inventory data is automatically saved to `inventory_data.xlsx`
- Import/export functionality supports standard Excel formats

## Project Structure
```
.
├── inventory_manager.py      # Main inventory management system
├── sample_products.py         # Script to generate sample data
├── test_inventory.py          # Automated test suite
├── sample_products.xlsx       # Sample product data (5 items)
├── inventory_data.xlsx        # Current inventory database
└── replit.md                  # This documentation file
```

## Usage

### Running the System
The inventory manager runs automatically via the workflow. You'll see an interactive menu with options 1-8.

### Menu Options
1. **View All Inventory** - Display complete inventory list
2. **Search Product** - Find products by SKU or name
3. **Add New Product** - Create a new inventory item
4. **Update Product** - Modify quantity or price
5. **Delete Product** - Remove an item from inventory
6. **Import from Excel** - Load products from an Excel file
7. **Export to Excel** - Save inventory to an Excel file
8. **Exit** - Close the application

### Excel File Format
Import files must have these columns:
- `SKU`: Product SKU code
- `Product_Name`: Name of the product
- `Quantity`: Number of units in stock
- `Price`: Price per unit

Example:
```
SKU     | Product_Name    | Quantity | Price
SKU001  | Wireless Mouse  | 50       | 29.99
SKU002  | USB-C Cable     | 100      | 12.50
```

### Sample Data
Run `python sample_products.py` to generate a sample Excel file with 5 products for testing.

### Running Tests
Execute `python test_inventory.py` to run the automated test suite that verifies all functionality.

## Dependencies
- **pandas**: Excel file processing and data manipulation
- **openpyxl**: Reading and writing Excel files
- **tabulate**: Formatted table output in console

All dependencies are managed via `uv` and specified in `pyproject.toml`.

## Technical Details
- **Language**: Python 3.11
- **Data Storage**: Excel files (XLSX format)
- **Primary Library**: pandas DataFrame for data management
- **Interface**: Command-line interactive menu

## Future Enhancements
Potential features for future development:
- Low stock alerts with configurable thresholds
- Inventory transaction history tracking
- Data validation and duplicate SKU prevention
- Batch update capabilities
- Advanced reporting and analytics
- Multi-location/warehouse support
- Database backend option (PostgreSQL)
