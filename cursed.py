#print ("rust and bob3 = love")

import math


def simulate_ball_throw(v0, angle_degrees, time_step=0.1):
    """
    Simulates the trajectory of a thrown ball using kinematics formulas.
    v0: initial velocity in m/s
    angle_degrees: launch angle in degrees
    time_step: time interval between calculated points in seconds
    Returns a list of (x, y) coordinates representing the trajectory.
    """
    g = 9.81  # Acceleration due to gravity (m/s^2)

    # Convert angle from degrees to radians for math functions
    angle_rad = math.radians(angle_degrees)

    # Calculate total time of flight
    total_time = (2 * v0 * math.sin(angle_rad)) / g

    trajectory = []
    t = 0.0

    # Calculate coordinates for each time step until the ball hits the ground
    while t <= total_time:
        x = v0 * math.cos(angle_rad) * t
        y = v0 * math.sin(angle_rad) * t - (0.5 * g * t ** 2)

        # Prevent negative height due to floating point imprecision
        if y < 0:
            y = 0.0

        trajectory.append((round(x, 2), round(y, 2)))
        t += time_step

    # Ensure the exact landing point is included
    final_x = v0 * math.cos(angle_rad) * total_time
    trajectory.append((round(final_x, 2), 0.0))

    return trajectory


# --- Example usage ---
initial_velocity = 20  # m/s
launch_angle = 45  # degrees

# Run the simulation with a time step of 0.5 seconds
trajectory_points = simulate_ball_throw(initial_velocity, launch_angle, time_step=0.5)

print("Trajectory points (X, Y):")
for point in trajectory_points:
    print(f"Distance: {point[0]:.2f} m | Height: {point[1]:.2f} m")