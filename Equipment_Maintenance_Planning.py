# The code below demonstrates advanced decision-making for equipment maintenance events.
# It considers factors such as equipment age, usage hours, and condition, as assessed by a technician (more detailed analysis can be provided by the technician).
# The next goal is to develop an AI system that will evaluate the entire unit and plan maintenance schedules.
# This example showcases decision-making for a single unit; the inputs can be expanded to include specific components, company-specific maintenance schedules, and other relevant details.

def classify_maintenance(age_years, usage_hours, condition):
    if condition.lower() == 'poor':
        return "Immediate Maintenance Needed"
    elif age_years > 10 or usage_hours > 10000:
        return "Schedule for Maintenance"
    elif age_years > 5 or usage_hours > 5000:
        return "Regular Inspection Needed"
    else:
        return "In Good Condition"

# Example usage
equipment_age = int(input("Enter equipment age in years: "))
equipment_usage = int(input("Enter usage hours: "))
equipment_condition = input("Enter condition (Good, Fair, Poor): ")

maintenance_status = classify_maintenance(equipment_age, equipment_usage, equipment_condition)
print(f"The equipment status is: {maintenance_status}")
