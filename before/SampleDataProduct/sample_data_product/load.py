def save_dataframe_to_delta(df, path):
    df.write_delta(path)