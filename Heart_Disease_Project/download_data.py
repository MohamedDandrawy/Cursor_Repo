import os
import sys
import csv
from pathlib import Path
from typing import List

import requests


DATA_DIR = Path(__file__).resolve().parent / "data"
TARGET_CSV = DATA_DIR / "heart_disease.csv"


def try_download(urls: List[str], target_path: Path) -> bool:
    target_path.parent.mkdir(parents=True, exist_ok=True)
    for url in urls:
        try:
            print(f"Attempting download: {url}")
            resp = requests.get(url, timeout=30)
            resp.raise_for_status()
            content = resp.text
            # Basic validation: ensure header contains expected columns
            if "age" in content and "sex" in content and ("target" in content or "HeartDisease" in content):
                target_path.write_text(content, encoding="utf-8")
                print(f"Downloaded dataset to {target_path}")
                return True
        except Exception as exc:
            print(f"Failed from {url}: {exc}")
    return False


def write_placeholder(target_path: Path) -> None:
    print("Writing placeholder sample dataset (10 rows) ...")
    header = [
        "age","sex","cp","trestbps","chol","fbs","restecg","thalach","exang","oldpeak","slope","ca","thal","target"
    ]
    rows = [
        [63,1,3,145,233,1,0,150,0,2.3,0,0,1,1],
        [37,1,2,130,250,0,1,187,0,3.5,0,0,2,1],
        [41,0,1,130,204,0,0,172,0,1.4,2,0,2,1],
        [56,1,1,120,236,0,1,178,0,0.8,2,0,2,1],
        [57,0,0,120,354,0,1,163,1,0.6,2,0,2,1],
        [57,1,0,140,192,0,1,148,0,0.4,1,0,1,1],
        [56,0,1,140,294,0,0,153,0,1.3,1,0,2,1],
        [44,1,1,120,263,0,1,173,0,0.0,2,0,3,1],
        [52,1,2,172,199,1,1,162,0,0.5,2,0,3,1],
        [57,1,2,150,168,0,1,174,0,1.6,2,0,2,1],
    ]
    target_path.parent.mkdir(parents=True, exist_ok=True)
    with target_path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(header)
        writer.writerows(rows)
    print(f"Placeholder written to {target_path}")


def main() -> int:
    urls = [
        # Common mirrors of the UCI Heart Disease (Cleveland) processed CSV
        "https://raw.githubusercontent.com/plotly/datasets/master/heart.csv",
        "https://raw.githubusercontent.com/dataprofessor/data/master/heart.csv",
        "https://raw.githubusercontent.com/GokuMohandas/MadeWithML/master/datasets/heart.csv",
    ]

    if TARGET_CSV.exists():
        print(f"Dataset already exists at {TARGET_CSV}")
        return 0

    success = try_download(urls, TARGET_CSV)
    if not success:
        write_placeholder(TARGET_CSV)
        print("Warning: Using placeholder sample; please replace with full dataset when available.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

