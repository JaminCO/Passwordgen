from django.shortcuts import render, redirect
from .models import Passcode
import time
import random


UPPERCASE = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

lowercase = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']

special_char = [".", ",", ";", ":", "_", "'", "#", "@", "!", "-", "$", "?", "[", "]", "(", ")", "{", "}", "/", "+", "|", "<", ">", "^"]


# Create your views here.

def home_view(request):

    password_one = random.choice(UPPERCASE) + random.choice(lowercase) + random.choice(numbers) + random.choice(special_char) + random.choice(UPPERCASE) + random.choice(lowercase) + random.choice(numbers) + random.choice(special_char)

    password_two = random.choice(UPPERCASE) + random.choice(UPPERCASE) + random.choice(numbers) + random.choice(special_char) + random.choice(lowercase) + random.choice(UPPERCASE) + random.choice(special_char) + random.choice(numbers) + random.choice(numbers) + random.choice(special_char) + random.choice(lowercase) + random.choice(lowercase)

    password_three = random.choice(lowercase) + random.choice(UPPERCASE) + random.choice(special_char) + random.choice(numbers) + random.choice(special_char) + random.choice(numbers) + random.choice(lowercase) + random.choice(UPPERCASE)  + random.choice(UPPERCASE) + random.choice(special_char) + random.choice(numbers) + random.choice(lowercase) + random.choice(UPPERCASE) + random.choice(lowercase) + random.choice(numbers) + random.choice(special_char)

    context = {
        "password":password_one,
        "password2":password_two,
        "password3":password_three,
	}

    return render(request, 'main/home.html', context)
    