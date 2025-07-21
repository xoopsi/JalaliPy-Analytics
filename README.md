# JalaliPy  Analytics

## Description
**JalaliPy  Analytics** is a Python-based open-source project for analyzing timber industry sales and purchase data. It leverages the Jalali calendar for localized date handling, alongside libraries like `pandas`, `numpy`, etc. This project provides deep insights into top customers, suppliers, monthly trends, and inventory management. The project includes a Jupyter Notebook (`analyze.ipynb`) and a helper module (`helper.py`) for reusable functions. It is compatible with Python 3.11+ and includes all dependencies in `requirements.txt`.

## Table of Contents
- [Overview](#overview)
- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [File Structure](#file-structure)
- [Data](#data)
- [Contributing](#contributing)
- [Troubleshooting](#troubleshooting)
- [Development Notes](#development-notes)
- [License](#license)
- [Contact](#contact)
- [Acknowledgments](#acknowledgments)

## Overview
This project was developed to assist businesses in the timber industry with data-driven decision-making. It processes raw data from Excel files (`WoodInc-purchase.xlsx` and `WoodInc-sale.xlsx`) to generate actionable insights, such as identifying top-performing customers and suppliers, analyzing monthly sales patterns, and managing inventory levels. The use of the Jalali calendar makes it particularly suitable for users in regions using this calendar system.

## Features
- **Data Cleaning**: Removes empty columns, duplicate rows, and extra whitespace.
- **Jalali Date Conversion**: Converts dates to the Jalali calendar using `jdatetime` and `jalali_pandas`.
- **Customer Analysis**: Identifies the top 3 customers by net price, both overall and monthly.
- **Supplier Analysis**: Highlights the top 3 suppliers based on purchase net price.
- **Monthly Trends**: Provides monthly breakdowns of customer and supplier performance.
- **Inventory Management**: Calculates stock levels by comparing purchased and sold quantities.
- **Reusable Code**: Includes a `helper.py` module with functions like `to_jalali_date` and `detect_outliers`.

## Requirements
To run this project, you need the following dependencies:
- `pandas==2.2.2`
- `numpy==1.26.4`
- `jdatetime==3.8.2`
- `jalali-pandas==0.2.1`
- `prettytable==3.10.0`
- `prettytable==3.16.0`

These are listed in the `requirements.txt` file. Ensure you have Python 3.11+ installed.

## Installation
Follow these steps to set up the project:

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-username/JalaliPy-Analytics.git
   ```
   Replace your-username with your GitHub username.
   
2. **Navigate to the Project Directory**:
   ```bash
   cd JalaliPy-Analytics
   ```
3. **Install Dependencies**: Use pip to install the required packages:
   ```bash
   pip install -r requirements.txt
   ```
   Alternatively, for Conda users:
   ```bash
   conda install --file requirements.txt
   ```
4. **Prepare Data Files**:
   Place the data files (WoodInc-purchase.xlsx and WoodInc-sale.xlsx) in the data/ directory.
   If these files are not provided, create sample files with the same column structure (see Data section).
   
5. **Set Up Jupyter Notebook**: If not already installed, install Jupyter:
   ```bash
   pip install jupyter
   ```
   Then launch it:
   ```bash
   jupyter notebook
   ``` 

## Usage
   Open src/analyze.ipynb in Jupyter Notebook.
   Run all cells to execute the data analysis pipeline.
   Review the output, including tables and visualizations, to gain insights.
   Modify the notebook or helper.py to customize the analysis (see Development Notes).
   
## Example Output
   Top Customers: A table and bar chart showing the top 3 customers by net price.
   Inventory Levels: A summary of stock differences for each product.
   Monthly Trends: Lists of top customers and suppliers per month.
   
## File Structure

```text
JalaliPy-Analytics/
├── img/                  # pictures of persian questions
├── analyze.ipynb         # Main analysis notebook
├── helper.py             # Helper functions module
├── README.md             # Documentation
├── requirements.txt      # Dependency list
├── .gitignore            # Ignored files
└── LICENSE               # Project license
```
## Data
   **Source Files**: `WoodInc-purchase.xlsx` and `WoodInc-sale.xlsx` contain purchase and sales data, respectively.
   **Column Structure**:
      - **purchase_date**, **sale_date**: Dates in a compatible format (e.g., `YYYY/MM/DD`).
      - **supplier_name**, **customer_name**: Names of entities.
      - **item_name**, **quantity**, **net_price**: Product details and financials.
   > **Note**: These files are not included in the repository due to size and sensitivity.
   Users must provide their own data or use the sample structure. A sample data generator can be added upon request.

## Contributing
   We welcome contributions to improve this project! Here’s how to contribute:
   
      1. Fork the repository.
      2. Create a new branch (git checkout -b feature-branch).
      3. Make your changes and commit them (git commit -m "Add new feature").
      4. Push to the branch (git push origin feature-branch).
      4. Open a pull request on GitHub.
   Please ensure your code follows PEP 8 style guidelines and includes tests if applicable.

## License
   This project is licensed under the MIT License, allowing free use, modification, and distribution, provided the original copyright and license notice are included.
   
## Contact
For questions, bugs, or suggestions, please:

- Open an issue on GitHub.  
- Contact the author at [hadi.shirin@gmail.com](mailto:hadi.shirin@gmail.com)
   
## Acknowledgments
   - Thanks to the xAI community for inspiration and tools.
   - Special thanks to the developers of `pandas`, `numpy`, `jdatetime`, `jalali_pandas` and `prettytable` for their powerful libraries.
   - Gratitude to all contributors who will enhance this project in the future.

   
