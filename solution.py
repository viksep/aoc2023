# open and read full calibration file content
with open('input.txt', 'r') as file:
    calibration_lines = file.readlines()

# start as 0
total_calibration_sum = 0

# going through each line
for line in calibration_lines:
    # taking the first and last digits
    first_digit = next((char for char in line if char.isdigit()), None)
    last_digit = next((char for char in reversed(line) if char.isdigit()), None)

    # Check if both are digits before building the 2 digit number
    if first_digit is not None and last_digit is not None:
        # building the 2 digit number
        calibration_value = int(first_digit + last_digit)

        # Add the calibration value to the total sum
        total_calibration_sum = total_calibration_sum + calibration_value

# total result
print("Total Calibration Sum:", total_calibration_sum)
