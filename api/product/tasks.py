# from celery import shared_task
# import subprocess


# @shared_task
# def import_products_from_excel(excel_file_path):
#     subprocess.call(
#         ['python', 'manage.py', 'import_products', excel_file_path])


from __future__ import absolute_import, unicode_literals
from celery import shared_task
from product.models import Product
import pandas as pd


@shared_task
def import_products_from_excel(file_path):
    try:
        df = pd.read_excel(file_path)
        for index, row in df.iterrows():
            Product.objects.create(
                name=row['Product_Name'], amount=row['Amount'])
    except Exception as e:
        print(f"Error importing products: {e}")
