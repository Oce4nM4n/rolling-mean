import pandas as pd

predictedmonths= 6

data = pd.read_csv('data.csv')


print("----------")
customers = data['customerid'].unique()

for customer in customers:
	print(f"Customer ID: {customer}")
	customer_data = data[data['customerid']==customer]
	resources = customer_data['resourceid'].unique()

	for resource in resources:
		print(f"Resource ID: {resource}")

		for i in range(predictedmonths):
			resource_data = data[(data['customerid'] == customer) & (data['resourceid'] == resource)]

			latest_months = sorted(resource_data['month'].unique() ,reverse=True)[:3]
			print(f"Latest months: {latest_months}")

			forecasted_cost = resource_data[resource_data['month'].isin(latest_months)]['cost'].mean()

			forecasted_data = pd.DataFrame({
				'customerid': customer,
				'resourceid': resource,
				'cost': forecasted_cost,
				'month': latest_months[0] + 1
			}, index=[0])

			print(f"Forecasted data for customer {customer}, resource {resource}:")
			print(forecasted_data.head())

			data = pd.concat([data, forecasted_data], ignore_index=True)
			print("\n")

data.to_csv('forecasted_data.csv', index=False)
