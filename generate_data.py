import pandas as pd
import random

ages = ['Young', 'Middle', 'Old']
budgets = ['Low', 'Medium', 'High']
genders = ['Male', 'Female']
interests = ['Electronics', 'Fashion', 'Sports', 'Food']

products = {
    ('Young', 'Low', 'Female', 'Fashion'): ['Accessories', 'Scarves', 'Casual Shirt'],
    ('Young', 'Medium', 'Female', 'Fashion'): ['Handbag', 'Sneakers', 'Accessories'],
    ('Young', 'High', 'Female', 'Fashion'): ['Designer Dress', 'Handbag', 'Jewelry'],
    ('Young', 'Low', 'Male', 'Fashion'): ['Casual Shirt', 'Sneakers', 'Scarves'],
    ('Young', 'Medium', 'Male', 'Fashion'): ['Sneakers', 'Casual Shirt', 'Watches'],
    ('Young', 'High', 'Male', 'Fashion'): ['Watches', 'Suit', 'Sneakers'],
    ('Middle', 'Low', 'Female', 'Fashion'): ['Scarves', 'Clothing', 'Accessories'],
    ('Middle', 'Medium', 'Female', 'Fashion'): ['Clothing', 'Scarves', 'Handbag'],
    ('Middle', 'High', 'Female', 'Fashion'): ['Jewelry', 'Designer Dress', 'Handbag'],
    ('Middle', 'Low', 'Male', 'Fashion'): ['Clothing', 'Casual Shirt', 'Scarves'],
    ('Middle', 'Medium', 'Male', 'Fashion'): ['Formal Shoes', 'Clothing', 'Watches'],
    ('Middle', 'High', 'Male', 'Fashion'): ['Suit', 'Watches', 'Formal Shoes'],
    ('Old', 'Low', 'Female', 'Fashion'): ['Clothing', 'Scarves', 'Accessories'],
    ('Old', 'Medium', 'Female', 'Fashion'): ['Scarves', 'Clothing', 'Jewelry'],
    ('Old', 'High', 'Female', 'Fashion'): ['Jewelry', 'Scarves', 'Clothing'],
    ('Old', 'Low', 'Male', 'Fashion'): ['Casual Shirt', 'Clothing', 'Scarves'],
    ('Old', 'Medium', 'Male', 'Fashion'): ['Watches', 'Formal Shoes', 'Clothing'],
    ('Old', 'High', 'Male', 'Fashion'): ['Suit', 'Watches', 'Formal Shoes'],
    ('Young', 'Low', 'Female', 'Electronics'): ['Earbuds', 'Smartphone', 'Tablet'],
    ('Young', 'Medium', 'Female', 'Electronics'): ['Smartphone', 'Earbuds', 'Tablet'],
    ('Young', 'High', 'Female', 'Electronics'): ['Laptop', 'Smartphone', 'Tablet'],
    ('Young', 'Low', 'Male', 'Electronics'): ['Earbuds', 'Smartphone', 'Tablet'],
    ('Young', 'Medium', 'Male', 'Electronics'): ['Smartphone', 'Earbuds', 'Laptop'],
    ('Young', 'High', 'Male', 'Electronics'): ['Laptop', 'Smartphone', 'Earbuds'],
    ('Middle', 'Low', 'Female', 'Electronics'): ['Earbuds', 'Tablet', 'Smartphone'],
    ('Middle', 'Medium', 'Female', 'Electronics'): ['Tablet', 'Smartphone', 'Earbuds'],
    ('Middle', 'High', 'Female', 'Electronics'): ['Laptop', 'Tablet', 'Smartphone'],
    ('Middle', 'Low', 'Male', 'Electronics'): ['Earbuds', 'Smartphone', 'Tablet'],
    ('Middle', 'Medium', 'Male', 'Electronics'): ['Smartphone', 'Laptop', 'Tablet'],
    ('Middle', 'High', 'Male', 'Electronics'): ['Laptop', 'Smartphone', 'Tablet'],
    ('Old', 'Low', 'Female', 'Electronics'): ['Earbuds', 'Tablet', 'Smartphone'],
    ('Old', 'Medium', 'Female', 'Electronics'): ['Tablet', 'Earbuds', 'Smartphone'],
    ('Old', 'High', 'Female', 'Electronics'): ['Tablet', 'Laptop', 'Earbuds'],
    ('Old', 'Low', 'Male', 'Electronics'): ['Earbuds', 'Tablet', 'Smartphone'],
    ('Old', 'Medium', 'Male', 'Electronics'): ['Tablet', 'Smartphone', 'Earbuds'],
    ('Old', 'High', 'Male', 'Electronics'): ['Laptop', 'Tablet', 'Smartphone'],
    ('Young', 'Low', 'Female', 'Sports'): ['Yoga Mat', 'Skipping Rope', 'Sports Shoes'],
    ('Young', 'Medium', 'Female', 'Sports'): ['Sports Shoes', 'Yoga Mat', 'Skipping Rope'],
    ('Young', 'High', 'Female', 'Sports'): ['Cycling Bike', 'Sports Shoes', 'Yoga Mat'],
    ('Young', 'Low', 'Male', 'Sports'): ['Skipping Rope', 'Sports Shoes', 'Yoga Mat'],
    ('Young', 'Medium', 'Male', 'Sports'): ['Sports Shoes', 'Cricket Kit', 'Skipping Rope'],
    ('Young', 'High', 'Male', 'Sports'): ['Gym Equipment', 'Cricket Kit', 'Sports Shoes'],
    ('Middle', 'Low', 'Female', 'Sports'): ['Yoga Mat', 'Skipping Rope', 'Sports Shoes'],
    ('Middle', 'Medium', 'Female', 'Sports'): ['Sports Shoes', 'Yoga Mat', 'Treadmill'],
    ('Middle', 'High', 'Female', 'Sports'): ['Treadmill', 'Cycling Bike', 'Sports Shoes'],
    ('Middle', 'Low', 'Male', 'Sports'): ['Skipping Rope', 'Cricket Kit', 'Sports Shoes'],
    ('Middle', 'Medium', 'Male', 'Sports'): ['Cricket Kit', 'Sports Shoes', 'Gym Equipment'],
    ('Middle', 'High', 'Male', 'Sports'): ['Gym Equipment', 'Treadmill', 'Cricket Kit'],
    ('Old', 'Low', 'Female', 'Sports'): ['Yoga Mat', 'Walking Shoes', 'Skipping Rope'],
    ('Old', 'Medium', 'Female', 'Sports'): ['Walking Shoes', 'Yoga Mat', 'Treadmill'],
    ('Old', 'High', 'Female', 'Sports'): ['Treadmill', 'Walking Shoes', 'Yoga Mat'],
    ('Old', 'Low', 'Male', 'Sports'): ['Skipping Rope', 'Walking Shoes', 'Yoga Mat'],
    ('Old', 'Medium', 'Male', 'Sports'): ['Walking Shoes', 'Cricket Kit', 'Skipping Rope'],
    ('Old', 'High', 'Male', 'Sports'): ['Treadmill', 'Walking Shoes', 'Cricket Kit'],
    ('Young', 'Low', 'Female', 'Food'): ['Snacks', 'Groceries', 'Restaurant Voucher'],
    ('Young', 'Medium', 'Female', 'Food'): ['Restaurant Voucher', 'Snacks', 'Food Subscription'],
    ('Young', 'High', 'Female', 'Food'): ['Food Subscription', 'Restaurant Voucher', 'Snacks'],
    ('Young', 'Low', 'Male', 'Food'): ['Snacks', 'Groceries', 'Restaurant Voucher'],
    ('Young', 'Medium', 'Male', 'Food'): ['Restaurant Voucher', 'Snacks', 'Food Subscription'],
    ('Young', 'High', 'Male', 'Food'): ['Food Subscription', 'Restaurant Voucher', 'Snacks'],
    ('Middle', 'Low', 'Female', 'Food'): ['Groceries', 'Cooking Set', 'Snacks'],
    ('Middle', 'Medium', 'Female', 'Food'): ['Cooking Set', 'Groceries', 'Food Subscription'],
    ('Middle', 'High', 'Female', 'Food'): ['Food Subscription', 'Cooking Set', 'Restaurant Voucher'],
    ('Middle', 'Low', 'Male', 'Food'): ['Groceries', 'Snacks', 'Cooking Set'],
    ('Middle', 'Medium', 'Male', 'Food'): ['Restaurant Voucher', 'Groceries', 'Cooking Set'],
    ('Middle', 'High', 'Male', 'Food'): ['Food Subscription', 'Restaurant Voucher', 'Cooking Set'],
    ('Old', 'Low', 'Female', 'Food'): ['Groceries', 'Cooking Set', 'Snacks'],
    ('Old', 'Medium', 'Female', 'Food'): ['Cooking Set', 'Groceries', 'Food Subscription'],
    ('Old', 'High', 'Female', 'Food'): ['Food Subscription', 'Cooking Set', 'Groceries'],
    ('Old', 'Low', 'Male', 'Food'): ['Groceries', 'Snacks', 'Cooking Set'],
    ('Old', 'Medium', 'Male', 'Food'): ['Cooking Set', 'Groceries', 'Restaurant Voucher'],
    ('Old', 'High', 'Male', 'Food'): ['Food Subscription', 'Cooking Set', 'Restaurant Voucher'],
}

rows = []
for key, prods in products.items():
    age, budget, gender, interest = key
    for _ in range(10):
        product = random.choices(prods, weights=[60, 30, 10])[0]
        rows.append([age, budget, gender, interest, product])

df = pd.DataFrame(rows, columns=['Age', 'Budget', 'Gender', 'Interest', 'Product'])
df = df.sample(frac=1).reset_index(drop=True)
df.to_csv('products.csv', index=False)
print(f"✅ Dataset generated: {len(df)} rows!")
print(f"Products: {df['Product'].unique()}")