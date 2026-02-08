import os
import xarray as xr
import matplotlib.pyplot as plt

# -------------------------------
# Load dataset
# -------------------------------
ds = xr.open_dataset("../data/screening_task.nc")

forces = ds["forces"]
components = list(ds["Component"].values)

# Get indices
vy_i = components.index("Vy_i")
vy_j = components.index("Vy_j")
mz_i = components.index("Mz_i")
mz_j = components.index("Mz_j")

# Central girder elements
central_elements = [15, 24, 33, 42, 51, 60, 69, 78, 83]

Vy = []
Mz = []

for e in central_elements:
    Vy.append(forces.sel(Element=e).values[vy_i])
    Mz.append(forces.sel(Element=e).values[mz_i])

# Create results folder
os.makedirs("../results", exist_ok=True)

# -------------------------------
# Plot
# -------------------------------
fig, axs = plt.subplots(2, 1, figsize=(10, 8))

# SFD
axs[0].plot(central_elements, Vy, marker="o", color="blue", linewidth=2)
axs[0].set_title("Shear Force Diagram (SFD) — Central Girder", fontsize=12)
axs[0].set_xlabel("Element Number")
axs[0].set_ylabel("Shear Force Vy (kN)")
axs[0].grid(True)

# BMD
axs[1].plot(central_elements, Mz, marker="o", color="red", linewidth=2)
axs[1].set_title("Bending Moment Diagram (BMD) — Central Girder", fontsize=12)
axs[1].set_xlabel("Element Number")
axs[1].set_ylabel("Bending Moment Mz (kN·m)")
axs[1].grid(True)

plt.tight_layout()
plt.savefig("../results/task1_sfd_bmd.png", dpi=300)
plt.show()

