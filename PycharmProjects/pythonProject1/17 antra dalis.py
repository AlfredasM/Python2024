import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('properties.csv')

stats = df.describe()


#
# plt.figure(figsize=(10, 6))
# sns.histplot(df['price'], bins=10, kde=True)
# plt.title('Kainu pasiskirstimas')
# plt.xlabel('Kaina')
# plt.ylabel('Daznis')
# plt.grid(True)
# plt.show()


def categorize_property(title):
    if 'Commercial' in title:
        return 'Commercial'
    elif 'Apartment' in title:
        return 'Apartment'
    elif 'Villa' in title:
        return 'Villa'
    elif 'Town House' in title:
        return 'Town House'
    else:
        return 'Other Residential'


df['Property Type'] = df['title'].apply(categorize_property)

average_metrics_by_property_type = df.groupby('Property Type')[['price', 'living_space']].mean()
# print(average_metrics_by_property_type)
property_count = df['Property Type'].value_counts()

fig, ax = plt.subplots(figsize=(14,8))
color = 'tab:red'
ax.set_xlabel('Property Type')
ax.set_ylabel('Average price', color=color)
bars = ax.bar(average_metrics_by_property_type.index,average_metrics_by_property_type['price'],
              alpha=0.6,label='Average price', color=color)
ax.tick_params(axis='y', labelcolor=color)

ax.set_xticks(range(len(average_metrics_by_property_type.index)))
ax.set_xticklabels(average_metrics_by_property_type.index, rotation=20, ha='right')

ax1 = ax.twinx()
color = 'tab:blue'
ax1.set_ylabel('Average living space', color=color)
bars2 = ax1.bar(range(len(average_metrics_by_property_type.index)), average_metrics_by_property_type['living_space'],
                color=color, alpha=0.4, width=0.4, label='Average living space')

ax1.tick_params(axis='y', labelcolor=color)
plt.show()


