"""
Develop a python program for an online shopping system that processes multiple customer orders simultaneously
using multithreading.
Create three Threads:
1. Order Verification Thread: Verifies customer orders, simulate processing time using sleep()
2. Payment Processing Thread: Processes payments for verified orders, simulate processing time using sleep()
3. Inventory Update Thread: Updates stock after payment confirmation, simulate processing time using sleep()
"""
import threading
import time
# Customer orders
orders = ["Order 1", "Order 2", "Order 3"]
# Shared lists
verified_orders = []
paid_orders = []
# Thread 1: Order Verification
def verify_orders():
    for order in orders:
        print(order, "verification started")
        time.sleep(2)
        verified_orders.append(order)
        print(order, "verified successfully")
# Thread 2: Payment Processing
def process_payment():
    for order in orders:
        while order not in verified_orders:
            time.sleep(0.5)
        print(order, "payment processing started")
        time.sleep(2)
        paid_orders.append(order)
        print(order, "payment successful")
# Thread 3: Inventory Update
def update_inventory():
    for order in orders:
        while order not in paid_orders:
            time.sleep(0.5)
        print(order, "inventory updating")
        time.sleep(2)
        print(order, "inventory updated successfully")

# Creating threads
t1 = threading.Thread(target=verify_orders)
t2 = threading.Thread(target=process_payment)
t3 = threading.Thread(target=update_inventory)
# Starting threads
t1.start()
t2.start()
t3.start()
# Waiting for all threads to finish
t1.join()
t2.join()
t3.join()
print("\nAll orders processed successfully!")