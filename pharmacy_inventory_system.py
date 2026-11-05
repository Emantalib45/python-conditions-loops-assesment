
# Task 2: Smart Pharmacy Inventory & Sales Management System

print("======================================")
print("   SMART PHARMACY MANAGEMENT SYSTEM")
print("======================================")

# Taking number of medicines
total_medicines = int(input("How many medicines do you want to process? "))

# Initializing variables
total_revenue = 0
restock_count = 0

# Using for loop
for i in range(1, total_medicines + 1):

    print("\nMedicine Number:", i)

    # Taking medicine details
    medicine_name = input("Enter Medicine Name: ")
    stock = int(input("Enter Available Stock: "))
    price = float(input("Enter Price Per Unit: Rs. "))
    quantity_sold = int(input("Enter Quantity Sold: "))

    # Checking input validation
    if stock < 0 or price < 0 or quantity_sold < 0:
        print("Invalid Input! Values cannot be negative.")

    else:

        # Checking stock availability
        if quantity_sold <= stock:

            sales_amount = quantity_sold * price
            remaining_stock = stock - quantity_sold

            # Updating total revenue
            total_revenue = total_revenue + sales_amount

            print("\nMedicine Name:", medicine_name)
            print("Total Sales: Rs.", sales_amount)
            print("Remaining Stock:", remaining_stock)

            # Checking low stock
            if remaining_stock < 10:
                print("Warning: Low Stock! Restocking Required.")
                restock_count = restock_count + 1

            else:
                print("Stock Status: Sufficient")

        else:
            print("Sale Failed! Not Enough Stock Available.")
            restock_count = restock_count + 1

# Displaying final report
print("\n======================================")
print("       FINAL PHARMACY REPORT")
print("======================================")

print("Total Medicines Processed:", total_medicines)
print("Total Pharmacy Revenue: Rs.", total_revenue)
print("Medicines Requiring Restocking:", restock_count)

print("======================================")
print("       DAILY SALES COMPLETED")
print("======================================")
