import os
import xarray as xr
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Load dataset
ds = xr.open_dataset("../data/screening_task.nc")
forces = ds["forces"]
components = list(ds["Component"].values)

vy_i = components.index("Vy_i")

# Girder elements
girders = {
    1: [13, 22, 31, 40, 49, 58, 67, 76, 81],
    2: [14, 23, 32, 41, 50, 59, 68, 77, 82],
    3: [15, 24, 33, 42, 51, 60, 69, 78, 83],
    4: [16, 25, 34, 43, 52, 61, 70, 79, 84],
    5: [17, 26, 35, 44, 53, 62, 71, 80, 85]
}

fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot(111, projection="3d")

for g, elems in girders.items():
    Vy = [forces.sel(Element=e).values[vy_i] for e in elems]
    x = range(len(elems))
    y = [g] * len(elems)
    ax.plot(x, y, Vy, linewidth=2, label=f"Girder {g}")

ax.set_title("3D Shear Force Diagram (Vy in kN)", fontsize=12)
ax.set_xlabel("Element Index")
ax.set_ylabel("Girder Number")
ax.set_zlabel("Shear Force Vy (kN)")
ax.legend()
ax.grid(True)

os.makedirs("../results", exist_ok=True)
plt.savefig("../results/task2_3d_sfd.png", dpi=300)
plt.show()

import os
import xarray as xr
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Load dataset
ds = xr.open_dataset("../data/screening_task.nc")
forces = ds["forces"]
components = list(ds["Component"].values)

mz_i = components.index("Mz_i")

# Girder elements
girders = {
    1: [13, 22, 31, 40, 49, 58, 67, 76, 81],
    2: [14, 23, 32, 41, 50, 59, 68, 77, 82],
    3: [15, 24, 33, 42, 51, 60, 69, 78, 83],
    4: [16, 25, 34, 43, 52, 61, 70, 79, 84],
    5: [17, 26, 35, 44, 53, 62, 71, 80, 85]
}

fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot(111, projection="3d")

for g, elems in girders.items():
    Mz = [forces.sel(Element=e).values[mz_i] for e in elems]
    x = range(len(elems))
    y = [g] * len(elems)
    ax.plot(x, y, Mz, linewidth=2, label=f"Girder {g}")

ax.set_title("3D Bending Moment Diagram (Mz in kN·m)", fontsize=12)
ax.set_xlabel("Element Index")
ax.set_ylabel("Girder Number")
ax.set_zlabel("Bending Moment Mz (kN·m)")
ax.legend()
ax.grid(True)

os.makedirs("../results", exist_ok=True)
plt.savefig("../results/task2_3d_bmd.png", dpi=300)
plt.show()
