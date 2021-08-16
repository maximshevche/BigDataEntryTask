import pandas as pd

df = pd.read_csv(
    "test-task_dataset_summer_products.csv",
    usecols=["origin_country", "price", "rating_count", "rating_five_count"]
)
group_by_country = df.groupby("origin_country")
avg_price_by_country = group_by_country["price"].mean()
five_percentage = group_by_country["rating_five_count"].sum() / group_by_country["rating_count"].sum() * 100
