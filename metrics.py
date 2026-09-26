# ============================================================
# VOLTRELAY ENERGY
# KPI / METRIC FUNCTIONS
# ============================================================

import pandas as pd
import numpy as np


def calculate_swap_metrics(df):
    """
    Calculate basic swap-network performance metrics.
    """

    total_attempts = len(df)

    if "event_type" not in df.columns:
        return {
            "total_attempts": total_attempts,
            "completed_swaps": 0,
            "failed_swaps": 0,
            "abandoned_swaps": 0,
            "cancelled_swaps": 0,
            "failure_rate_pct": np.nan
        }

    event_type = (
        df["event_type"]
        .astype("string")
        .str.strip()
        .str.lower()
    )

    completed_swaps = int(
        event_type.eq("swap_completed").sum()
    )

    failed_no_battery = int(
        event_type.eq("failed_no_charged_battery").sum()
    )

    failed_system_error = int(
        event_type.eq("failed_system_error").sum()
    )

    abandoned_swaps = int(
        event_type.eq("abandoned_queue").sum()
    )

    cancelled_swaps = int(
        event_type.eq("cancelled_by_rider").sum()
    )

    failed_swaps = (
        failed_no_battery
        + failed_system_error
    )

    unsuccessful_attempts = (
        failed_swaps
        + abandoned_swaps
        + cancelled_swaps
    )

    failure_rate = calculate_failure_rate(
        total_attempts,
        unsuccessful_attempts
    )

    return {
        "total_attempts": total_attempts,
        "completed_swaps": completed_swaps,
        "failed_swaps": failed_swaps,
        "failed_no_charged_battery": failed_no_battery,
        "failed_system_error": failed_system_error,
        "abandoned_swaps": abandoned_swaps,
        "cancelled_swaps": cancelled_swaps,
        "unsuccessful_attempts": unsuccessful_attempts,
        "failure_rate_pct": failure_rate
    }


def calculate_failure_rate(total_attempts, failed_attempts):
    """
    Calculate unsuccessful attempt rate as a percentage.
    """

    if total_attempts == 0:
        return np.nan

    return (
        failed_attempts / total_attempts
    ) * 100


def calculate_margin_per_swap(margin, completed_swaps):
    """
    Calculate contribution margin per completed swap.
    """

    if completed_swaps == 0:
        return np.nan

    return margin / completed_swaps


def process_swap_file(file_path, chunksize=250_000):
    """
    Process the large swap_events.csv file in chunks.

    This avoids loading the entire ~3.9M-row file into memory.
    """

    total_attempts = 0
    completed_swaps = 0

    failed_no_battery = 0
    failed_system_error = 0

    abandoned_swaps = 0
    cancelled_swaps = 0

    chunks_processed = 0

    for chunk in pd.read_csv(
        file_path,
        chunksize=chunksize,
        low_memory=False
    ):

        chunks_processed += 1

        total_attempts += len(chunk)

        event_type = (
            chunk["event_type"]
            .astype("string")
            .str.strip()
            .str.lower()
        )

        completed_swaps += int(
            event_type.eq("swap_completed").sum()
        )

        failed_no_battery += int(
            event_type.eq(
                "failed_no_charged_battery"
            ).sum()
        )

        failed_system_error += int(
            event_type.eq(
                "failed_system_error"
            ).sum()
        )

        abandoned_swaps += int(
            event_type.eq("abandoned_queue").sum()
        )

        cancelled_swaps += int(
            event_type.eq("cancelled_by_rider").sum()
        )

        print(
            f"Processed chunk {chunks_processed} | "
            f"Rows processed: {total_attempts:,}"
        )

    failed_swaps = (
        failed_no_battery
        + failed_system_error
    )

    unsuccessful_attempts = (
        failed_swaps
        + abandoned_swaps
        + cancelled_swaps
    )

    failure_rate = calculate_failure_rate(
        total_attempts,
        unsuccessful_attempts
    )

    return {
        "total_attempts": total_attempts,
        "completed_swaps": completed_swaps,
        "failed_swaps": failed_swaps,
        "failed_no_charged_battery": failed_no_battery,
        "failed_system_error": failed_system_error,
        "abandoned_swaps": abandoned_swaps,
        "cancelled_swaps": cancelled_swaps,
        "unsuccessful_attempts": unsuccessful_attempts,
        "failure_rate_pct": failure_rate,
        "chunks_processed": chunks_processed
    }