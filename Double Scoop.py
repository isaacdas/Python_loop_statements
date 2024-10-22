import random 

moods = ["Happy", "Sad", "Mad", "Energetic", "Calm"]
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
times = ["morning", "afternoon", "evening"] 

for day in days:
    for time in times:
        print(f"On {day} {time} you were {random.choice(moods)}")