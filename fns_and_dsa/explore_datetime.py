from datetime import datetime, timedelta

def display_current_datetime():
    #get the current date and time
    current_date = datetime.now()

    #format the current date and time as "YYYY-MM-DD HH:MM:SS"
    formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")

    print(f"Current date and time: {formatted_date}")

def calculate_future_date():
    current_date = datetime.now()

    days_to_add = int(input("Enter the number of days to add to the current date: "))

    future_date = current_date + timedelta(days_to_add)

    formatted_future_date = future_date.strftime("%Y-%m-%d")

    print(f"Future date: {formatted_future_date}")

if __name__ == "__main__":
    display_current_datetime()

    calculate_future_date()
