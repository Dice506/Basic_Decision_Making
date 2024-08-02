# Building on the initial base code, we now allow the user to enter multiple units.
# The system then schedules maintenance events based on the condition of each unit.
# This progression showcases the evolution from simple yes/no decisions to more integrated thinking, 
# such as assessing maintenance conditions and scheduling.
# We can continue to expand this decision-making process by incorporating factors like parts availability, labor requirements,
# and other elements critical to equipment planning. 
# Future enhancements could include integrating production information to provide detailed insights into equipment usage and maintenance needs.

def classify_maintenance(age_years, usage_hours, condition):
    if condition.lower() == 'poor':
        return "Immediate Maintenance Needed"
    elif age_years > 10 or usage_hours > 10000:
        return "Schedule for Maintenance"
    elif age_years > 5 or usage_hours > 5000:
        return "Regular Inspection Needed"
    else:
        return "In Good Condition"

def maintenance_priority(condition):
    # Assign numerical values to maintenance priorities for sorting
    priorities = {
        "Immediate Maintenance Needed": 1,
        "Schedule for Maintenance": 2,
        "Regular Inspection Needed": 3,
        "In Good Condition": 4
    }
    return priorities.get(condition, 4)  # Default to lowest priority if not found

# Get the number of units
num_units = int(input("Enter the number of units: "))

# Collect data for each unit
units = []
for i in range(num_units):
    print(f"\nEntering details for unit {i+1}:")
    equipment_age = int(input("Enter equipment age in years: "))
    equipment_usage = int(input("Enter usage hours: "))
    equipment_condition = input("Enter condition (Good, Fair, Poor): ")
    
    # Determine maintenance status
    maintenance_status = classify_maintenance(equipment_age, equipment_usage, equipment_condition)
    
    # Store unit details along with maintenance priority
    units.append({
        "Unit": i + 1,
        "Age": equipment_age,
        "Usage": equipment_usage,
        "Condition": equipment_condition,
        "Maintenance Status": maintenance_status,
        "Priority": maintenance_priority(maintenance_status)
    })

# Sort units by maintenance priority (lowest number indicates highest priority)
units.sort(key=lambda x: x["Priority"])

# Display sorted maintenance schedule
print("\nMai
