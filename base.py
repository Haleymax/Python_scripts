import pandas as pd

def convert_to_excel(data):
    # Extract the 'list' key from the data
    data_list = data['data']['list']

    # Filter the data for director_name equals to "黄宏伟"
    filtered_data = [entry for entry in data_list if entry.get('director_name') == '黄宏伟']

    # Convert the filtered data to DataFrame
    df = pd.DataFrame(filtered_data)

    # Write DataFrame to Excel file
    excel_file = "filtered_data.xlsx"
    df.to_excel(excel_file, index=False)

    return excel_file


