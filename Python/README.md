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
  - To exit use ctrl+c.

## Example Output
The script provides output in the format: "The day of the week for YYYY-MM-DD is [Day]."

## Sample Run
Here is an example of how the script works:
```python
# Sample Run
Enter year or ctrl+c to exit:1900
Enter month or ctrl+c to exit::2
Enter date or ctrl+c to exit::28
The day of the week for 1900-02-28 is Wednesday.
```
