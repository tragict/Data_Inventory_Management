# Inventory Management System

A Python-based inventory management system that imports data from Excel files and tracks products with SKUs, quantities, and prices.

## Features

- **Import from Excel** - Load product data from Excel files (XLSX format)
- **Product Tracking** - Manage products with SKU, name, quantity, and price
- **View Inventory** - Display all products with formatted tables and total value calculation
- **Search** - Find products by SKU or product name
- **Add Products** - Create new inventory items
- **Update Products** - Modify quantities and prices
- **Delete Products** - Remove items from inventory
- **Export to Excel** - Save current inventory to Excel files
- **Filter Views** - View products filtered by SKU or name

## Installation

1. Clone this repository
2. Install Python 3.11 or higher
3. Install dependencies:
```bash
pip install pandas openpyxl tabulate
```

Or if using `uv`:
```bash
uv sync
```

## Usage

### Running the Application

```bash
python inventory_manager.py
```

This will start the interactive menu with options 1-8:

1. View All Inventory
2. Search Product
3. Add New Product
4. Update Product (Quantity/Price)
5. Delete Product
6. Import from Excel
7. Export to Excel
8. Exit

### Excel File Format

Import files must have these columns:
- `SKU` - Product SKU code
- `Product_Name` - Name of the product
- `Quantity` - Number of units in stock
- `Price` - Price per unit

Example:
```
SKU     | Product_Name    | Quantity | Price
SKU001  | Wireless Mouse  | 50       | 29.99
SKU002  | USB-C Cable     | 100      | 12.50
```

### Sample Data

Generate sample data for testing:
```bash
python sample_products.py
```

This creates `sample_products.xlsx` with 5 sample products.

### Running Tests

Run the automated test suite:
```bash
python test_inventory.py
```

All 10 tests should pass, validating:
- Import functionality
- View operations
- Search capabilities
- Add/update/delete operations
- Export functionality
- Filtered view calculations

## Project Structure

```
.
├── inventory_manager.py      # Main inventory management system
├── sample_products.py         # Script to generate sample data
├── test_inventory.py          # Automated test suite
├── sample_products.xlsx       # Sample product data
├── inventory_data.xlsx        # Current inventory database
├── README.md                  # This file
└── replit.md                  # Project documentation
```

## Data Persistence

All inventory data is automatically saved to `inventory_data.xlsx`. Your changes persist between sessions.

## Dependencies

- **pandas** - Excel file processing and data manipulation
- **openpyxl** - Reading and writing Excel files
- **tabulate** - Formatted table output in console

## Technical Details

- **Language**: Python 3.11
- **Data Storage**: Excel files (XLSX format)
- **Primary Library**: pandas DataFrame for data management
- **Interface**: Command-line interactive menu

## License

This project is open source and available for personal and commercial use.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.
