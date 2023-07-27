import pandas as pd
from prophet import Prophet
from alpha_vantage.timeseries import TimeSeries

ts = TimeSeries(key='LKX8H74DNJAAK2JC')

symbol = input("Enter the stock symbol: ")
data, meta_data = ts.get_daily(symbol=symbol, outputsize='compact')

df = pd.DataFrame.from_dict(data).T
df = df[['4. close']]

closing_data = df.head(100)

df = pd.DataFrame(closing_data)
df.reset_index(inplace=True)
df = df.rename(columns={'index': 'ds', '4. close': 'y'})

closing_data = df.head(100)

m = Prophet()
m.fit(df)

#next day dataframe
future = m.make_future_dataframe(periods=1)
#next day prediction
forecast = m.predict(future)
next_day = forecast.iloc[-1]['yhat']

# next week dataframe
future_week = m.make_future_dataframe(periods=7)

#next week prediction
forecast_week = m.predict(future_week)
next_week = forecast_week.iloc[-1]['yhat']

#next month dataframe
future_month = m.make_future_dataframe(periods=30)

#next month prediction
forecast_month = m.predict(future_month)
next_month = forecast_month.iloc[-1]['yhat']

print(f"Next day prediction: {next_day:.2f}")
print(f"Next week prediction: {next_week:.2f}")
print(f"Next month prediction: {next_month:.2f}")
