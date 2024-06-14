# # main/management/commands/import_products.py
# from django.core.management.base import BaseCommand
# import pandas as pd
# # from main.models import Product
# from product.models import Product


# class Command(BaseCommand):
#     help = 'Import products from an Excel file'

#     def add_arguments(self, parser):
#         parser.add_argument('file_path', type=str)

#     def handle(self, *args, **kwargs):
#         file_path = kwargs['file_path']
#         df = pd.read_excel(file_path)
#         for _, row in df.iterrows():
#             Product.objects.get_or_create(
#                 name=row['name'],
#                 defaults={'amount': row['amount']}
#             )
#         self.stdout.write(self.style.SUCCESS('Successfully imported products'))

# your_app/management/commands/import_products.py

import pandas as pd
from django.core.management.base import BaseCommand
from product.models import Product


class Command(BaseCommand):
    help = 'Import products from an Excel file'

    def add_arguments(self, parser):
        parser.add_argument('excel_file', type=str,
                            help='Path to the Excel file')

    def handle(self, *args, **kwargs):
        excel_file = kwargs['excel_file']
        try:
            df = pd.read_excel(excel_file, engine='openpyxl')
            for index, row in df.iterrows():
                product_name = row['product_name']
                amount = row['amount']

                # Check if the product already exists
                product, created = Product.objects.get_or_create(
                    name=product_name, defaults={'amount': amount})

                if created:
                    self.stdout.write(self.style.SUCCESS(
                        f'Product "{product_name}" created successfully'))
                else:
                    self.stdout.write(self.style.WARNING(
                        f'Product "{product_name}" already exists'))

        except Exception as e:
            self.stderr.write(self.style.ERROR(
                f'Error importing products: {e}'))
