import math

def main_menu():
    print("Choose an option:")
    print("1. Kinematic EQ 1")
    print("2. Kinematic EQ 2")
    print("3. Kinematic EQ 3")
    print("4. Force")
    print("5. Coulomb's Law")
    print("6. Ohm's Law")
    print("7. Magnetic Force")
    
    while True:
        try:
            choice = int(input("Enter your choice (1-7): "))
            if 1 <= choice <= 7:
                return choice  # Returning the selected option
            else:
                print("Invalid option. Please enter a number between 1 and 7.")
        except ValueError:
            print("Invalid input. Please enter a numeric value.")

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

def FORCE():
    solve_for = int(input("Solve for:\n1. Force\n2. Mass\n3. Acceleration\n"))
    if solve_for == 1:
        mass = take("Enter the mass of the object in (kg): ")
        acceleration = take("Enter the acceleration on the object in (m/s^2): ")
        force = mass * acceleration
        print(f"The force is: {force}N")
    elif solve_for == 2:
        force = take("Enter the force in N: ")
        acceleration = take("Enter the acceleration in (m/s^2): ")
        mass = force/acceleration
        print(f"The mass is: {mass}kg")
    elif solve_for == 3:
        force = take("Enter the force in N: ")
        mass = take("Enter the mass in (kg): ")
        acceleration = force/mass
        print(f"The acceleration is: {acceleration}m/s^2")
    else:
        print("Invalid option, can only solve for the following 3.")

def COULOMB_LAW():
    COULOMB_CONSTANT = 8.99 * 10**9
    solve_for = int(input("Solve for:\n1. Force between the charges\n2. Magnitude of either charge\n3. Distance of separation\n"))
    if solve_for == 1:
        charge1 = take("Enter the first charge in (C): ")
        charge2 = take("Enter the second charge in (C): ")
        distance = take("Enter the distance of separation in (m): ")
        force = COULOMB_CONSTANT * (charge1 * charge2)/distance**2
        print(f"The force between the charges is: {force}N")
    elif solve_for == 2:
        charge = take("Enter the value of the charge (other charge is taken automatically as a variable) in (C): ")
        distance = take("Enter the distance of separation in (m): ")
        force = take("Enter the force between the charges in (N): ")
        missingCharge = (force * (distance**2))/(COULOMB_CONSTANT * charge)
        print(f"The magnitude of the missing charge is: {missingCharge}C")
    elif solve_for == 3:
        charge1 = take("Enter the first charge in (C): ")
        charge2 = take("Enter the second charge in (C): ")
        force = take("Enter the force between the charges in (N): ")
        distance = math.sqrt((COULOMB_CONSTANT * charge1 * charge2)/force)
        print(f"The distance between the charges is: {distance}m")
    else:
        print("Invalid option, can only solve for the following 3.")

def OHM_LAW():
    solve_for = int(input("Solve for:\n1. Voltage\n2. Current\n3. Resistance\n"))
    if solve_for == 1:
        current = take("Enter the current magnitude in (A): ")
        resistance = take("Enter the resistance magnitude in (ohm): ")
        voltage = current * resistance
        print(f"The voltage is: {voltage}V")
    elif solve_for == 2:
        voltage = take("Enter the voltage in (V): ")
        resistance = take("Enter the resistance in (ohm): ")
        current = voltage/resistance
        print(f"The current is: {current}A")
    elif solve_for == 3:
        voltage = take("Enter the voltage in (V): ")
        current = take("Enter the current magnitude in (A): ")
        resistance = voltage/current
        print(f"The resistance is: {resistance}ohm(s)")
    else:
        print("Invalid option, can only solve for the following 3.")

def MAGNETIC_FORCE():
    solve_for = int(input("Solve for:\n1. Magnetic force\n2. Charge of the moving particle\n3. Velocity of particle\n4. Magnetic field"))
    if solve_for == 1:
        charge = take("Enter the charge of the particle in (C): ")
        velocity = take("Enter the velocity of the particle in (m/s): ")
        magnetic_field = take("Enter the magnetic field's magnitude in (T): ")
        angle = math.radians(take("Enter the angle between velocity and magnetic field vectors in (degrees): "))
        if angle == 0:
            print("The angle between velocity and magnetic field vectors can't be 0, since magnetic field will be 0")
        force = charge * velocity * magnetic_field * math.sin(angle)
        print(f"The magnetic force is: {force}N")
    elif solve_for == 2:
        velocity = take("Enter the velocity of the particle in (m/s): ")
        magnetic_field = take("Enter the magnetic field's magnitude in (T): ")
        angle = math.radians(take("Enter the angle between velocity and magnetic field vectors in (degrees): "))
        if angle == 0:
            print("The angle between velocity and magnetic field vectors can't be 0, since magnetic field will be 0")
        force = take("Enter the magnitude of magnetic force in (N): ")
        charge = force/(velocity * magnetic_field * math.sin(angle))
        print(f"The charge of the particle is: {charge}C")
    elif solve_for == 3:
        magnetic_field = take("Enter the magnetic field's magnitude in (T): ")
        angle = math.radians(take("Enter the angle between velocity and magnetic field vectors in (degrees): "))
        if angle == 0:
            print("The angle between velocity and magnetic field vectors can't be 0, since magnetic field will be 0")
        force = take("Enter the magnitude of magnetic force in (N): ")
        charge = take("Enter the charge of the particle in (C): ")
        velocity = force/(charge * magnetic_field * math.sin(angle))
        print(f"The velocity of the particle is: {velocity}m/s")
    elif solve_for == 4:
        angle = math.radians(take("Enter the angle between velocity and magnetic field vectors in (degrees): "))
        if angle == 0:
            print("The angle between velocity and magnetic field vectors can't be 0, since magnetic field will be 0")
        force = take("Enter the magnitude of magnetic force in (N): ")
        charge = take("Enter the charge of the particle in (C): ")
        velocity = take("Enter the velocity of the particle in (m/s): ")
        magnetic_field = force/(charge * velocity * math.sin(angle))
        print(f"The magnetic field is: {magnetic_field}T")
    else:
        print("Invalid option, can only solve for the following 4.")


def program():
    CHOICE = main_menu()    
    if CHOICE == 1:
        KINEMATIC_EQ1()
    elif CHOICE == 2:
        KINEMATIC_EQ2()
    elif CHOICE == 3:
        KINEMATIC_EQ3()
    elif CHOICE == 4:
        FORCE()
    elif CHOICE == 5:
        COULOMB_LAW()
    elif CHOICE == 6:
        OHM_LAW()
    elif CHOICE == 7:
        MAGNETIC_FORCE()
    else:
        print("Invalid option.")

while True:
    program()
    start_again = input("Do you want to use the calculator again? (y/n) case sensitive: ")
    if start_again != 'y':
        break
