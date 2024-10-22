import random

moods = ["Happy", "Sad", "Mad", "Energetic", "Calm"]
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
for i in range(7):
    print(f"On {days[i]}, you were feeling {random.choice(moods)}")