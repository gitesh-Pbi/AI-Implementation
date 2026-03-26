import pandas as pd


def load_data(file_path: str):
    """
    Load CSV or Excel file into a pandas DataFrame
    """

    try:
        if file_path.endswith(".csv"):
            df = pd.read_csv(file_path)

        elif file_path.endswith(".xlsx"):
            df = pd.read_excel(file_path)

        else:
            raise ValueError("Unsupported file format. Use CSV or Excel.")

        print(f"✅ Data loaded successfully: {file_path}")
        print(f"📊 Rows: {df.shape[0]}, Columns: {df.shape[1]}")

        return df

    except Exception as e:
        raise RuntimeError(f"Error loading file: {str(e)}")