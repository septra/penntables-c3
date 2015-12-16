import pandas as pd

def transform(frame, key_column, x_column, y_column):
    import json
    xs = {
            str(key_val): str(key_val)+"_x" for key_val in
            frame[key_column].unique()
        }
    columns = []
    for key, val in xs.items():
        columns.append(
            [key] + list(frame.loc[frame[key_column] == key, y_column])
        )
        columns.append(
            [val] + list(frame.loc[frame[key_column] == key, x_column])
        )
    data = {"xs" : xs, "columns" : columns}
    return json.dumps(data, indent = 2)

penn = pd.read_csv('./PennTablesGA.csv')

files = {var: dataframe for var, dataframe in
            zip(
                penn['VariableCode'].unique(),
                map(
                    lambda x: penn.loc[penn['VariableCode'] == x],
                    penn['VariableCode'].unique()
                )
            )
        }

# Iterate over filenames and save corresponding dataframes to json files.
for fname, dataframe in files.items():
    with open(str(fname) + ".json", 'wb') as f:
        f.write(transform(dataframe, "RegionCode", "YearCode", "AggValue"))
