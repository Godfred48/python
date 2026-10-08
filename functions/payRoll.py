#function for average hours worked by employees
def calculate_average_hours(hours):
    total_hours = sum(hours)
    average_hours = total_hours / len(hours)
    return average_hours 

#funtion for total sales 
def calculate_total_sales(sales):
    total_sales = sum(sales)
    return total_sales 

#function for performance rating based on sales
def get_performance_rating(total_sales):
    if total_sales >= 9000:
        return "Excellent"
    elif total_sales >= 7000:
        return "Very Good"
    elif total_sales >= 5000:
        return "Good"
    elif total_sales >= 3000:
        return "Average"    
    else :
        return "Poor"

#function for bonus calculation 
def calculate_bonus(sales, performance, average_hours):
    if performance == "Excellent":
        bonus = 0.15 * sales
    elif performance == "Very Good":
        bonus = 0.10 * sales
    elif performance == "Good":
        bonus = 0.07 * sales
    elif performance == "Average":
        bonus = 0.04 * sales
    else:
        bonus = 0

    # Adjust bonus based on average hours worked
    if average_hours < 7:
        bonus -= 0.5  #50% deduction from bonus

    return bonus

#function for top performer
def find_top_performer(employee_names, total_sales):
    top_sales = max(total_sales)
    top_performer = employee_names[total_sales.index(top_sales)]
    return top_performer, top_sales


