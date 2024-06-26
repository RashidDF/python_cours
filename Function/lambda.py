def greeting(greet):
    return lambda name: f"{greet}, {name}"


morning_greeting = greeting("Good Morning")
print(morning_greeting('Rashid'))

evening_greeting = greeting("Good Evening")
print(evening_greeting('Rashid'))

night_greeting = greeting('Good Night')
print(night_greeting('Rashid'))
