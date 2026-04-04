import csv
import datetime

def read_dictionary(filename, key_column_index):
    
    products_dict = {}
    try:
        with open(filename, 'r', newline='') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                key = row[key_column_index]
                products_dict[key] = row
        return products_dict
    except FileNotFoundError as e:
        print("Error: missing file")
        print(e)
        return {}
    except PermissionError as e:
        print("Error: permission denied")
        print(e)
        return {}

def main():
    store_name = "Inkom Emporium"
    TAX_RATE = 0.06

    try:
       
        products_dict = read_dictionary("products.csv", 0)
        if not products_dict:
            return  

        # Abrir pedidos
        with open("request.csv", 'r', newline='') as request_file:
            reader = csv.reader(request_file)
            next(reader) 

            subtotal = 0
            total_items = 0
            order_lines = []

            for row in reader:
                try:
                    prod_num = row[0]
                    quantity = int(row[1])
                    product = products_dict[prod_num]
                    product_name = product[1]
                    price = float(product[2])

                    # BOGO (buy one, get one half off) para item D083
                    line_total = quantity * price
                    bogo_text = ""
                    if prod_num == "D083" and quantity > 1:
                        full_price_count = quantity // 2 + quantity % 2
                        half_price_count = quantity // 2
                        line_total = full_price_count * price + half_price_count * price * 0.5
                        bogo_text = " (BOGO applied)"

                    subtotal += line_total
                    total_items += quantity

                    order_lines.append((product_name, quantity, price, line_total, bogo_text))
                except KeyError:
                    print("Error: unknown product ID in the request.csv file")
                    print(f"'{prod_num}'")
                except ValueError:
                    print("Error: invalid quantity for product", prod_num)

        tax = subtotal * TAX_RATE
        total = subtotal + tax

        
        print(f"\n{store_name:^50}")  # Nome da loja centralizado
        print("-"*50)
        print(f"{'Item':<25}{'Qty':>5}{'Price':>10}{'Total':>10}")
        print("-"*50)
        for item_name, qty, price, line_total, bogo_text in order_lines:
            print(f"{item_name:<25}{qty:>5}{price:>10.2f}{line_total:>10.2f}{bogo_text}")
        print("-"*50)
        print(f"{'Number of Items:':<25}{total_items:>25}")
        print(f"{'Subtotal:':<25}{subtotal:>25.2f}")
        print(f"{'Sales Tax:':<25}{tax:>25.2f}")
        print(f"{'Total:':<25}{total:>25.2f}")
        print("-"*50)
        print(f"Thank you for shopping at the {store_name}.")

        
        now = datetime.datetime.now()
        print(now.strftime("%a %b %d %H:%M:%S %Y"))

        
        today = datetime.date.today()
        new_year = datetime.date(today.year + 1, 1, 1)
        days_until_ny = (new_year - today).days
        print(f"Days until New Year's Sale: {days_until_ny}")

        
        return_date = now + datetime.timedelta(days=30)
        return_date = return_date.replace(hour=21, minute=0, second=0, microsecond=0)
        print("Return by:", return_date.strftime("%a %b %d %H:%M:%S %Y"))

        
        if order_lines:
            first_item = order_lines[0][0]
            print(f"Coupon: Get 10% off your next {first_item} purchase!")

    except FileNotFoundError as e:
        print("Error: missing file")
        print(e)
    except PermissionError as e:
        print("Error: permission denied")
        print(e)

if __name__ == "__main__":
    main()