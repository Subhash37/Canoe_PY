"""
Example script to manipulate both system and environment variables in CANoe
"""

import sys
import logging
import os
import time

# Add the parent directory to the path so we can import the library
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from my_canoe_lib import MyCANoe, MyCANoeException

def main():
    try:
        # Create MyCANoe instance with user CAPL functions
        canoe = MyCANoe(log_level=logging.INFO)
        
        # Connect to CANoe first
        canoe._connect_to_canoe()
        
        # Check if measurement is running
        if not canoe.is_measurement_running():
            print("Measurement is not running. Starting measurement...")
            canoe.start_measurement()
        
        print("\n--- System Variables Example ---")
        # Example: Get and set system variables
        try:
            # Use a system variable that exists in the demo configuration
            sys_var_name = "Cybersecurity::CID_value"  # Example system variable from the demo config
            
            # Get current value
            current_value = canoe.get_system_variable_value(sys_var_name)
            print(f"Current value of system variable {sys_var_name}: {current_value}")
            
            # Set new value
            new_value = 100
            canoe.set_system_variable_value(sys_var_name, new_value)
            print(f"Set system variable {sys_var_name} to {new_value}")
            
            # Verify new value
            updated_value = canoe.get_system_variable_value(sys_var_name)
            print(f"Updated value of system variable {sys_var_name}: {updated_value}")
            
        except MyCANoeException as e:
            print(f"Failed to access system variable: {e}")
            print("This example requires appropriate system variables in your CANoe configuration.")
        
        return 0
        
    except MyCANoeException as e:
        print(f"MyCANoe Error: {str(e)}")
        return 1
    except Exception as e:
        print(f"Unexpected error: {str(e)}")
        return 1

if __name__ == "__main__":
    sys.exit(main())



