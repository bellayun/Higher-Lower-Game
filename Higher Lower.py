# Higher Lower
# Higher followers or lower followers?

from game_data import data
import random

def format_data(account):
    """format the account data into printable format"""
    account_name = account["name"]
    account_descr = account["description"]
    account_country = account["country"]
    return f"{account_name}, a {account_descr}, from {account_country}"


def check_answer(user_guess, a_followers, b_followers):
    """Take a user's guess and the follower counts and returns if this is correct"""
    if a_followers > b_followers:
        return user_guess == "a"
    else:
        return user_guess == "b"
    

score = 0
game_should_continue = True
account_b = random.choice(data)

# Generate a random aacount from the agme data.
while game_should_continue:
    account_a = account_b
    # account_a = random.choice(data)
    account_b = random.choice(data)
    if account_a == account_b :
        account_b = random.choice(data)

    print(f"Compare A: {format_data(account_a)}.")
    print(f"Against B: {format_data(account_b)}.")

    # Ask user for a guess
    guess = input("Who has higer followers A or B?: ").lower()

    # Check if user is correct
    ## Get follower count of each account
    a_follower_count = account_a["follower_count"]
    b_follower_count = account_b["follower_count"]

    is_correct = check_answer(guess, a_follower_count, b_follower_count)


    # Give user feedback on their guess
    if is_correct:
        score += 1
        print(f"You are right. Current score: {score}")
    else:
        print(f"Sorry, that's wrong. Final score: {score}")
        game_should_continue = False


# Score keeping


# Make the game repeatable


# Making account at position B become the next account at position A