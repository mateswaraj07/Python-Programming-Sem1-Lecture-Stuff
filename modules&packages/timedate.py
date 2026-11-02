from datetime import datetime, timedelta
future_date = datetime.now() + timedelta(days=10)
past_date = datetime.now() - timedelta(days=10)
print("Future date:", future_date)
print("Past date:", past_date)

date1=datetime(2026, 11, 1)
date2=datetime(2026, 12, 16)
print("Difference between two dates:", date2 - date1)
print("Total days between two dates:", (date2 - date1).days)
print("Total seconds between two dates:", (date2 - date1).total_seconds())