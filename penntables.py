# Function to transform the Penn World Tables into json acceptable by NVD3
# Returns an appropriate json string
def transform_nvd3(frame, key_column, x_column, y_column):
    import json
    data = []
    for key in frame[key_column].unique():
        holder = {"key": key}
        holder.update(
            {
                "values": [
                    [x, y] for x, y in zip(frame[x_column], frame[y_column])
                ]
            }
        )
        data.append(holder)
    return json.dumps(data, sort_keys=True)


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
