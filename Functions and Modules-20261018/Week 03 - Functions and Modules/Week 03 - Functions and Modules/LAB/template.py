"""
RECORD CHECK  -  my version
===========================

Name  : Munashe Mapara
Lane  : Cyber     (delete two)
Date  :

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""

30
# ==========================================================================
# 5. Before you finish:
#
#    [ ] Run it three times with different numbers
#    [ ] Run it with a total of 0 and note the error (do not fix it yet)
#    [ ] Check every function does one job - if a function both calculates
#        and prints, split it

def check(value: float, limit: float, base: float):
    """Calculate the difference and percentage based on the provided limits."""
    difference = value - limit
    
    # Prevent division by zero if base is 0
    if base != 0:
        percentage = (value / base) * 100.0
    else:
        percentage = 0.0
        
    return difference, percentage


def status_of(percent: float) -> str:
    """Determine the status string based on the calculated percentage."""
    if percent >= 100.0:
        return "Target Met / Exceeded"
    elif percent >= 50.0:
        return "Pass Standard / Progressing"
    else:
        return "Below Standard"


def print_report(actual: float, target: float, base: float, diff: float, pct: float):
    """Generate and display the complete bordered performance report."""
    status = status_of(pct)
    
    print("=" * 34)
    print("             PERFORMANCE REPORT          ")
    print("=" * 34)
    print(f" Actual Value:     {actual:10.2f}")
    print(f" Target Value:     {target:10.2f}")
    print(f" Base Value:       {base:10.2f}")
    print("=" * 34)
    print(f" Difference:       {diff:10.2f}")
    print(f" Percentage:       {pct:10.2f}%")
    print("=" * 34)
    print(f" STATUS:           {status}")
    print("=" * 34)


def main():
    over_limit_count = 0

    while True:
        print("--- Enter Record Data (Type 'quit' to exit) ---")
        user_input = input("Enter Actual value (or 'quit'): ").strip().lower()
        
        if user_input == 'quit':
            break
            
        try:
            # Parse the inputs
            actual = float(user_input)
            target = float(input("Enter Target value: "))
            base = float(input("Enter Base value:   "))
            
            # Call check to get the difference and percentage
            difference, percentage = check(actual, target, base)
            
            # Track if the record exceeded the limit target
            if difference > 0:
                over_limit_count += 1
                
            # Direct all printing to print_report
            print_report(actual, target, base, difference, percentage)
            
        except ValueError:
            print("❌ Invalid input! Please enter numbers only.\n")

    # Final summary printed once after the loop terminates
    print("=" * 34)
    print(f" TOTAL OVER LIMIT RECORDS: {over_limit_count}")
    print("=" * 34)


if __name__ == "__main__":
    main()
