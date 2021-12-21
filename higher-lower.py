import random
from art import logo, vs
from replit import clear
from game_data import data

def  random_archeva():
    return random.choice(data)

def informacia(anagarishi):
    name = anagarishi['name']
    description = anagarishi["description"]
    country = anagarishi["country"]

    return name, " a ", description, " from ", country

def followers(gamomwerebi):
    follower_count = gamomwerebi["follower_count"]
    return follower_count


def shedareba(a_followers, b_followers,guess):
    if a_followers > b_followers:
        return guess=='a'
    else:
        return guess=='b'

def tamashi():
    tamashi = True
    qula = 0
    while tamashi:
        a_angarishi = random_archeva()
        b_angarishi = random_archeva()
        while a_angarishi == b_angarishi:
            b_angarishi = random_archeva()

        print("Shevadarot A:", informacia(a_angarishi))
        print(vs)
        print("Shevadarot B:", informacia(b_angarishi))
        a_followers = followers(a_angarishi)
        b_followers = followers(b_angarishi)
        print(a_followers,b_followers)
        guess = input("Romels ufro meti gamomweri hyavs 'A' tu 'B':").lower()
        shemowmeba = (shedareba(a_followers,b_followers,guess))
        print(logo)
        clear()
        if shemowmeba:
            qula=qula+1
            print("Tqven martali Brdzandebit Tqven Gaqvt :",qula, "qula")
        else:
            print("Tqven Samwuxarod Damarcxdit, Tavidan Scadet !")
            tamashi=False
tamashi()