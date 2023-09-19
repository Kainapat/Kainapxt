from datetime import datetime

# Set the target date
target_date = datetime(2024, 1, 22).date()

# Get today's date
today = datetime.today().date()

# Calculate the difference in days
difference = target_date - today

# Print the remaining days
print(f"Remaining days: {difference.days} days")