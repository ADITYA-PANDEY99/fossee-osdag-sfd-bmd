import xarray as xr
import matplotlib.pyplot as plt
import os

# Load dataset
ds = xr.open_dataset("../data/screening_task.nc")

forces = ds["forces"]
elements = ds["Element"].values
components = list(ds["Component"].values)

# Indices for Vy and Mz
vy_idx = components.index("Vy_i")
mz_idx = components.index("Mz_i")

Vy = forces[:, vy_idx].values
Mz = forces[:, mz_idx].values

# Create results folder if not exists
os.makedirs("../results", exist_ok=True)

# Create subplots
fig, axs = plt.subplots(2, 1, figsize=(10, 8))

# SFD
axs[0].plot(elements, Vy, marker="o")
axs[0].set_title("Shear Force Diagram (SFD)")
axs[0].set_xlabel("Element Number")
axs[0].set_ylabel("Shear Force Vy (kN)")
axs[0].grid(True)

# BMD
axs[1].plot(elements, Mz, marker="o")
axs[1].set_title("Bending Moment Diagram (BMD)")
axs[1].set_xlabel("Element Number")
axs[1].set_ylabel("Bending Moment Mz (kN.m)")
axs[1].grid(True)

plt.tight_layout()

# SAVE IMAGE (IMPORTANT LINE)
plt.savefig("../results/sfd_bmd.png", dpi=300)

# SHOW GRAPH
plt.show()
