import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


def simulate_2d_burgers_with_city_surface_plot(
        distance_to_city_km=100.0,
        city_width_km=15.0,
        city_depth_km=8.0,
        domain_width_km=15.0,
        dx=0.5,   # km
        dy=0.5,   # km
        dt=0.04,  # hr
        nu=1.2,   # viscosity
        max_source_amplitude=1.5,
        source_frequency=0.5,
        simulation_time_h=24.0 * 60,
):
    # --- Stability check (CFL) ---
    dt_diff = min(dx, dy) ** 2 / (4 * nu)
    dt_adv = min(dx, dy) / (max_source_amplitude + 1e-6)
    print(f"dt ≤ {dt_diff:.3f} (diff), dt ≤ {dt_adv:.3f} (adv)")
    if dt > dt_diff or dt > dt_adv:
        print("Uwaga: dt może być niestabilne!")

    # --- Grid setup ---
    domain_length_km = distance_to_city_km + city_depth_km + distance_to_city_km / 2
    nx, ny = int(domain_width_km / dx), int(domain_length_km / dy)
    x = np.linspace(0, domain_width_km, nx)
    y = np.linspace(0, domain_length_km, ny)
    X, Y = np.meshgrid(x, y)

    # --- Initial fields ---
    u = np.zeros((ny, nx))
    v = np.zeros((ny, nx))

    nt = int(simulation_time_h / dt)
    store = max(1, nt // 150)
    v_hist = []

    # --- Main time loop ---
    for n in range(nt):
        un, vn = u.copy(), v.copy()

        # diffusion
        u_xx = (np.roll(un, 1, 1) - 2 * un + np.roll(un, -1, 1)) / dx ** 2
        u_yy = (np.roll(un, 1, 0) - 2 * un + np.roll(un, -1, 0)) / dy ** 2
        v_xx = (np.roll(vn, 1, 1) - 2 * vn + np.roll(vn, -1, 1)) / dx ** 2
        v_yy = (np.roll(vn, 1, 0) - 2 * vn + np.roll(vn, -1, 0)) / dy ** 2

        # reversed advection (wave goes downward)
        u_adv_x = un * (np.roll(un, -1, 1) - un) / dx
        u_adv_y = vn * (np.roll(un, -1, 0) - un) / dy
        v_adv_x = un * (np.roll(vn, -1, 1) - vn) / dx
        v_adv_y = vn * (np.roll(vn, -1, 0) - vn) / dy

        # time update
        u = un + dt * (nu * (u_xx + u_yy) + u_adv_x + u_adv_y)
        v = vn + dt * (nu * (v_xx + v_yy) + v_adv_x + v_adv_y)

        # source at top edge
        t = n * dt
        gf = min(1.0, t / simulation_time_h)
        amp = min(max_source_amplitude * gf, max_source_amplitude / 2)
        v[-1, :] = amp + 0.1 * np.sin(2 * np.pi * source_frequency * t)
        u[-1, :] = 0

        # free outflow at bottom
        u[0, :] = u[1, :]
        v[0, :] = v[1, :]
        # free outflow sides
        u[:, 0], u[:, -1] = u[:, 1], u[:, -2]
        v[:, 0], v[:, -1] = v[:, 1], v[:, -2]

        if n % store == 0:
            v_hist.append(np.sqrt(u ** 2 + v ** 2))

    print(f"Stored {len(v_hist)} frames.")

    # --- Animation setup ---
    fig = plt.figure(figsize=(14, 10))
    ax = fig.add_subplot(111, projection='3d')
    max_z = np.max(v_hist)

    # coordinates for levees at x=0 and x=Lx
    Lx = domain_width_km
    Ly = domain_length_km
    # two vertical planes for levees
    Z_lev = np.array([[0., 0.],
                      [.6, .6]])
    Y_lev = np.array([[0., Ly],
                      [0., Ly]])
    X0 = np.full_like(Z_lev, fill_value=0)  # x=0
    X1 = np.full_like(Z_lev, fill_value=Lx)  # x=Lx

    def update(i):
        ax.clear()
        Z = v_hist[i]
        # surface
        ax.plot_surface(X, Y, Z, cmap='Blues_r',
                        vmin=0, vmax=max_z, edgecolor='none')

        # green levees
        ax.plot_surface(X0, Y_lev, Z_lev, color='green', alpha=0.5)
        ax.plot_surface(X1, Y_lev, Z_lev, color='green', alpha=0.5)

        # red city footprint sticking out of domain
        cx = (domain_width_km - city_width_km) / 2
        cy = domain_length_km - distance_to_city_km
        eps = 3 * dx  # margines w km, można dostosować

        # Rozszerzamy footprint o eps w osi X
        Xc = np.array([
            [cx - eps, cx + city_width_km + eps],
            [cx - eps, cx + city_width_km + eps]
        ])
        Yc = np.array([
            [cy, cy],
            [cy + city_depth_km, cy + city_depth_km]
        ])
        # podnieś troszkę nad max_z, żeby była dobrze widoczna
        Zc = np.full_like(Xc, max_z * 0.0)

        ax.plot_surface(Xc, Yc, Zc, color='red', alpha=0.6)

        ax.set_zlim(0, max_z * 1.1)
        ax.set_xlabel("Width of the river (m)")
        ax.set_ylabel("Length of the river (km)")
        ax.set_zlabel("Height (m)")
        ax.view_init(elev=25, azim=-65)
        ax.set_title(f"Time: {i * dt * store:.2f}h", fontsize=14)

    ani = FuncAnimation(fig, update, frames=len(v_hist),
                        interval=50, blit=False)

    try:
        ani.save(f'burgers2d_with_levees_{max_source_amplitude}.gif', writer='pillow', fps=20)
        print("Saved: burgers2d_with_levees.gif")
    except Exception as e:
        print(f"Error saving: {e}")


if __name__ == '__main__':
    simulate_2d_burgers_with_city_surface_plot()
