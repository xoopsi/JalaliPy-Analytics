import pandas as pd                     #pip install pandas
import numpy as np                      #pip install numpy
import jdatetime as jdt                 #pip install jdatetime
import jalali_pandas                    #pip install jalali_pandas
from prettytable import PrettyTable     #pip install prettytable
import re                               #Import the regular expression module  ===>  pip install re


def to_jalali_date(column, year_dir='L'): 

    if column.dtype == 'object':
        if '/' in column[0]:
            mod_col = [x.split('/') for x in column]
        elif '-' in column[0]:
            mod_col = [x.split('-') for x in column]
        elif '.' in column[0]:
            mod_col = [x.split('.') for x in column]
    elif column.dtype == 'int64':
        str_col = column.astype('str')
        if len(str(column[0])) == 8:
            if year_dir == 'L':
                mod_col = [[x[0:4], x[4:6], x[6:]] for x in str_col]
            elif year_dir == 'R':
                mod_col = [[x[0:2], x[2:4], x[4:]] for x in str_col]
        elif len(str(column[0])) == 6:
            mod_col = [[x[0:2], x[2:4], x[4:]] for x in str_col]

    if year_dir == 'L':
        year = [i[0] for i in mod_col]
        month = [i[1] for i in mod_col]
        day = [i[2] for i in mod_col]
    else:
        year = [i[2] for i in mod_col]
        month = [i[1] for i in mod_col]
        day = [i[0] for i in mod_col]

    if len(year[0]) == 2:
        if int(year[0]) < 50:
            year = ['14'+j for j in year]
        elif int(year[0]) > 50:
            year = ['13'+j for j in year]

    new_correct_date = []
    for n in range(len(year)):
        y = int(year[n])
        m = int(month[n])
        d = int(day[n])
        new_correct_date.append(jdt.date(y, m, d))
    return new_correct_date


# تعریف تابعی برای استریپ کردن کل اطلاعات در یک دیتافریم در همه سلول ها
def strip_dataframe(df):
    stripped_copy = df.copy()
    for col in df.columns:
        stripped_copy[col] = df[col].map(lambda x: x.strip() if isinstance(x, str) else x)
    print(
        "\033[1m"
        + f"====  >  Your dataframe with size {df.shape} has been"
        + "\033[32m"
        + " stripped."
        + "\033[0m"
    )
    return stripped_copy


# تعریف تابعی که ستون های بی ارزش یک دیتافریم را دراپ می کند
def drop_unvalued_columns(df):
    """
    ورودی تابع یک دیتافریم است
    سه تا دیتا فریم تولید می کند
    یک - ستون های کاملا خالی از دیتاست
    دو - ستون های پر شده با کاراکتر اسپیس با هر میزان دلخواه
    سه - ستون هایی که شامل یک مقدار مشخص برای کل سلول های ستون هستند
    و نهایتا فیلترهای بالا را تجمیع کرده و خروجی یک کپی از دیتاست ورودی است که ستون های فوق از آن دراپ شده است
    """
    # پیدا کردن ستون های کاملا خالی از دیتا ست ورودی
    df_empty_columns = [
        col for col in df.columns if df[col].isnull().all()
    ]
    
    # ستون های شامل یک یا چند کاراکتر فاصله در دیتا ست ورودی
    df_space_included_columns = [
        col
        for col in df.columns
        if df[col].replace(r"^\s+$", np.nan, regex=True).isnull().all()
    ]

    # ستون های با مقدار مساوی در دیتاست خرید
    df_same_fixedvalue_columns = [
        col for col in df.columns if df[col].nunique() == 1
    ]
    # ساخت یک کپی از دیتاست
    cleared_df = df.copy()

    # تجمیع فیلترهای بالا و دراپ از کپی دیتاست
    df_all_filtered = list(
        set(
            df_empty_columns
            + df_space_included_columns
            + df_same_fixedvalue_columns
        )
    )
    cleared_df = cleared_df.drop(columns=df_all_filtered)
    print("\033[1m" + "\033[32m" + "Your Data Frame is now Clean." + "\033[0m")
    print("\033[1m" + "=====  >  " + "\033[31m" + "Report" + "\033[0m")
    # هد جدول گزارش
    myTable = PrettyTable(["Filter", "Count", "Name(s)"])
    # ساخت ردیف های جدول گزارش
    myTable.add_row(["Empty", len(df_empty_columns), df_empty_columns])
    myTable.add_row(
        ["Space Included", len(df_space_included_columns), df_space_included_columns]
    )
    myTable.add_row(
        ["Fixed Value", len(df_same_fixedvalue_columns), df_same_fixedvalue_columns],
        divider=True,
    )
    myTable.add_row(
        [
            "\033[1m" + "Total" + "\033[0m",
            "\033[1m" + str(len(df_all_filtered)) + "\033[0m",
            df_all_filtered,
        ]
    )
    print(myTable)
    print("size before apply :", df.shape)
    print("size after apply : ", cleared_df.shape)
    return cleared_df


# تعریف تابعی که ردیف های تکراری را دراپ می کند
def drop_repeated_rows(df):
    rows_cleaning_df = df.copy()
    count_of_duplicated_rows = df.duplicated().sum()
    rows_cleaning_df.drop_duplicates(inplace=True)

    print(
        "\033[1m"
        + "====  >  Duplicated rows in your dataframe has been"
        + "\033[32m"
        + " droped."
        + "\033[0m"
    )
    print(
        "\033[1m"
        + "There were "
        + "\033[31m"
        + f"{str(count_of_duplicated_rows)}"
        + "\033[0m"
        + "\033[1m"
        + " duplicated rows."
        + "\033[0m"
    )
    print("size before apply :", df.shape)
    print("size after apply : ", rows_cleaning_df.shape)
    return rows_cleaning_df


# مشاهده اطلاعات مربوط به سلول های خالی جدول
def empty_cells_info(df):
    """
    input is a Data frame
    output is a table which gives informations about the count of empty celss for each columns and the Total for Data frame
    """
        
    null_matrix = df.isna()
    result = []
    sums = null_matrix.sum()
    total_nan = null_matrix.sum().sum()
    for col, sum in sums.items():
        result.append((col, sum))
    print("\033[1m" + "=====  >  " + "\033[31m" + "Report" + "\033[0m")
    print(f"Rows in data frame = \033[1;4;32m{str(len(df))}\033[0m")       
    table = PrettyTable()
    table.field_names = ["Column Name"] + [col for col, _ in result]
    table.add_row(["Number of Empty cells"] + [nan for _, nan in result])
    print(table)
    print(f"Total empty cells in this Data frame = \033[4;31m{str(total_nan)}\033[0m .")
    
# مشاهده اطلاعات مربوط به تعداد داده های مجزا در هر ستون
def count_distinct_values(df):
    """
    input is a Data frame.
    output is a table which gives informations about the number of unique values for each columns.
    """
    if not isinstance(df, pd.DataFrame):
        print("Your input should be a DataFrame. Please try again.")
        return
    result = []
    type_result = []
    for col in df.columns:
        dtype = str(df[col].dtypes)
        if dtype == 'object':
            dtype = "\033[31m" + dtype + "\033[0m"  # Red color for 'object'
        type_result.append(dtype)

    for col in df.columns:
        result.append((col, df[col].nunique()))

    print("\033[1m" + "=====  >  " + "\033[31m" + "Report" + "\033[0m")
    print(f"Rows in data frame = \033[1;4;32m{str(len(df))}\033[0m")
    table = PrettyTable()
    table.field_names = ["Column Name"] + [col for col, _ in result]
    table.add_row(["Number of unique values"] + [var for _, var in result])
    table.add_row(["Data type"] + type_result)
    print(table)

     
# در هر ستون از دیتاست که بعنوان ورودی می گیرد لیست  مقادیر دارای کاراکترهای ویژه و تعدادشان را برمیگرداند
def detect_special_values(column):
    if isinstance(column, pd.DataFrame):
        print("Your input argument is not a column. That is a DataFrame. Please try again.")
        return
    if column.dtypes != 'object':
        print("Your column type should be object. Please try another column.")
        return
    result = []
    for data in column:
        # Check if the value contains any special character or space using a regular expression
        pattern = r'[-+~!@#$%^&*()\s]'
        # If the value matches the pattern, append it to the output list
        if re.search(pattern, str(data)):
            result.append(data)
    if not result:
        print("Your Column seems \033[1;32mGOOD!\033[0m")
    else:
        result = pd.Series(result)
        result_table = result.value_counts()
        ptable = PrettyTable()
        # ptable.header_style = 'HEADER'
        ptable.field_names = ["Value", "Count"]
        for value, count in result_table.items():
            ptable.add_row([value, count])
        print(ptable)
        return result


# یک تابع برای پیدا کردن مقادیر پرت حاصل از ورود اشتباه اپراتور
def detect_outliers(*args):
    if len(args) != 2 or not isinstance(args[0], pd.DataFrame) or not isinstance(args[1], str):
        return "You should pass 2 arguments, arg[0] = your data frame and arg[1] = your specific column."
    df, column = args[0], args[1]
    if column not in df.columns:
        return "The provided column name does not exist in the DataFrame."
    Q1 = df[column].quantile(0.25)
    Q3 = df[column].quantile(0.75)
    IQR = Q3 - Q1
    outliers_df = df[(df[column] < (Q1 - 1.5 * IQR)) | (df[column] > (Q3 + 1.5 * IQR))]
    return outliers_df


if __name__ == "__main__":
    print("Running helper.py directly...")

    
    






