import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Simulation parameters
N = 50  # Grid size (NxN)
L = 1.0  # Domain length
dx = L / N  # Grid spacing
dt = 0.0005  # Time step (reduced for stability with uniform flow)
T = 0.5  # Total simulation time (reduced for quicker animation)
nu = 0.01  # Viscosity

# --- User Controls --- #
# Obstacle Type: Choose 'square', 'triangle', 'rectangle', or 'none'
obstacle_type = input("Choose obstacle type")  # Change this to select an obstacle

# Initialize velocity field
u_flow_speed = 1.0  # Initial speed of the river flow
u_velocity = np.zeros((N, N))  # u-component (east-west)
v_velocity = np.ones((N, N)) * u_flow_speed  # v-component (south-north, river flows "upwards")

# Obstacle definition
obstacle_mask = np.zeros((N, N), dtype=bool)

if obstacle_type == 'square':
    # Square obstacle in the middle
    center_x, center_y = N // 2, N // 2
    half_size = N // 10
    obstacle_mask[center_y - half_size: center_y + half_size,
    center_x - half_size: center_x + half_size] = True
elif obstacle_type == 'triangle':
    # Isosceles triangle pointing upwards, in the middle
    center_x, base_y = N // 2, N // 2 - N // 10
    height = N // 5
    tip_y = base_y + height
    half_base_width = N // 10
    for y_coord in range(base_y, tip_y):
        # Calculate current width of the triangle at this y_coord
        # Linear interpolation from half_base_width to 0
        current_half_width = int(half_base_width * (tip_y - y_coord) / height)
        obstacle_mask[y_coord, center_x - current_half_width: center_x + current_half_width + 1] = True
elif obstacle_type == 'rectangle':
    # Narrow rectangle (vertical orientation) in the middle
    center_x, center_y = N // 2, N // 2
    rect_height_half = N // 6
    rect_width_half = N // 20
    obstacle_mask[center_y - rect_height_half: center_y + rect_height_half,
    center_x - rect_width_half: center_x + rect_width_half] = True
# If 'none', obstacle_mask remains all False

# --- 2D Burger's Equation Solver --- #
fig, ax = plt.subplots(figsize=(8, 7))
ims = []  # To store frames for animation

print(f"Starting simulation for {T / dt:.0f} steps...")

for t_step in range(int(T / dt)):
    u = u_velocity
    v = v_velocity

    # Calculate derivatives using central differences for diffusion terms
    u_xx = (np.roll(u, 1, axis=1) - 2 * u + np.roll(u, -1, axis=1)) / dx ** 2  # d^2u/dx^2
    u_yy = (np.roll(u, 1, axis=0) - 2 * u + np.roll(u, -1, axis=0)) / dx ** 2  # d^2u/dy^2
    v_xx = (np.roll(v, 1, axis=1) - 2 * v + np.roll(v, -1, axis=1)) / dx ** 2  # d^2v/dx^2
    v_yy = (np.roll(v, 1, axis=0) - 2 * v + np.roll(v, -1, axis=0)) / dx ** 2  # d^2v/dy^2

    # Calculate advection terms using upwind scheme (first order)
    # For u * du/dx
    u_adv_x = np.where(u > 0, (u - np.roll(u, 1, axis=1)) / dx, (np.roll(u, -1, axis=1) - u) / dx)
    # For v * du/dy
    u_adv_y = np.where(v > 0, (u - np.roll(u, 1, axis=0)) / dx, (np.roll(u, -1, axis=0) - u) / dx)

    # For u * dv/dx
    v_adv_x = np.where(u > 0, (v - np.roll(v, 1, axis=1)) / dx, (np.roll(v, -1, axis=1) - v) / dx)
    # For v * dv/dy
    v_adv_y = np.where(v > 0, (v - np.roll(v, 1, axis=0)) / dx, (np.roll(v, -1, axis=0) - v) / dx)

    # Update velocities using Euler forward step
    u_new = u + dt * (-u * u_adv_x - v * u_adv_y + nu * (u_xx + u_yy))
    v_new = v + dt * (-u * v_adv_x - v * v_adv_y + nu * (v_xx + v_yy))

    # Apply obstacle boundary conditions (no-slip: velocity is zero on/in the obstacle)
    u_new[obstacle_mask] = 0
    v_new[obstacle_mask] = 0

    # Apply periodic boundary conditions (implicitly handled by np.roll for derivatives)
    # For explicit periodic BC on u and v if needed (though roll handles it for derivatives)
    # u_new[0, :] = u_new[-2, :]; u_new[-1, :] = u_new[1, :]; # Example for y-dir, adjust if N is edge or center points
    # u_new[:, 0] = u_new[:, -2]; u_new[:, -1] = u_new[:, 1]; # Example for x-dir
    # v_new[0, :] = v_new[-2, :]; v_new[-1, :] = v_new[1, :];
    # v_new[:, 0] = v_new[:, -2]; v_new[:, -1] = v_new[:, 1];
    # Note: The np.roll already provides periodicity for the difference calculations.
    # For a channel flow, one might want fixed inflow/outflow or wall conditions on sides.
    # Here, we keep it fully periodic for simplicity as per the previous structure.

    u_velocity = u_new
    v_velocity = v_new

    # Add frame for animation (e.g., every few steps to save time/memory)
    if t_step % 10 == 0:
        velocity_magnitude = np.sqrt(u_velocity ** 2 + v_velocity ** 2)
        img = ax.imshow(velocity_magnitude, origin='lower', extent=[0, L, 0, L], animated=True, cmap='viridis', vmin=0,
                        vmax=u_flow_speed * 1.5)
        if t_step == 0:
            ax.imshow(obstacle_mask, origin='lower', extent=[0, L, 0, L], cmap='gray',
                      alpha=0.5)  # Show obstacle static
            plt.colorbar(img, ax=ax, label='Velocity Magnitude (m/s)')
            ax.set_title(f"2D River Flow (Burger's) - Obstacle: {obstacle_type}")
            ax.set_xlabel("X position (m)")
            ax.set_ylabel("Y position (m) - Flow South to North")

        ims.append([img])
        print(f"Step {t_step}/{int(T / dt)} completed.", end='\r')

print("\nSimulation finished. Creating animation...")

# Create animation
ani = animation.ArtistAnimation(fig, ims, interval=50, blit=True, repeat_delay=1000)

# Save or show animation
# To save as GIF (requires imagemagick or pillow):

ani.save('river_flow_animation_triangle.gif', writer='imagemagick', fps=15)
print("Animation saved as river_flow_animation.gif")
plt.show()
print("Program finished.")
