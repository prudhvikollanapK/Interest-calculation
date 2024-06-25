# Interest Calculation and Exporting Application

## Overview

This Django application calculates interest on booking payment schedules based on functionality and shown in frontend table and to export the interest report to an Excel file.

### Features

- **Interest Calculation**: Calculates interest based on delayed payment details associated with booking payment schedules.
- **Export to Excel**: Generates an Excel file containing the interest report for download.

### Dependencies

- Python
- Django
- pandas
- xlsxwriter

### Setup Instructions

1. **Clone Repository :** 
    > git clone [<repository-url>](https://github.com/prudhvikollanapK/Interest-calculation.git)
cd Interest-calculation

2. **Install Dependencies :**
    > pip install -r requirements.txt

3. **Run Migrations :**
    > python manage.py makemigrations interest
    
    > python manage.py migrate

4. **Create superuser :**
    > python manage.py createsuperuser

5. **Start Django Development Server :**
    > python manage.py runserver

6. **Inject excel Data :**
    > python manage.py import_data DATA.xlsx

7. **Access the Application**
- Open browser and hit `http://localhost:8000/interest/interest-report/` to view the interest report table.
- Click on the "Export to Excel" button to download the interest report in Excel format.

8. **Database Adminstrator :**
![image](https://github.com/prudhvikollanapK/Interest-calculation/assets/86195686/c1459137-6fac-4173-87e5-d28d3347ed0b)
![image](https://github.com/prudhvikollanapK/Interest-calculation/assets/86195686/1789ef11-ff87-451e-acdd-672a6ad8fab1)





