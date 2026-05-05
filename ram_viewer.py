import wmi

def get_ram_details():
    c = wmi.WMI()
    
    print(f"{'Manufacturer':<20} | {'Capacity (GB)':<15} | {'Speed (MHz)':<10} | {'Part Number'}")
    print("-" * 70)
    
    for ram in c.Win32_PhysicalMemory():
        # Convert capacity from Bytes to GB
        capacity_gb = round(int(ram.Capacity) / (1024**3), 2)
        
        manufacturer = ram.Manufacturer
        speed = ram.Speed
        part_number = ram.PartNumber.strip()  # Full model code
        
        print(f"{manufacturer:<20} | {capacity_gb:<15} | {speed:<10} | {part_number}")

if __name__ == "__main__":
    try:
        get_ram_details()
    except Exception as e:
        print(f"An error occurred: {e}")



#2. option
# or short form of the request with minimal details:

import os

# Send query directly to command line
os.system('wmic memorychip get devicelocator, manufacturer, partnumber, speed, capacity')