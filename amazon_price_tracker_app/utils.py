import os
import pandas as pd 
from django.conf import settings 

def get_product_by_id(id):
    """
    Uses the id of the product to get the product from the excel file.
    
    Args:
        id (str): ID of the product

    Returns:
        Product: Product object with the ID of the product
    """
    excel_file_path = os.path.join(settings.BASE_DIR, "amazon_price_tracker_app/data/amazon_product_data.xlsx")
    try:
        excel = pd.ExcelFile(excel_file_path)
        if id in excel.sheet_names:
            sheet = pd.read_excel(excel_file_path, sheet_name=id)
            product = {
                "id": id,
                "name": sheet["name"][0],
                "description": sheet.get("description", ["No description"])[0],
                "price": sheet["price"].iloc[-1],
                "date": sheet["date"][0]
            }    
            return product
        else:
            return f"Product with ID {id} was not found."
    except Exception as e:
        print(f"Error reading Excel file : {str(e)}")
        return None

def get_all_products() -> list:
    """
    Fetches all products from the Excel file.

    Returns:
        list: All products from the Excel file
    """
    excel_file_path = os.path.join(settings.BASE_DIR, "amazon_price_tracker_app/data/amazon_product_data.xlsx")
    all_products = []
    try:
        excel = pd.ExcelFile(excel_file_path)
        for sheet_name in excel.sheet_names:
            
            sheet = pd.read_excel(excel_file_path, sheet_name=sheet_name)

            product = {
                "id": sheet_name,
                "name": sheet["name"][0],
                "description": sheet.get("description", ["No description"])[0],
                "price": sheet["price"].iloc[-1],
                "date": sheet["date"][0]
            }
            all_products.append(product)
        return all_products
    except Exception as e:
        print(f"Error reading Excel file: {str(e)}")
        return []