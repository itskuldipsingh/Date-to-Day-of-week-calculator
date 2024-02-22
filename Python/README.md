# Date to Day of Week Calculator
This Python script calculates the day of the week for a given date.

## How to Use
1. Run the [script](https://github.com/itskuldipsingh/Date-to-Day-of-week-calculator/blob/main/Python/WeekOfDayCalculator.py) in a Python environment.
2. Enter the year, month, and date when prompted.
3. The script will output the corresponding day of the week for the entered date.

## Input Validation
The script ensures valid input for the year (between 0 and 9999), month (between 1 and 12), and date based on the selected month and leap year status.

## Code Structure
- The script is organized into sections:
  - Input validation for year, month, and date.
  - Determining leap year status.
  - Calculating the century code.
  - Assigning month codes based on leap year status.
  - Applying Zeller's Congruence formula to find the day of the week.

## Example Output
The script provides output in the format: "The day of the week for YYYY-MM-DD is [Day]."

## Sample Run
Here is an example of how the script works:
```python
# Sample Run
Enter year: 2022
Enter month: 2
Enter date: 22
The day of the week for 2022-02-22 is Tuesday.
```
Feel free to use, modify, and enhance the script as needed. If you encounter any issues or have suggestions, please let us know.
