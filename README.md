\# Book Manager Django Project



\## Overview



A simple web application built using Django and PostgreSQL that allows users to perform CRUD operations on books via REST APIs. The project also integrates a third-party API to fetch book details and includes a basic data visualization for reporting.



\## Features



\* \*\*CRUD Operations\*\*: Create, Read, Update, Delete books.

\* \*\*API Integration\*\*: Fetch book details from Open Library API.

\* \*\*Data Visualization\*\*: Shows number of books per author using a bar chart.

\* \*\*Frontend\*\*: Simple HTML + JavaScript interface to interact with APIs.



\## Project Structure



```

myproject/              # Django project folder

&nbsp; myproject/            # Project settings

&nbsp; main/                 # App folder

&nbsp;   templates/          # Contains index.html

&nbsp;   views.py            # API views and homepage

&nbsp;   urls.py             # App URLs

&nbsp;   models.py           # Book model

&nbsp;   serializers.py      # DRF serializers

&nbsp; manage.py

requirements.txt        # Dependencies

.gitignore

README.md

```



\## Setup Instructions



\### 1. Clone Repository



```bash

git clone https://github.com/sharayumandke/book-manager-django.git

cd book-manager-django

```



\### 2. Create Virtual Environment



```bash

python -m venv venv

venv\\Scripts\\activate  # Windows

source venv/bin/activate # Linux/Mac

```



\### 3. Install Dependencies



```bash

pip install -r requirements.txt

```



\### 4. Database Setup



\* Configure PostgreSQL or Supabase credentials in `myproject/settings.py`.

\* Run migrations:



```bash

python manage.py makemigrations

python manage.py migrate

```



\### 5. Run Server Locally



```bash

python manage.py runserver

```



Open \[http://127.0.0.1:8000](http://127.0.0.1:8000) in your browser.



\## Usage



\* Use the forms on the homepage to Add, Update, or Delete books.

\* All books are displayed on the homepage with a chart showing the number of books per author.

\* The API endpoint `/api/books/` can be accessed directly for CRUD operations.



\## Deployment



\* The project is deployed on Render: \[https://book-manager-django.onrender.com](https://book-manager-django.onrender.com)

\* Remember to set `ALLOWED\_HOSTS` in `settings.py` for deployment:



```python

ALLOWED\_HOSTS = \['book-manager-django.onrender.com']

```



\## Demo API Integration



\* Endpoint: `/api/books/import/`

\* Method: POST

\* Payload example:



```json

{

&nbsp; "title": "Pride and Prejudice"

}

```



\* Adds book from Open Library API to your database.



\## Notes



\* Frontend uses JavaScript `fetch` to interact with APIs.

\* Chart.js is used for visualization.

\* Gunicorn is included for production deployment.



\## Author



Sharayu Mandke



