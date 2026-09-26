# ============================================================
# VOLTRELAY ENERGY
# DATA CLEANING FUNCTIONS
# ============================================================

import pandas as pd
import numpy as np


def quality_summary(df, dataset_name):
    """
    Create a data-quality summary for a dataframe.
    """

    summary = pd.DataFrame({
        "Column": df.columns,
        "Data Type": df.dtypes.astype(str).values,
        "Missing Count": df.isna().sum().values,
        "Missing %": (df.isna().mean() * 100).round(2).values,
        "Unique Values": df.nunique(dropna=True).values
    })

    summary.insert(0, "Dataset", dataset_name)

    return summary


def duplicate_summary(df, dataset_name):
    """
    Check exact duplicate rows.
    """

    total_rows = len(df)
    duplicate_rows = int(df.duplicated().sum())

    duplicate_pct = (
        duplicate_rows / total_rows * 100
        if total_rows > 0
        else 0
    )

    return {
        "Dataset": dataset_name,
        "Total Rows": total_rows,
        "Duplicate Rows": duplicate_rows,
        "Duplicate %": round(duplicate_pct, 2)
    }


def standardize_city_names(df, column="city"):
    """
    Standardize city names by removing extra spaces
    and applying consistent capitalization.
    """

    df = df.copy()

    if column in df.columns:
        df[column] = (
            df[column]
            .astype("string")
            .str.strip()
            .str.title()
        )

    return df


def convert_datetime(df, column):
    """
    Convert a column to pandas datetime safely.
    """

    df = df.copy()

    if column in df.columns:
        df[column] = pd.to_datetime(
            df[column],
            errors="coerce"
        )

    return df


def remove_exact_duplicates(df):
    """
    Remove exact duplicate rows.
    """

    return df.drop_duplicates().copy()


def missing_value_summary(df):
    """
    Return columns containing missing values.
    """

    result = pd.DataFrame({
        "Missing Count": df.isna().sum(),
        "Missing %": (df.isna().mean() * 100).round(2)
    })

    return result[result["Missing Count"] > 0].sort_values(
        "Missing %",
        ascending=False
    )