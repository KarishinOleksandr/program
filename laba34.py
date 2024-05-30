import pandas as pd

df = pd.read_csv('phone_data.csv')
print(df.head(10))

print(df.shape)

print(df.dtypes)

df['date'] = pd.to_datetime(df['date'], format='%d/%m/%y %H:%M')
print(df.dtypes)

longest_call = df[df['item'] == 'call']['duration'].max()
print(f'Longest call was {longest_call} second.')

longest_data = df[df['item'] == 'data']['duration'].max()
print(f'Longest date insert was {longest_data} second.')

total_call_duration = df[df['item'] == 'call']['duration'].sum()
total_call_duration_hour = float(total_call_duration/3600)
print(f'\n Total amount of phone call was {total_call_duration_hour} hour.')

monthly_items = df.groupby('month')['item'].count()
print(monthly_items)

first_records_per_month = df.groupby('month').first()
print(first_records_per_month)

monthly_call_duration = df[df['item'] == 'call'].groupby('month')['duration'].sum()
print(monthly_call_duration)

network_call_duration = df[df['item'] == 'call'].groupby('network')['duration'].sum()
print('\n',network_call_duration)

monthly_counts = df.groupby(['month', 'item']).size().unstack(fill_value=0)
print(monthly_counts)

monthly_network_counts = df.groupby(['month', 'network_type', 'item']).size().unstack(fill_value=0)
print(monthly_network_counts)
