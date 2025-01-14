import math
CHOICE = int(input("Options:\n1. Solve for Kinematic EQ 1\2. Solve for Kinematic EQ 2\n3. Solve for Kinematic EQ 3\n4. Solve for Force\n5. Solve for Inertia\n6. Solve for momentum\n7. Solve for conservation of momentum (valid for third law of motion)\n[SELECT INTEGER ALONGSIDE CHOICE]: "))

def take(prompt):
    while True:
        try:
            value = float(input(prompt))
            return value
        except ValueError:
            print("Invalid input. Please enter a numeric value.")

def KINEMATIC_EQ1():
    solve_for = int(input("Solve for:\n1. Final velocity\n2. Initial velocity\n3. Acceleration\n4. Time\n"))
    if solve_for == 1:
        velocityInit = take("Enter the initial velocity in (m/s): ")
        acceleration = take("Enter the acceleration on the object in (m/s^2): ")
        time = take("Enter the time taken in (s): ")
        velocity = velocityInit + (acceleration * time)
        print(f"The final velocity is: {velocity} m/s")
    elif solve_for == 2:
        velocity = take("Enter the final velocity in (m/s): ")
        acceleration = take("Enter the acceleration on the object in (m/s^2): ")
        time = take("Enter the time taken in (s): ")
        velocityInit = velocity - (acceleration * time)
        print(f"The initial velocity is: {velocityInit} m/s")
    elif solve_for == 3:
        velocity = take("Enter the final velocity in (m/s): ")
        velocityInit = take("Enter the initial velocity in (m/s): ")
        time = take("Enter the time taken in (s): ")
        acceleration = (velocity - velocityInit)/time
        print(f"The acceleration is: {acceleration} m/s^2")
    elif solve_for == 4:
        velocity = take("Enter the final velocity in (m/s): ")
        velocityInit = take("Enter the initial velocity in (m/s): ")
        acceleration = take("Enter the acceleration on the object in (m/s^2): ")
        time = (velocity - velocityInit)/acceleration
        print(f"The time taken is: {time} seconds.")
    else:
        print("Invalid option, can only solve for the following 4.")

def KINEMATIC_EQ2():
    solve_for = int(input("Solve for:\n1. Distance\n2. Initial velocity\n3. Acceleration\n4. Time"))
    if solve_for == 1:
        velocityInit = take("Enter the initial velocity in (m/s): ")
        acceleration = take("Enter the acceleration on the object in (m/s^2): ")
        time = take("Enter the time taken in (s): ")
        distance = (velocityInit * time) + 0.5 * (acceleration * time * time)
        print(f"The distance traveled by the object is: {distance}m.")
    elif solve_for == 2:
        distance = take("Enter the distance traveled by the object in (m): ")
        acceleration = take("Enter the acceleration on the object in (m/s^2): ")
        time = take("Enter the time taken in (s): ")
        velocityInit = (distance - (0.5 * (acceleration * time * time)))/time
        print(f"The initial velocity is: {velocityInit}m/s")
    elif solve_for == 3:
        distance = take("Enter the distance traveled by the object in (m): ")
        velocityInit = take("Enter the initial velocity in (m/s): ")
        time = take("Enter the time taken in (s): ")
        acceleration = 2 *distance - 2*(velocityInit * time)/(time * time)
        print(f"The acceleration on the object is: {acceleration}m/s^2")
    elif solve_for == 4:
        distance = take("Enter the distance traveled by the object in (m): ")
        velocityInit = take("Enter the initial velocity in (m/s): ")
        acceleration = take("Enter the acceleration on the object in (m/s^2): ")
        time = (-1*velocityInit + math.sqrt(velocityInit * velocityInit + (2 * acceleration * distance)))/acceleration
        print(f"The time taken is: {time} seconds")
    else:
        print("Invalid option, can only solve for the following 4.")

def KINEMATIC_EQ3():
    solve_for = int(input("Solve for:\n1. Final velocity\n2. Initial velocity\n3. Acceleration\n4. Distance"))
    if solve_for == 1:
        velocityInit = take("Enter the initial velocity in (m/s): ")
        acceleration = take("Enter the acceleration on the object in (m/s^2): ")
        distance = take("Enter the distance traveled by the object in (m): ")
        velocity = math.sqrt((velocityInit * velocityInit) + 2 * acceleration * distance)
        print(f"The velocity of the object is: {velocity}m/s")
    elif solve_for == 2:
        velocity = take("Enter the final velocity in (m/s): ")
        acceleration = take("Enter the acceleration on the object in (m/s^2): ")
        distance = take("Enter the distance traveled by the object in (m): ")
        velocityInit = math.sqrt((velocity*velocity) - 2 * acceleration * distance)
        print(f"The initial velocity is: {velocityInit}m/s")
    elif solve_for == 3:
        velocity = take("Enter the final velocity in (m/s): ")
        velocityInit = take("Enter the initial velocity in (m/s): ")
        distance = take("Enter the distance traveled by the object in (m): ")
        acceleration = ((velocity * velocity) - (velocityInit * velocityInit))/(2 * distance)
        print(f"The acceleration of the object is: {acceleration}m/s^2")
    elif solve_for == 4:
        velocity = take("Enter the final velocity in (m/s): ")
        velocityInit = take("Enter the initial velocity in (m/s): ")
        acceleration = take("Enter the acceleration on the object in (m/s^2): ")
        distance = ((velocity * velocity) - (velocityInit * velocityInit))/(2 * acceleration)
        print(f"The distance is: {distance}m")
    else:
        print("Invalid option, can only solve for the following 4.")

if CHOICE == 1:
    KINEMATIC_EQ1()
elif CHOICE == 2:
    KINEMATIC_EQ2()
elif CHOICE == 3:
    KINEMATIC_EQ3()
else:
    print("Invalid option.")