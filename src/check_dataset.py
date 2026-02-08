import xarray as xr


ds = xr.open_dataset("../data/screening_task.nc")


print("DATASET LOADED SUCCESSFULLY\n")
print(ds)

print("\nDATA VARIABLES:")
print(list(ds.data_vars))

print("\nDIMENSIONS:")
print(ds.dims)
