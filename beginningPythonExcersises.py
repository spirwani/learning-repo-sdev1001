#temp conversion program

celcuis = float(input("Give me Celcius temp: "))
farienheit = (celcuis * 9/5) + 32
print(f"{celcuis} celcius converted to farienheit is: {farienheit}")

# Rectangle calculator program

width =float(input("Enter a width of the rectangle: "))
height =float(input("Enter a height of the rectangle: "))
area = width * height
perimiter = 2*(width * height)
print(f"Area: {area:.3f}")