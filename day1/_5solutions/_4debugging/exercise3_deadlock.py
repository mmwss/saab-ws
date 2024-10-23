import threading

class BankAccount:
    def __init__(self, balance=0):
        self.balance = balance
        self.lock = threading.Lock()

def transfer(from_account, to_account, amount):
    # Acquire locks in a consistent order
    first_lock, second_lock = (from_account.lock, to_account.lock) if id(from_account) < id(to_account) else (to_account.lock, from_account.lock)
    with first_lock:
        # Simulate some processing delay
        import time
        time.sleep(0.1)
        with second_lock:
            from_account.balance -= amount
            to_account.balance += amount

# Create accounts
account_a = BankAccount(1000)
account_b = BankAccount(1000)

# Create threads to perform transfers
t1 = threading.Thread(target=transfer, args=(account_a, account_b, 100))
t2 = threading.Thread(target=transfer, args=(account_b, account_a, 200))

# Start threads
t1.start()
t2.start()

# Wait for threads to finish
t1.join()
t2.join()

print(f"Account A balance: {account_a.balance}")
print(f"Account B balance: {account_b.balance}")
