import pandas as pd
import matplotlib.pyplot as plt


data ="Auto Sales data.csv"
df = pd.read_csv(data)

#print(df.tail(10))

df['ORDERDATE'] = pd.to_datetime(df['ORDERDATE'], dayfirst=True)

df['YEAR'] = df['ORDERDATE'].dt.year
sales_per_year = df.groupby('YEAR')['SALES'].sum()

#print(f'Sales per year: {sales_per_year}')


sales_by_product_line = df.groupby('PRODUCTLINE')['SALES'].sum()

#print(f'Sales by product line: {sales_by_product_line}')

# plt.figure(figsize=(10, 6))
# sales_per_year.plot(kind='line', marker='o', color='b', linestyle='-', linewidth='2', label='Sales per year', markersize=8)
# plt.title('Sales Treand over tiome 2018-2020')
# plt.xlabel('Year')
# plt.ylabel('Total sales')
# plt.grid(True)
# plt.xticks(sales_per_year.index)
# plt.show()


# plt.figure(figsize=(12, 8))
# sales_by_product_line.plot(kind='bar', color='skyblue')
# plt.title('Sales bu Product line')
# plt.xlabel('Product line')
# plt.ylabel('Total sales')
# plt.xticks(rotation=0)
# plt.show()

#df['MONTH_YEAR'] = df['ORDERDATE'].dt.to_period('M')

#monthly_sales = df.groupby('MONTH_YEAR')['SALES'].sum()

#print(f'Monthly sales: {monthly_sales}')

# plt.figure(figsize=(12, 8))
# monthly_sales.plot(kind='line', marker='o', color='green', linestyle='-', linewidth=2, markersize=5)
# plt.title('Monthly sales trends')
# plt.xlabel('Monthly/YEAR')
# plt.ylabel('Total Sales')
# plt.xticks(rotation=0)
# plt.grid(True)
# plt.show()

# best_5_clients = df.groupby('CUSTOMERNAME')['SALES'].sum().sort_values(ascending=False).head(5)
# #print(best_5_clients)
# plt.figure(figsize=(12,8))
# ax = best_5_clients.plot(kind='bar', color='orange')
# plt.title('Top 5 customers', fontsize=20)
# plt.xlabel('Customers names', fontsize=12)
# plt.ylabel('Total sales', fontsize=12)
# plt.xticks(rotation=5)
# for p in ax.patches:
#     ax.annotate(f'$ {p.get_height():,.2f}', (p.get_x() + p.get_width() / 2., p.get_height()), ha='center', va='center'
#                 , xytext=(0,10), textcoords='offset points', color='red')
#
# plt.show()

# best_sales_by_country = df.groupby('COUNTRY')['SALES'].sum().sort_values(ascending=False)
#
#
# plt.figure(figsize=(14,10))
# ax = best_sales_by_country.plot(kind='bar', color='blue')
# plt.title('Sales by countries', fontsize=20)
# plt.xlabel('Country name', fontsize=12)
# plt.ylabel('Total sales', fontsize=12)
# plt.xticks(rotation=45)
# for p in ax.patches:
#      ax.annotate(f'$ {p.get_height():,.2f}', (p.get_x() + p.get_width() / 2., p.get_height()), ha='center', va='center'
#                  , xytext=(0,10), textcoords='offset points', color='red', rotation=90)
#
# plt.show()
customer_sales = df.groupby('CUSTOMERNAME')['SALES'].sum().sort_values(ascending=False)

quantiles = customer_sales.quantile(q=[0.25, 0.5, 0.75])

def segment_customers(x, q):
    if x <= q [0.25]:
        return 'Zemiausias segmentas'
    elif x <= q [0.5]:
        return 'Vidutinis/zemas segmentas'
    elif x <=q [0.75]:
        return 'Vidutinis/aukstas segmentas'
    else:
        return 'Auksciausias segmentas'

customer_segments = customer_sales.apply(segment_customers, q=quantiles)

segment_counts = customer_segments.value_counts()

plt.figure(figsize=(10, 6))
segment_counts.plot(kind='bar', color='blue')
plt.title('Klientu segmentavimas pagal pardavimus')
plt.xlabel('Segmentas')
plt.xticks(rotation=5)
plt.ylabel('Klientu skaicius')
plt.show()

print(segment_counts)
