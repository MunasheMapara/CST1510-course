"""
RECORD CHECK  -  my version
===========================

Name  : Munashe Mapara
Lane  : Cyber  
Date  : 18/10/2026
"""
label = print(input("Enter label: "))
first = float(input("Enter first value: "))
second = float(input("Enter second value: "))

print()
print("=" * 34)
print(f"  RECORD CHECK  -  {label}")
print("=" * 34)

difference = first - second
percent = (first / second) * 100

print(f"Difference: {difference:>+10.2f}")
print(f"Percent of second: {percent:>+10.2f}")
#Useful:   f"{value:>10.2f}"  means: right-aligned, 2 decimal places ,f"{value:>+10.2f}"  means: the same, but always shows the sign

print("=" * 34)


# =================================================================== OUTPUT
# 3. Print the report.
#
#    Threshold : print the three values you were given, inside a border
#    Typical   : add difference and percent, 2 decimal places, right-aligned
#    Excellent : difference always shows its sign, plus one line of your own
#
#    Useful:   f"{value:>10.2f}"    right-aligned, 2 decimal places
#              f"{value:>+10.2f}"   the same, but always shows the sign


# ==========================================================================
# 4. Before you finish:
#
#    [ ] Run it three times with different numbers
#    [ ] Run it with a total of 0 and write the error in your journal
#    [ ] Check every variable name says what it holds
#    [ ] Show it to the person next to you
