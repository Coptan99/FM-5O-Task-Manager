import pandas as pd
import numpy as np


start_date = '2023-11-01'
end_date = '2024-01-31'
date_range = pd.date_range(start=start_date, end=end_date, freq='D')


calendar_schedule = pd.DataFrame(index=date_range)


events = ['Meeting ', 'task done ', 'No Event']

for date in date_range:
    calendar_schedule.loc[date, 'Event'] = np.random.choice(events)


with pd.option_context('display.max_rows', None, 'display.max_columns', None):
    print("Generated Calendar Schedule:")
    print(calendar_schedule)
