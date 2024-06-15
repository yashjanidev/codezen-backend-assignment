# codezen-backend-assignment

## Steps to install and run the project

1. Clone the repository

```bash
git clone
```

2. Install the dependencies

```bash
pip install -r requirements.txt
```

3. Run the server

```bash
python manage.py runserver
```

4. Importing Excel file

```bash
python manage.py import_products product/excelfile/Product_data.xlsx
```

5. Start Celery worker

```bash
celery -A api worker --loglevel=info
```

6. Start Celery beat

```bash
celery -A api beat --loglevel=info
```

7. Api Endpoints
    
    ```bash
    1. http://127.0.0.1:8000/
    2. http://127.0.0.1:8000/products/
    2. http://127.0.0.1:8000/orders/
    ```
