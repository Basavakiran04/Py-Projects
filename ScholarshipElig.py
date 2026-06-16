name = input("Enter your Name:")
rollno = int(input("Enter your Roll no:"))
attendence = int(input("Enter your attendence:"))
CGPA = float(input("Enter your CGPA:"))

if attendence >=90:
    bonus_marks=5

if attendence >=75 and CGPA >= 8.0:
    Eligibility=True
else:
    Eligibility=False

print("===|Report|===")

print(name)
print(rollno)
print(attendence)
print(CGPA)
print(f"{'Eligible' if Eligibility else 'Not Eligible'}")

if bonus_marks ==5:
    print("Honor Scholar")
else:
    print("Not Honor Scholar")