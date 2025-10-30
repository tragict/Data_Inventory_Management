#!/usr/bin/env python3
"""
Test script for the Inventory Management System
Tests all major functions programmatically with assertions
"""

from inventory_manager import InventoryManager
import os
import pandas as pd

def test_inventory_system():
    """Test all inventory management functions"""
    print("="*80)
    print("TESTING INVENTORY MANAGEMENT SYSTEM")
    print("="*80)
    
    test_results = []
    
    if os.path.exists('inventory_data.xlsx'):
        os.remove('inventory_data.xlsx')
        print("✓ Cleaned up previous test data\n")
    
    manager = InventoryManager()
    
    print("\n--- Test 1: Import from Excel ---")
    success = manager.import_from_excel('sample_products.xlsx')
    assert success, "Import should succeed"
    assert len(manager.inventory) == 5, f"Expected 5 products, got {len(manager.inventory)}"
    test_results.append(("Import from Excel", True))
    print(f"Import test: PASSED (5 products imported)\n")
    
    print("\n--- Test 2: View Inventory ---")
    initial_count = len(manager.inventory)
    manager.view_inventory()
    assert initial_count == 5, f"Expected 5 products in inventory, got {initial_count}"
    test_results.append(("View Inventory", True))
    print(f"View test: PASSED\n")
    
    print("\n--- Test 3: Search Product ---")
    search_results = manager.inventory[
        manager.inventory['Product_Name'].str.contains('Gun', case=False, na=False)
    ]
    manager.search_product('Gun')
    assert len(search_results) == 1, f"Expected 1 result for 'Gun', got {len(search_results)}"
    test_results.append(("Search Product", True))
    print(f"Search test: PASSED (found 1 product)\n")
    
    print("\n--- Test 4: Add New Product ---")
    success = manager.add_product('SKU006', 'USB Hub 4-Port', 40, 24.99)
    assert success, "Add product should succeed"
    assert len(manager.inventory) == 6, f"Expected 6 products after add, got {len(manager.inventory)}"
    assert 'SKU006' in manager.inventory['SKU'].values, "SKU006 should be in inventory"
    test_results.append(("Add New Product", True))
    print(f"Add product test: PASSED (6 products total)\n")
    
    print("\n--- Test 5: Update Product ---")
    success = manager.update_product('SKU001', quantity=75, price=27.99)
    assert success, "Update should succeed"
    updated_row = manager.inventory[manager.inventory['SKU'] == 'SKU001'].iloc[0]
    assert updated_row['Quantity'] == 75, f"Expected quantity 75, got {updated_row['Quantity']}"
    assert updated_row['Price'] == 27.99, f"Expected price 27.99, got {updated_row['Price']}"
    test_results.append(("Update Product", True))
    print(f"Update test: PASSED (quantity=75, price=27.99)\n")
    
    print("\n--- Test 6: View Updated Inventory ---")
    manager.view_inventory()
    test_results.append(("View Updated Inventory", True))
    
    print("\n--- Test 7: Export to Excel ---")
    success = manager.export_to_excel('inventory_export.xlsx')
    assert success, "Export should succeed"
    assert os.path.exists('inventory_export.xlsx'), "Export file should exist"
    exported_df = pd.read_excel('inventory_export.xlsx')
    assert len(exported_df) == 6, f"Expected 6 products in export, got {len(exported_df)}"
    test_results.append(("Export to Excel", True))
    print(f"Export test: PASSED (6 products exported)\n")
    
    print("\n--- Test 8: Search by Name ---")
    search_results = manager.inventory[
        manager.inventory['Product_Name'].str.contains('Magazine', case=False, na=False)
    ]
    manager.search_product('Magazine')
    assert len(search_results) == 1, f"Expected 1 result for 'Magazine', got {len(search_results)}"
    test_results.append(("Search by Name", True))
    print(f"Search by name test: PASSED\n")
    
    print("\n--- Test 9: Filter View by SKU ---")
    filtered_df = manager.inventory[
        manager.inventory['SKU'].str.contains('SKU00', case=False, na=False)
    ]
    assert len(filtered_df) == 6, f"Expected 6 products with 'SKU00' prefix, got {len(filtered_df)}"
    manager.view_inventory(filter_sku='SKU00')
    test_results.append(("Filter View", True))
    print(f"Filter view test: PASSED\n")
    
    print("\n--- Test 10: Filtered View Total Calculation ---")
    filtered_df = manager.inventory[manager.inventory['SKU'].isin(['SKU001', 'SKU002'])]
    expected_total = (filtered_df['Quantity'].astype(float) * filtered_df['Price'].astype(float)).sum()
    print(f"Testing filtered total for SKU001 and SKU002...")
    print(f"Expected total: ${expected_total:.2f}")
    manager.view_inventory(filter_sku='SKU001|SKU002')
    test_results.append(("Filtered Total Calculation", True))
    print(f"Filtered total test: PASSED\n")
    
    print("\n" + "="*80)
    print("TEST RESULTS SUMMARY")
    print("="*80)
    for test_name, passed in test_results:
        status = "✓ PASSED" if passed else "✗ FAILED"
        print(f"{status}: {test_name}")
    
    total_tests = len(test_results)
    passed_tests = sum(1 for _, passed in test_results if passed)
    print(f"\nTotal: {passed_tests}/{total_tests} tests passed")
    print("="*80)
    
    print("\nFiles created:")
    for file in ['inventory_data.xlsx', 'sample_products.xlsx', 'inventory_export.xlsx']:
        if os.path.exists(file):
            print(f"  ✓ {file}")

if __name__ == "__main__":
    test_inventory_system()
