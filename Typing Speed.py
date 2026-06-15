import time

print("Welcome to the Typing Speed Test!")

Sentence ="The five boxing wizards jump quickly."

print("\n Type this Sentence Exactly... ")
print(Sentence)

input("\nPress Enter to start the test...")

start=time.time()

user_input=input("\n Type the sentence here: ")

end=time.time()

time_taken = round(end-start,2)

speed=round(len(Sentence)/time_taken,2)

print("Time Taken :" ,time_taken,"second")
print("Typing Speed :", speed," letters/sec")

if user_input == Sentence:
    print("Congratulations! You typed the sentence correctly.")
else:
    print("Oops! There were some mistakes in your typing. Keep practicing to improve your speed and accuracy.")