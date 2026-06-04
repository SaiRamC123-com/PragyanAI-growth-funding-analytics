import pandas as pd

def generate_excel(df):

    path = (
        "reports/generated_reports/"
        "startup_report.xlsx"
    )

    with pd.ExcelWriter(path) as writer:

        df.to_excel(
            writer,
            sheet_name="Dataset",
            index=False
        )

    return path
