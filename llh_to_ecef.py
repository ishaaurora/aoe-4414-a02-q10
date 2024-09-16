# llh_to_ecef
#
# Usage: python3 llh_to_ecef.py lat_deg lon_deg hae_km
#Converts llh components to ecef 
# Parameters:
#  lat_deg: alttitude in degrees
#  lon_deg: longitude in degrees
# hae_km: Hieght above ellipsoid in km

# Output:
#  A description of the script output: Outputs rx ry rz which is ecef components in kn
#
# Written by Isha Aurora
# Other contributors: None
#
# Optional license statement, e.g., See the LICENSE file for the license.

# import Python modules
# e.g., import math # math module
import sys # argv
import math

# "constants"
R_E_KM = 6378.1363
e_E = .081819221456

# helper functions
def calc_denom(ecc,lat_rad):
   
   return math.sqrt(1 - (ecc*ecc)*(math.sin(lat_rad))**2)

## function description
# def calc_something(param1, param2):
#   pass

# initialize script arguments
lat_deg = float('nan')
lon_deg = float('nan')
hae_km = 0

# parse script arguments
if len(sys.argv)==4:
   lat_deg = float(sys.argv[1])
   lon_deg = float(sys.argv[2])
   hae_km = float(sys.argv[3])
else:
   print(\
    'Usage: '\
    'python3 llh_to_ecef.py lat_deg lon_deg hae_km ...'\
   )
   exit()

#in radians
lat_rad = lat_deg*math.pi/180
lon_rad = lon_deg*math.pi/180

# write script below this line
denom = calc_denom(e_E, lat_rad)
Ce = R_E_KM/denom 
Se = (R_E_KM*(1-e_E**2))/denom
rx_km = (Ce+hae_km)*math.cos(lat_rad)*math.cos(lon_rad)
ry_km = (Ce+hae_km)*math.cos(lat_rad)*math.sin(lon_rad)
rz_km = (Se+hae_km)*math.sin(lat_rad)

#answers:
print(rx_km)
print(ry_km)
print(rz_km)