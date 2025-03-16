import pandas as pd


def read_excel(file_path):
    try:
        df = pd.read_excel(file_path, engine="openpyxl")  # Явно указываем движок
        required_columns = {"title", "url", "xpath"}
        if not required_columns.issubset(df.columns):
            raise ValueError(
                f"Файл должен содержать столбцы: {', '.join(required_columns)}"
            )
        return df
    except Exception as e:
        raise ValueError(f"Ошибка при чтении файла: {e}")
