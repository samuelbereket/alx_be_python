

# Prompt user for inputs
task = input("Enter the task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound (yes/no)").lower()

# Process with match-case
match priority:
    case "high":
        reminder = f"Reminder: '{task}' is a HIGH priority task."
    case "medium":
        reminder = f"Reminder: '{task}' is a MEDIUM priority task."
    case "low":
        reminder = f"Reminder: '{task}' is a LOW priority task."
    case _:
        reminder = f"Reminder: '{task}' has an UNKNOWN priority."

# Check if time-bound
if time_bound == "yes":
    reminder += " This task requires immediate attention today!"

# Print the customized reminder
print(reminder)
