import pandas as pd
import random
from datetime import datetime, timedelta

# Function to generate users
def generate_users(n):
    users = []
    for user_id in range(1, n + 1):
        name = f"User_{user_id}"  # Generate a simple name like User_1, User_2, etc.
        users.append({
            'user_id': user_id,
            'name': name
        })
    return users

# Function to generate transactions
def generate_transactions(users, num_transactions):
    transactions = []
    now = datetime.now()
    for transaction_id in range(1, num_transactions + 1):
        user_id = random.choice(users)['user_id']
        amount = round(random.uniform(1000, 10000), 2)  # Random amount between 10 and 1000
        transaction_date = now - timedelta(days=random.randint(0, 365))  # Random date within the last year
        transactions.append({
            'transaction_id': transaction_id,
            'user_id': user_id,
            'amount': amount,
            'transaction_date': transaction_date
        })
    return transactions

# Main script
if __name__ == "__main__":

    # Generate user and transaction data
    users = generate_users(50)  # Ensure this is called before referencing `users`
    transactions = generate_transactions(users, 500)  # Ensure `users` exists before this

# Convert to Pandas DataFrame for tabular display
users_df = pd.DataFrame(users)
transactions_df = pd.DataFrame(transactions)

# Display the users and transactions in a tabular format
print("Users Table:")
print(users_df)

print("\nTransactions Table:")
print(transactions_df)


# Function to calculate total transaction amount for each user
def calculate_total_spending(transactions):
    spending = {}
    for transaction in transactions:
        user_id = transaction['user_id']
        amount = transaction['amount']
        if user_id in spending:
            spending[user_id] += amount # add amount  to current total
        else:
            spending[user_id] = amount # add current amount
    return spending

# Function to identify the top 5 users with the highest spending
def top_5_users(spending):
    top_5 = sorted(spending.items(), key=lambda x: x[1], reverse=True)  # returns a view object of all the key-value pairs as tuples
    return top_5[:5] #ensures only the top 5 results are returned.

# Function to calculate total number of transactions in the last 3 months
def transactions_in_last_3_months(transactions):
    three_months_ago = datetime.now() - timedelta(days=90)
    recent_transactions = [t for t in transactions if t['transaction_date'] >= three_months_ago]
    return len(recent_transactions)

# Generate users and transactions
users = generate_users(50)
transactions = generate_transactions(users, 500)

# Calculate total spending for each user
spending = calculate_total_spending(transactions)

# Identify top 5 users with highest spending
top_5_users = top_5_users(spending)

# Calculate total number of transactions in the last 3 months
three_months_transactions_count = transactions_in_last_3_months(transactions)

# Convert to pandas DataFrame for tabular format printing
user_spending_df = pd.DataFrame(spending.items(), columns=['User ID', 'Total Spending'])
top_5_users_df = pd.DataFrame(top_5_users, columns=['User ID', 'Total Spending'])

# Print results to console in a tabular format
print("\nTotal Spending by Each User:")
print(user_spending_df)

print("\nTop 5 Users with Highest Spending:")
print(top_5_users_df)

print("\nTotal Number of Transactions in the Last 3 Months:", three_months_transactions_count)
