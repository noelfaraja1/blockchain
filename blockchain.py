# Initialized our empty blockchain
blockchain = []

def get_last_blockchain_value():
    """returns the last value of current blockchain"""
    if len(blockchain) < 1:
        return None
    return blockchain[-1]

def add_transaction(transaction_amount, last_transaction=[1]):
    """Append new value current blockchain"""
    if last_transaction == None:
        last_transaction = [1]
    blockchain.append([last_transaction, transaction_amount])

def get_transaction_value():
    """returns s new transaction amount as a float"""
    user_input = float(input("enter your transactions amount: ")) 
    return user_input

def get_user_choice():
    user_input = input("Your choice: ")
    return user_input

def print_blockchain_elements():
    # output the blockchainlist to the console
    for block in blockchain:
        print("outputting")
        print(block)

# get the first transaction input and add the blockchain
tx_amount = get_transaction_value()
add_transaction(tx_amount)

while True:
    print("Please choose")
    print("1: Add a new transaction value")
    print("2: Output the blockchain blocks")
    print("q: Quit")
    user_choice = get_user_choice()
    if user_choice == "1":
        tx_amount = get_transaction_value()
        add_transaction(tx_amount, get_last_blockchain_value())

    elif user_choice == "2":
        print_blockchain_elements()

    elif user_choice == "q":
        break

    else:
        print("Input was invalid, please pick a value from a list")
        print("Choice registered!")

    # output the blockchainlist to the console
    for block in blockchain:
        print("outputting")
        print(block)

print("Done")

