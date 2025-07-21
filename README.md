# JalaliPy Timber Analytics

## Description
**JalaliPy Timber Analytics** is a Python-based open-source project for analyzing timber industry sales and purchase data, created on July 21, 2025. It leverages the Jalali calendar for localized date handling, alongside libraries like `pandas`, `numpy`, and `seaborn` to provide deep insights into top customers, suppliers, monthly trends, and inventory management. The project includes a Jupyter Notebook (`analyze.ipynb`) and a helper module (`helper.py`) for reusable functions. It is compatible with Python 3.11+ and includes all dependencies in `requirements.txt`.

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
- **Visualization**: Uses `seaborn` and `matplotlib` to create bar charts for key metrics.
- **Reusable Code**: Includes a `helper.py` module with functions like `to_jalali_date` and `detect_outliers`.

## Requirements
To run this project, you need the following dependencies:
- `pandas==2.2.2`
- `numpy==1.26.4`
- `jdatetime==3.8.2`
- `jalali-pandas==0.2.1`
- `prettytable==3.10.0`
- `seaborn==0.13.2`
- `matplotlib==3.8.4`

These are listed in the `requirements.txt` file. Ensure you have Python 3.11+ installed.

## Installation
Follow these steps to set up the project:

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-username/JalaliPy-Timber-Analytics.git