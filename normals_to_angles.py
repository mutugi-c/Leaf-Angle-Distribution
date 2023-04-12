import math
import pandas as pd

# Read the CSV file and calculate the absolute value of z-coordinates
file = pd.read_csv(
    r"file_normals.xyz",
    sep=' ',
    header=None,
    names=['x', 'y', 'z'],
    encoding='utf-8',
    usecols=['x', 'y', 'z']
)
file = file.loc[(file != 0).any(1)]

file['z'] = file['z'].abs()

# Define z as a tuple
z = (0, 0, 1)


def zenith_angle(a, z):
    '''This function calculates the angle between a normal vector and the z axis.'''
    # Calculate a.z
    az = a[0]*z[0] + a[1]*z[1] + a[2]*z[2]

    # Calculate ||a||.||Z|| i.e. magnitudes of a and Z
    magnitude_a = math.sqrt(a[0]*a[0] + a[1]*a[1] + a[2]*a[2])
    magnitude_z = math.sqrt(z[0]*z[0] + z[1]*z[1] + z[2]*z[2])
    dot_magnitude = magnitude_a * magnitude_z

    # Calculate zenith angle in degrees
    z_angle_rad = math.acos(az/dot_magnitude)
    zenith_angle = z_angle_rad * (180/math.pi)

    return zenith_angle


# Calculate inclination angles for each normal vector and save to a CSV file
with open(r'LAD.csv', 'w', newline='', encoding='utf-8') as f:
    f.write('Angle_degree\n')

    for i, a in enumerate(file.itertuples(index=False)):
        inclination = zenith_angle(a, z)
        angles = pd.DataFrame([[inclination]], columns=['Angle_degree'])

        # Only include header in the first row
        if i == 0:
            angles.to_csv(f, header=False, index=False)
        else:
            angles.to_csv(f, header=False, index=False)
