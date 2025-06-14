import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# --- Simulation Parameters ---
K = 100  # Grid size in X axis (width)
N = 100  # Grid size in Y axis (height)
L_x = 1.0  # Domain length in X
L_y = 2.0  # Domain length in Y
dx = L_x / K  # Grid spacing in X
dy = L_y / N  # Grid spacing in Y
dt = 0.0001  # Time step (reduced for stability)
T = 1.0  # Total simulation time
nu = 0.01  # Viscosity


# --- Helper function to create obstacles ---
def create_obstacle_mask(shape, K, N, center_x, center_y, size_param):
    """
    Creates a boolean mask for a given obstacle shape.
    size_param is interpreted as half_size, radius, etc. depending on the shape.
    """
    mask = np.zeros((N, K), dtype=bool)

    if shape == 'square':
        half_size = int(N * size_param)
        mask[center_y - half_size: center_y + half_size,
        center_x - half_size: center_x + half_size] = True
    elif shape == 'rectangle':
        rect_height_half = int(N * size_param * 1.5)  # Make it taller
        rect_width_half = int(K * size_param * 0.5)  # Make it narrower
        mask[center_y - rect_height_half: center_y + rect_height_half,
        center_x - rect_width_half: center_x + rect_width_half] = True
    elif shape == 'circle':
        radius = int(N * size_param)
        y_coords, x_coords = np.ogrid[:N, :K]
        dist_from_center = np.sqrt((x_coords - center_x) ** 2 + (y_coords - center_y) ** 2)
        mask[dist_from_center <= radius] = True
    elif shape == 'triangle':
        height = int(N * size_param * 2)
        half_base_width = int(K * size_param)
        base_y = center_y - height // 2
        tip_y = base_y + height
        for y_coord in range(base_y, tip_y):
            if y_coord < 0 or y_coord >= N: continue
            current_half_width = int(half_base_width * (tip_y - y_coord) / height)
            start_x = max(0, center_x - current_half_width)
            end_x = min(K, center_x + current_half_width + 1)
            mask[y_coord, start_x:end_x] = True

    return mask


# --- User Controls ---
obstacle_type = input("Choose obstacle type (square, circle, rectangle, triangle, or none): ")

# --- Initialize THREE sets of velocity fields ---
u_flow_speed = 1.0
# Simulation 1 (Left subplot)
u1 = np.zeros((N, K))
v1 = np.ones((N, K)) * u_flow_speed
# Simulation 2 (Middle subplot)
u2 = np.zeros((N, K))
v2 = np.ones((N, K)) * u_flow_speed
# Simulation 3 (Right subplot)
u3 = np.zeros((N, K))
v3 = np.ones((N, K)) * u_flow_speed

# --- Define Obstacles for all simulations ---
# Mask 1: Single obstacle in the center
center_y_single = N // 2
mask1 = create_obstacle_mask(obstacle_type, K, N, center_x=K // 2, center_y=center_y_single, size_param=0.1)

# Mask 2: Two obstacles side-by-side
size_for_two = 0.08
mask2a = create_obstacle_mask(obstacle_type, K, N, center_x=K // 4, center_y=center_y_single, size_param=size_for_two)
mask2b = create_obstacle_mask(obstacle_type, K, N, center_x=3 * K // 4, center_y=center_y_single,
                              size_param=size_for_two)
mask2 = np.logical_or(mask2a, mask2b)

# Mask 3: Three obstacles in a triangle formation
size_for_three = 0.08
top_y = N // 2 + N // 10
bottom_y = N // 2 - N // 10
mask3a = create_obstacle_mask(obstacle_type, K, N, center_x=K // 4, center_y=top_y, size_param=size_for_three)
mask3b = create_obstacle_mask(obstacle_type, K, N, center_x=3 * K // 4, center_y=top_y, size_param=size_for_three)
mask3c = create_obstacle_mask(obstacle_type, K, N, center_x=K // 2, center_y=bottom_y, size_param=size_for_three)
mask3 = np.logical_or.reduce([mask3a, mask3b, mask3c])

if obstacle_type == 'none':
    mask1.fill(False)
    mask2.fill(False)
    mask3.fill(False)

# --- Setup the plot for three subplots ---
fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(20, 7))
ims = []

print(f"Starting simulation for {T / dt:.0f} steps...")

# --- Main Simulation Loop ---
for t_step in range(int(T / dt)):
    sim_data = [(u1, v1), (u2, v2), (u3, v3)]
    new_data = []

    # Process all three simulations
    for u, v in sim_data:
        u_xx = (np.roll(u, 1, axis=1) - 2 * u + np.roll(u, -1, axis=1)) / dx ** 2
        u_yy = (np.roll(u, 1, axis=0) - 2 * u + np.roll(u, -1, axis=0)) / dy ** 2
        v_xx = (np.roll(v, 1, axis=1) - 2 * v + np.roll(v, -1, axis=1)) / dx ** 2
        v_yy = (np.roll(v, 1, axis=0) - 2 * v + np.roll(v, -1, axis=0)) / dy ** 2

        u_adv_x = np.where(u > 0, (u - np.roll(u, 1, axis=1)) / dx, (np.roll(u, -1, axis=1) - u) / dx)
        u_adv_y = np.where(v > 0, (u - np.roll(u, 1, axis=0)) / dy, (np.roll(u, -1, axis=0) - u) / dy)
        v_adv_x = np.where(u > 0, (v - np.roll(v, 1, axis=1)) / dx, (np.roll(v, -1, axis=1) - v) / dx)
        v_adv_y = np.where(v > 0, (v - np.roll(v, 1, axis=0)) / dy, (np.roll(v, -1, axis=0) - v) / dy)

        u_new = u + dt * (-u * u_adv_x - v * u_adv_y + nu * (u_xx + u_yy))
        v_new = v + dt * (-u * v_adv_x - v * v_adv_y + nu * (v_xx + v_yy))
        new_data.append((u_new, v_new))

    # Apply Boundary Conditions and Obstacles to all simulations
    masks = [mask1, mask2, mask3]
    for i in range(3):
        u_new, v_new = new_data[i]
        mask = masks[i]

        # Neumann BCs on left/right walls
        u_new[:, 0], u_new[:, -1] = u_new[:, 1], u_new[:, -2]
        v_new[:, 0], v_new[:, -1] = v_new[:, 1], v_new[:, -2]

        # Obstacle no-slip condition
        u_new[mask], v_new[mask] = 0, 0

    # Update state variables
    u1, v1 = new_data[0]
    u2, v2 = new_data[1]
    u3, v3 = new_data[2]

    # --- Add frame to animation ---
    if t_step % 10 == 0:
        mag1 = np.sqrt(u1 ** 2 + v1 ** 2)
        mag2 = np.sqrt(u2 ** 2 + v2 ** 2)
        mag3 = np.sqrt(u3 ** 2 + v3 ** 2)

        common_vmax = u_flow_speed * 1.5

        img1 = ax1.imshow(mag1, origin='lower', extent=[0, L_x, 0, L_y], animated=True, cmap='Blues_r', vmin=0,
                          vmax=common_vmax)
        img2 = ax2.imshow(mag2, origin='lower', extent=[0, L_x, 0, L_y], animated=True, cmap='Blues_r', vmin=0,
                          vmax=common_vmax)
        img3 = ax3.imshow(mag3, origin='lower', extent=[0, L_x, 0, L_y], animated=True, cmap='Blues_r', vmin=0,
                          vmax=common_vmax)

        if t_step == 0:
            ax1.imshow(mask1, origin='lower', extent=[0, L_x, 0, L_y], cmap='gray', alpha=0.6)
            ax2.imshow(mask2, origin='lower', extent=[0, L_x, 0, L_y], cmap='gray', alpha=0.6)
            ax3.imshow(mask3, origin='lower', extent=[0, L_x, 0, L_y], cmap='gray', alpha=0.6)

            ax1.set_title(f'Flow with 1 "{obstacle_type}" obstacle')
            ax2.set_title(f'Flow with 2 "{obstacle_type}" obstacles')
            ax3.set_title(f'Flow with 3 "{obstacle_type}" obstacles')

            for ax in [ax1, ax2, ax3]:
                ax.set_xlabel("X Position (m)")
            ax1.set_ylabel("Y Position (m)")

            fig.colorbar(img3, ax=ax3, label='Velocity Magnitude (m/s)', shrink=0.75)

        ims.append([img1, img2, img3])
        print(f"Step {t_step}/{int(T / dt)} completed.", end='\r')

print("\nSimulation finished. Creating animation...")

# Create animation
ani = animation.ArtistAnimation(fig, ims, interval=50, blit=True, repeat_delay=1000)

# Save or show animation
try:
    save_filename = f'flow_animation_triple_{obstacle_type}.gif'
    ani.save(save_filename, writer='imagemagick', fps=15)
    print(f"Animation saved as {save_filename}")
except Exception as e:
    print(f"\nCould not save animation as GIF. Error: {e}")
    print("This may require 'imagemagick' to be installed on your system.")
    print("Showing animation in Matplotlib window instead.")
    plt.show()

print("Program finished.")