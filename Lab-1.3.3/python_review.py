name = "Asko"
age = 20
height = 1.75
is_student = True

print(name, type(name))
print(age, type(age))
print(height, type(height))
print(is_student, type(is_student))

devices = ["Kali Linux", "Ubuntu", "Windows"]
devices.append("Cisco DEVASC")
print(devices)

student = {
    "name": "Asko",
    "course": "Information Security",
    "year": 3
}
print(student)

attempts = 7

if attempts >= 5:
    print("Suspicious activity")
else:
    print("Normal activity")

for device in devices:
    print(device)

counter = 1
while counter <= 5:
    print(counter)
    counter += 1

def calculate_sum(a, b):
    return a + b

def check_login(attempts):
    if attempts >= 5:
        return "Suspicious"
    return "Normal"

print(calculate_sum(10, 20))
print(check_login(7))
print(check_login(2))

with open("lab.txt", "w") as file:
    file.write("DEVASC Python Programming Review")

with open("lab.txt", "r") as file:
    print(file.read())
