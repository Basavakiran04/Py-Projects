speed = int(input("Enter speed in km/h: "))
distance = int(input("Enter distance in km: "))
time = distance / speed

hours = int(time);
minutes = int((time - hours) * 60);
seconds = int((((time - hours) * 60) - minutes) * 60);

print(f"You will reach your destination in {hours} hours, {minutes} minutes, and {seconds} seconds.\nIf you maintain a speed of {speed} km/h.\nHave a safe trip!")