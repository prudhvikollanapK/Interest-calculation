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

1. **Clone Repository**

> git clone [<repository-url>](https://github.com/prudhvikollanapK/Interest-calculation.git)
cd interest


2. **Install Dependencies**


pip install -r requirements.txt



3. **Configure Django Settings**
- Update database settings in `settings.py` as per your environment.
- Ensure all required Django apps are properly configured.

4. **Run Migrations**


python manage.py migrate


5. **Load Sample Data (Optional)**
- If sample data is provided (`sample_data.xlsx`), load it into the database.

python manage.py loaddata sample_data.xlsx


6. **Start Django Development Server**

python manage.py runserver


7. **Access the Application**
- Open a web browser and go to `http://localhost:8000/interest/interest-report/` to view the interest report.
- Click on the "Export to Excel" button to download the interest report in Excel format.

## Usage

### Calculating Interest

1. **Interest Calculation Logic**
- The `calculate_interest_report` function in `views.py` calculates interest based on booking payment schedules and associated payment receipts.

2. **HTML Template (`interest_report.html`)**
- Displays the interest report in a tabular format.
- Uses Django template language to iterate through `report_data` and display relevant fields.

### Exporting to Excel

1. **Export Logic (`export_to_excel` in `views.py`)**
- Extracts the interest report data from the rendered HTML using `pd.read_html`.
- Converts the data into a Pandas DataFrame and exports it to an Excel file (`interest_report.xlsx`).

2. **Excel Export**
- Uses `xlsxwriter` as the engine to write the DataFrame to an Excel file with proper formatting.

### Error Handling

- The application includes basic error handling to manage exceptions during interest calculation and exporting.
- Errors are logged and appropriate error messages are displayed to users.

## Files and Directories

- **views.py**: Contains view functions for calculating interest, rendering HTML templates, and exporting data to Excel.
- **models.py**: Defines Django models for booking payment schedules, payment receipts, and other related entities.
- **templates/**: Directory containing HTML templates, including `interest_report.html`.
- **static/**: Directory for static files such as CSS for custom styling.

## Further Enhancements

- Improve error handling and validation during data import and calculation.
- Enhance user interface with additional filtering and sorting options for the interest report.
- Optimize performance for handling large datasets during interest calculation and export.

## Contributors

- [Your Name](https://github.com/your-username) - Initial development

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.



