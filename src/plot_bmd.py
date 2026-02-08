import xarray as xr
import matplotlib.pyplot as plt

# Load dataset
ds = xr.open_dataset("../data/screening_task.nc")


# Central longitudinal girder elements (Task-1)
central_elements = [15, 24, 33, 42, 51, 60, 69, 78, 83]

# Lists to store bending moment values
Mz_values = []
element_numbers = []

for elem in central_elements:
    # Extract Mz at i and j end
    mz_i = ds["forces"].sel(Element=elem, Component="Mz_i").values
    mz_j = ds["forces"].sel(Element=elem, Component="Mz_j").values

    # Append values (continuous diagram)
    Mz_values.append(mz_i)
    element_numbers.append(elem - 0.5)

    Mz_values.append(mz_j)
    element_numbers.append(elem + 0.5)

# Plot Bending Moment Diagram
plt.figure(figsize=(10, 5))
plt.plot(element_numbers, Mz_values, marker='o')
plt.xlabel("Element Number")
plt.ylabel("Bending Moment (Mz)")
plt.title("Bending Moment Diagram (BMD) - Central Girder")
plt.grid(True)

# Save result
plt.savefig("../results/bmd.png", dpi=300)
plt.show()
