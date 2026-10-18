"""
RECORD CHECK  -  my version
===========================

Name  :
Lane  :  AI / Cyber / IT      (delete two)
Date  :

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""

# ==========================================================================
# 4. Before you finish:
#
#    [ ] Run it and check every record's numbers are correct by hand
#    [ ] If you are loading from a file, check what happens when the file
#        does not exist - write the error down
#    [ ] Check every function still does one job

def check_record(value: float, limit: float, base: float):
    """Calculate the difference and percentage."""
    difference = value - limit
    percentage = (value / base) * 100.0 if base != 0 else 0.0
    return difference, percentage


def status_of(percent: float) -> str:
    """Determine the status string based on the calculated percentage."""
    if percent >= 100.0:
        return "Target Met / Exceeded"
    elif percent >= 50.0:
        return "Pass Standard / Progressing"
    else:
        return "Below Standard"


def print_report(label: str, actual: float, target: float, base: float, diff: float, pct: float):
    """Generate and display the complete right-aligned bordered performance report."""
    status = status_of(pct)
    
    print("=" * 30)
    print(f"       PERFORMANCE REPORT: {label.upper()} ")
    print("=" * 30)
    print(f" Actual Value:     {actual:10.2f}")
    print(f" Target Value:     {target:10.2f}")
    print(f" Base Value:       {base:10.2f}")
    print("=" * 30)
    print(f" Difference:       {diff:10.2f}")
    print(f" Percentage:       {pct:10.2f}%")
    print("=" * 30)
    print(f" STATUS:           {status}")
    print("=" * 30)


def main():
    # List of dictionaries defining the records directly in the code
    records = [
        {"label": "Q1 Sales", "value": 12.0, "limit": 1000.0, "base": 10000.0},
        {"label": "Q2 Marketing", "value": 400.0, "limit": 5000.0, "base": 6000.0},
        {"label": "Q3 Production", "value": 500.0, "limit": 800.0, "base": 8000.0}
    ]
    
    over_limit_count = 0

    # Loop over your records and print a report for each
    for record in records:
        diff, pct = check_record(record["value"], record["limit"], record["base"])
        
        if diff > 0:
            over_limit_count += 1
            
        print_report(record["label"], record["value"], record["limit"], record["base"], diff, pct)

    print("=" * 30)
    print(f" TOTAL OVER LIMIT RECORDS: {over_limit_count}")
    print("=" * 30)


if __name__ == "__main__":
    main()
