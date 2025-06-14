import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


def simulate_burgers_with_city(
        d_distance_to_city=None,  # km, will be prompted if None
        city_width=8.0,  # km
        dx=0.1,  # km, spatial step
        dt=0.01,  # time step
        nu=0.1,  # viscosity
        source_amplitude=0.3,  # Amplitude of the sinusoidal source
        source_frequency=0.8,  # Frequency of the sinusoidal source
        initial_baseline=0.01,
        simulation_time_factor=1.5  # Factor to determine total simulation time
):
    """
    Simulates the 1D Burger's equation with a wave source at the left boundary
    and a city further down the domain.

    The simulation prompts the user for 'd', the distance from the start of the
    simulation domain (source location) to the city's left edge.
    The city is represented by two vertical lines, 'city_width' km apart.
    The volume of water (integrated height) within the city is calculated and displayed.
    The x-axis represents distance in kilometers.
    A sinusoidal source is applied at the left boundary.
    The right boundary condition is zero-gradient (free outflow).
    """

    if d_distance_to_city is None:
        while True:
            try:
                d_str = input("Enter the distance 'd' from the source (left edge) to the city (in km): ")
                d_distance_to_city = float(d_str)
                if d_distance_to_city <= 0:
                    print("Distance 'd' must be positive.")
                else:
                    break
            except ValueError:
                print("Invalid input. Please enter a numerical value for 'd'.")

    # Domain length needs to accommodate the city and some space beyond it
    # Let's set it to d_distance_to_city + city_width + some buffer (e.g., d_distance_to_city / 2 or a fixed value)
    L = d_distance_to_city + city_width + d_distance_to_city / 2
    if L < city_width + 10:  # Ensure minimum length for visualization
        L = city_width + 10

    nx = int(L / dx) + 1
    x = np.linspace(0, L, nx)

    # Initial condition: baseline value
    u = np.full(nx, initial_baseline)

    u_hist = [u.copy()]

    # Estimate simulation time needed for the wave to reach and pass the city
    # This is trickier with a continuous source, let's set a reasonable simulation time
    # based on some wave propagation speed assumption and domain length.
    # Assuming a characteristic speed related to the source amplitude or a default value.
    char_speed = max(source_amplitude, 0.1)
    estimated_travel_time_to_city_end = (d_distance_to_city + city_width) / char_speed
    total_sim_time = estimated_travel_time_to_city_end * simulation_time_factor
    nt = int(total_sim_time / dt)

    nt = min(nt, 10000)  # Cap timesteps to avoid overly long runs, adjust as needed
    if nt * dt == 0:
        storage_frequency = 1
    else:
        storage_frequency = max(1, nt // 200)  # Store ~200 frames for animation

    print(f"Simulation parameters: L={L:.2f}km, dx={dx}km, dt={dt}, nu={nu}")
    print(f"City from {d_distance_to_city:.2f}km to {d_distance_to_city + city_width:.2f}km")
    print(f"Source amplitude={source_amplitude}, frequency={source_frequency}")
    print(f"Target simulation time: {total_sim_time:.2f} (nt={nt} steps). Storing every {storage_frequency} steps.")

    for n_iter in range(nt):
        un = u.copy()

        u[1:-1] = (un[1:-1] -
                   dt * un[1:-1] * (un[2:] - un[0:-2]) / (2 * dx) +
                   nu * dt * (un[2:] - 2 * un[1:-1] + un[0:-2]) / dx ** 2)

        # Boundary condition: sinusoidal inflow on the left
        current_time_step = n_iter * dt
        u[0] = source_amplitude * abs(np.sin(2 * np.pi * source_frequency * current_time_step)) + initial_baseline

        # Right boundary: free outflow (Neumann-like)
        u[-1] = u[-2]

        if n_iter % storage_frequency == 0:
            u_hist.append(u.copy())

    print(f"Simulation finished. Stored {len(u_hist)} frames.")

    fig, ax = plt.subplots(figsize=(12, 7))
    line, = ax.plot(x, u_hist[0], lw=2, color='blue')

    city_start_x = d_distance_to_city
    city_end_x = d_distance_to_city + city_width
    ax.axvline(x=city_start_x, color='red', linestyle='--', linewidth=2, label=f'City Start ({city_start_x:.1f} km)')
    ax.axvline(x=city_end_x, color='red', linestyle='--', linewidth=2, label=f'City End ({city_end_x:.1f} km)')

    max_u_overall = np.max(u_hist) if len(u_hist) > 0 and np.max(
        u_hist) > initial_baseline else source_amplitude + initial_baseline
    min_u_overall = np.min(u_hist) if len(u_hist) > 0 else initial_baseline
    ax.set_ylim(min_u_overall - 0.1 * abs(max_u_overall if max_u_overall != 0 else 1), max_u_overall * 1.1 + 0.1)

    volume_text_x = city_start_x + city_width / 2
    volume_text_y = ax.get_ylim()[1] * 0.93
    volume_text = ax.text(volume_text_x, volume_text_y, '', ha='center', fontsize=10,
                          bbox=dict(facecolor='white', alpha=0.8, edgecolor='lightgray'))

    ax.set_xlabel("Distance (km)", fontsize=12)
    ax.set_ylabel("Wave Height (u)", fontsize=12)
    ax.legend(loc='upper right', fontsize=10)
    ax.grid(True, linestyle=':', alpha=0.7)

    city_indices = np.where((x >= city_start_x) & (x <= city_end_x))[0]

    def update(frame_num):
        current_u = u_hist[frame_num]
        line.set_ydata(current_u)

        integrated_height = 0.0
        if len(city_indices) > 0:
            current_u_in_city = current_u[city_indices]
            integrated_height = np.sum(current_u_in_city) * dx

        volume_text.set_text(f'Integrated height in city: {integrated_height:.3f}')
        current_time_in_animation = frame_num * dt * storage_frequency
        ax.set_title(
            f"1D Burger's Model: Wave from source approaching city (d={d_distance_to_city} km)\nTime: {current_time_in_animation:.2f}",
            fontsize=14)
        return line, volume_text

    ani_interval = 70
    ani = FuncAnimation(fig, update, frames=len(u_hist), interval=ani_interval, blit=True, repeat=False)

    animation_file = 'burgers_simulation_with_source.gif'
    try:
        ani.save(animation_file, writer='imagemagick', fps=15)
        print(f"Animation saved to {animation_file}")
    except Exception as e:
        print(f"Could not save animation: {e}. Ensure imagemagick or ffmpeg is installed and in your PATH.")
        print("Attempting to save with Pillow as fallback...")
        try:
            ani.save(animation_file, writer='pillow', fps=15)
            print(f"Animation saved to {animation_file} using Pillow.")
        except Exception as e2:
            print(f"Could not save animation with Pillow either: {e2}")


if __name__ == '__main__':
    simulate_burgers_with_city(d_distance_to_city=20.0)