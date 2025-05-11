import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Simulation parameters
N = 50  # Grid size (NxN)
L = 1.0  # Domain length
dx = L / N  # Grid spacing
dt = 0.0005  # Time step
T = 1.0  # Total simulation time (increased to see more oscillations)
nu = 0.01  # Viscosity

# --- User Controls --- #
# Obstacle Type: Choose 'square', 'triangle', 'rectangle', or 'none'
obstacle_type = 'square'  # Change this to select an obstacle

# Initialize velocity field
u_velocity = np.zeros((N, N)) # u-component (east-west)
# Initial v_velocity will be set by the inflow condition mostly, but start with a base
v_velocity = np.ones((N, N)) * 1.1 # v-component (south-north, river flows "upwards")

# Obstacle definition
obstacle_mask = np.zeros((N, N), dtype=bool)

if obstacle_type == 'square':
    center_x, center_y = N // 2, N // 2
    half_size = N // 10
    obstacle_mask[center_y - half_size : center_y + half_size, 
                  center_x - half_size : center_x + half_size] = True
elif obstacle_type == 'triangle':
    center_x, base_y = N // 2, N // 2 - N // 10
    height = N // 5
    tip_y = base_y + height
    half_base_width = N // 10
    for y_coord in range(base_y, tip_y):
        current_half_width = int(half_base_width * (tip_y - y_coord) / height)
        if current_half_width > 0:
            obstacle_mask[y_coord, center_x - current_half_width : center_x + current_half_width + 1] = True
elif obstacle_type == 'rectangle':
    center_x, center_y = N // 2, N // 2
    rect_height_half = N // 6
    rect_width_half = N // 20
    obstacle_mask[center_y - rect_height_half : center_y + rect_height_half, 
                  center_x - rect_width_half : center_x + rect_width_half] = True

# --- 2D Burger's Equation Solver --- #
fig, ax = plt.subplots(figsize=(8, 7))
ims = []

# For quiver plot normalization and arrow density
X, Y = np.meshgrid(np.linspace(0, L, N), np.linspace(0, L, N))
skip = (slice(None, None, 3), slice(None, None, 3)) # Plot one arrow every 3 grid points

print(f"Starting simulation for {T/dt:.0f} steps...")

# Oscillation parameters for inflow velocity V at south boundary (y=0)
amplitude = 0.2  # (1.3 - 0.9) / 2
mean_velocity = 1.1  # (1.3 + 0.9) / 2
# Omega for roughly 2-3 cycles in T. Let's say 2.5 cycles in T=1.0s => freq = 2.5 Hz
frequency = 2.5 
omega = 2 * np.pi * frequency

for t_step in range(int(T / dt)):
    u = u_velocity
    v = v_velocity

    # Calculate derivatives (central for diffusion, upwind for advection)
    u_xx = (np.roll(u, 1, axis=1) - 2 * u + np.roll(u, -1, axis=1)) / dx**2
    u_yy = (np.roll(u, 1, axis=0) - 2 * u + np.roll(u, -1, axis=0)) / dx**2
    v_xx = (np.roll(v, 1, axis=1) - 2 * v + np.roll(v, -1, axis=1)) / dx**2
    v_yy = (np.roll(v, 1, axis=0) - 2 * v + np.roll(v, -1, axis=0)) / dx**2

    u_adv_x = np.where(u > 0, (u - np.roll(u, 1, axis=1)) / dx, (np.roll(u, -1, axis=1) - u) / dx)
    u_adv_y = np.where(v > 0, (u - np.roll(u, 1, axis=0)) / dx, (np.roll(u, -1, axis=0) - u) / dx)
    v_adv_x = np.where(u > 0, (v - np.roll(v, 1, axis=1)) / dx, (np.roll(v, -1, axis=1) - v) / dx)
    v_adv_y = np.where(v > 0, (v - np.roll(v, 1, axis=0)) / dx, (np.roll(v, -1, axis=0) - v) / dx)

    u_new = u + dt * (-u * u_adv_x - v * u_adv_y + nu * (u_xx + u_yy))
    v_new = v + dt * (-u * v_adv_x - v * v_adv_y + nu * (v_xx + v_yy))

    # --- Boundary Conditions --- # 
    # Oscillating inflow at South boundary (y=0, first row)
    current_time = t_step * dt
    inflow_v_value = amplitude * np.sin(omega * current_time) + mean_velocity
    v_new[0, :] = inflow_v_value
    u_new[0, :] = 0  # No horizontal flow at the inflow boundary

    # Outflow at North boundary (y=L, last row) - simple Neumann (zero gradient)
    v_new[-1, :] = v_new[-2, :]
    u_new[-1, :] = u_new[-2, :]

    # Walls at East/West boundaries (x=0, x=L) - No-slip or Free-slip
    # Using No-slip for u, and zero gradient for v (less restrictive)
    u_new[:, 0] = 0 # No-slip for u at x=0 (west)
    u_new[:, -1] = 0 # No-slip for u at x=L (east)
    v_new[:, 0] = v_new[:, 1] # Zero gradient for v at x=0
    v_new[:, -1] = v_new[:, -2] # Zero gradient for v at x=L
    
    # Obstacle boundary conditions (no-slip)
    u_new[obstacle_mask] = 0
    v_new[obstacle_mask] = 0

    u_velocity = u_new
    v_velocity = v_new

    if t_step % 20 == 0: # Update animation less frequently
        # Clear previous quiver plot for animation
        if t_step > 0 and len(ax.collections) > 0:
             # Keep the obstacle imshow, remove only the quiver
            for q_coll in ax.collections:
                if isinstance(q_coll, plt.Quiver):
                    q_coll.remove()
            # If there was a colorbar for quiver, remove it too, but we won't add one per frame for quiver

        # Normalize arrows for quiver plot: Calculate magnitude, but scale for display
        # This basic normalization might need adjustment for visual clarity
        magnitude = np.sqrt(u_velocity**2 + v_velocity**2)
        # Prevent division by zero or very small magnitudes if any point has zero velocity
        # However, quiver handles zero-length arrows fine.
        # For scaling, we can set a fixed scale or scale by max magnitude
        max_mag = np.max(magnitude)
        if max_mag == 0: max_mag = 1.0 # Avoid division by zero if all velocities are zero
        
        # Quiver plot for velocity field
        # The 'scale' parameter in quiver adjusts arrow lengths. A larger scale means shorter arrows.
        # We might need to experiment with the scale value.
        # Let's try to make arrows visible but not overly dense or long.
        # A common approach is to set scale_units='xy', scale=constant, or scale_units='width', scale=constant
        quiver_plot = ax.quiver(X[skip], Y[skip], 
                                u_velocity[skip], v_velocity[skip], 
                                magnitude[skip], # Color by magnitude
                                cmap='viridis', 
                                scale=20, # Adjust this scale factor as needed
                                scale_units='inches', # 'inches' makes scale relative to plot size
                                headwidth=3, headlength=5, width=0.003,
                                pivot='mid')

        if t_step == 0: # Initial setup for the plot
            ax.imshow(obstacle_mask, origin='lower', extent=[0, L, 0, L], cmap='gray', alpha=0.5, zorder=0) # Show obstacle static
            ax.set_title(f"2D River Flow (Arrows) - Obstacle: {obstacle_type}")
            ax.set_xlabel("X position (m)")
            ax.set_ylabel("Y position (m) - Flow South to North")
            ax.set_xlim(0, L)
            ax.set_ylim(0, L)
            ax.set_aspect('equal')
            # Add a colorbar for the quiver magnitude if desired (can be static)
            # This colorbar will correspond to the magnitude used for coloring arrows
            cbar = fig.colorbar(quiver_plot, ax=ax, label='Velocity Magnitude (m/s)')

        ims.append([quiver_plot] + ([ax.imshow(obstacle_mask, origin='lower', extent=[0, L, 0, L], cmap='gray', alpha=0.5, zorder=0, animated=True)] if t_step > 0 else []))
        print(f"Step {t_step}/{int(T/dt)} completed. Inflow V: {inflow_v_value:.2f}", end='\r')

print("\nSimulation finished. Creating animation...")

ani = animation.ArtistAnimation(fig, ims, interval=100, blit=False, repeat_delay=1000)
# ani.save('river_flow_arrows.gif', writer='imagemagick', fps=10)
# print("Animation saved as river_flow_arrows.gif")
plt.show()

print("Program finished.")
