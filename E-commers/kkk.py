import hashlib
import json
import random
import string
from Products import *  # Assuming Products module contains product data

import pyaudio
import speech_recognition as sr
import pyttsx3
import webbrowser

FRAMES_PER_BUFFER = 3200
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 16000

# Initialize PyAudio
p = pyaudio.PyAudio()

# Open PyAudio stream for recording
stream = p.open(format=FORMAT,
                channels=CHANNELS,
                rate=RATE,
                input=True,
                frames_per_buffer=FRAMES_PER_BUFFER)

engine = pyttsx3.init()

# Set properties for female voice
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

users_file_path = r'C:\Users\ABC\Desktop\Mini Projects\SpeakSmart\E-commers\Data\users.json'
logged_in_user = None
order_history = []

# Generate 20 unique gift card codes
gift_cards = ["".join(random.choices(string.ascii_uppercase + string.digits, k=10)) for _ in range(20)]

try:
    with open(users_file_path, 'r') as file:
        try:
            users = json.load(file)
        except json.decoder.JSONDecodeError as e:
            print(f"Error loading JSON data from {users_file_path}: {e}")
            users = {}
except FileNotFoundError:
    print(f"File not found: {users_file_path}")
    users = {}

def save_users():
    with open(users_file_path, 'w') as file:
        json.dump(users, file)

def register():
    username = input("Enter username: ")
    if username in users:
        print("Username already exists!")
        return
    password = input("Enter password: ")
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    users[username] = {
        'password': hashed_password,
        'login_count': 0,
        'gift_card': None
    }
    save_users()
    print("Registration successful!")

def login():
    global logged_in_user

    engine.say("Enter the username")
    engine.runAndWait()
    username = input("Enter username: ")

    engine.say("Enter Password")
    engine.runAndWait()
    password = input("Enter password: ")

    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    if username in users and users[username]['password'] == hashed_password:
        logged_in_user = username
        print("You have logged in successfully!")
        engine.say("You have logged in successfully!")
        engine.runAndWait()
        users[username]['login_count'] += 1
        if users[username]['login_count'] == 1:
            users[username]['gift_card'] = gift_cards.pop()
            print(f"Congratulations! You have received a gift card: {users[username]['gift_card']}")
        save_users()
        return True
    else:
        print("Invalid username or password.")
        engine.say("Invalid username or password.")
        engine.runAndWait()
        return False

def display_products():
    print("The Available categories:")
    engine.say("The Available categories are ")
    engine.runAndWait()
    if logged_in_user:
        categories = {
            1: food_products,
            2: technology_products,
            3: personal_care,
            4: clothing,
            5: furniture,
            6: accessories,
            7: footwear
        }

        for category_num, category_name in {
            1: 'food products',
            2: 'technology products',
            3: 'personal care',
            4: 'clothing',
            5: 'furniture',
            6: 'accessories',
            7: 'footwear'
        }.items():
            print(f"{category_num}. {category_name}")

        choice = int(input("Enter the category number: "))
        if choice in categories:
            category = categories[choice]
            print(f"\nAvailable products in {list(categories.keys())[choice-1]}:")
            for idx, product in enumerate(category):
                print(f"{idx+1}. {product['name']} - ${product['price']} - Stock: {product['stock']}")
            return category
        else:
            print("Invalid category number!")
    else:
        print("Please login to view products.")
        engine.say("Please login to view products")
        engine.runAndWait()

def place_order():
    global logged_in_user
    if logged_in_user:
        products = display_products()
        choice = int(input("Enter the number of the product you want to purchase: "))
        quantity = int(input("Enter the quantity you want to purchase: "))

        if choice >= 1 and choice <= len(products):
            product = products[choice - 1]
            if product['stock'] >= quantity:
                product['stock'] -= quantity
                total_amount = product['price'] * quantity
                order_history.append((product['name'], product['price'], quantity))
                print("Order placed successfully!")
                print(f"Total amount: ${total_amount}")
            else:
                print("Insufficient stock!")
        else:
            print("Invalid choice!")
    else:
        print("Please login to place an order.")
        engine.say("Please login to place an order.")
        engine.runAndWait()

def display_bill():
    global logged_in_user
    print("Your Bill:")
    total_price = 0
    print("{:<20} {:<10} {:<10} {:<10}".format("Item", "Price", "Quantity", "Total Price"))
    print("=" * 52)  
    for item in order_history:
        name, price, quantity = item
        total_item_price = price * quantity
        total_price += total_item_price
        print("{:<20} ${:<9} {:<10} ${:<10}".format(name, price, quantity, total_item_price))
        
    print("=" * 52)
    print("{:<40} ${:<10}".format("Total Price:", total_price))
    
    engine.say("You have ordered: ")
    for item in order_history:
        name, price, quantity = item
        engine.say(f"{name} with Quantity of {quantity} Each price {price}")
        engine.runAndWait()

    if users[logged_in_user]['login_count'] == 1 and users[logged_in_user]['gift_card']:
        apply_gift_card = input("Do you want to apply your gift card for a 10% discount? (yes/no): ").strip().lower()
        if apply_gift_card == 'yes':
            discount = total_price * 0.1
            total_price -= discount
            print(f"Applied 10% discount with gift card {users[logged_in_user]['gift_card']}: -${discount:.2f}")
            print("{:<40} ${:<10}".format("Discounted Total Price:", total_price))

    engine.say(f"The total price is {total_price}")
    engine.say('Thank you. Visit again to Loki Mart!') 
    engine.runAndWait()

while True:
    print("\nWelcome to E-commerce System")         
    print("1. Register")
    print("2. Login")
    print("3. Display Products")
    print("4. Place Order")
    print("5. Display Bill and Exit")
    
    try:
        choice = int(input("Enter your choice: "))  
    except ValueError:
        print("Invalid input. Please enter a number.")
        continue
    
    if choice == 1:
        register()
    elif choice == 2:
        login()
    elif choice == 3:
        display_products()
    elif choice == 4:
        place_order()
    elif choice == 5:
        display_bill()
        print("Thank you. Visit again!")
        break
    else:
        print("Invalid choice. Please try again.")
