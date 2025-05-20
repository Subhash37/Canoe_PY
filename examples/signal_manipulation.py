"""
Example script to manipulate signals in CANoe
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
        # Create MyCANoe instance
        canoe = MyCANoe(log_level=logging.INFO)
        
        # Check if measurement is running
        if not canoe.is_measurement_running():
            print("Measurement is not running. Starting measurement...")
            canoe.start_measurement()
        
        # Example: Get and set environment variables
        # Replace with actual environment variables from your configuration
        try:
            var_name = "Cybersecurity::CID_value"  # Example variable name
            
            # Get current value
            current_value = canoe.get_environment_variable(var_name)
            print(f"Current value of {var_name}: {current_value}")
            
            # Set new value
            new_value = 100
            canoe.set_environment_variable(var_name, new_value)
            print(f"Set {var_name} to {new_value}")
            
            # Verify new value
            updated_value = canoe.get_environment_variable(var_name)
            print(f"Updated value of {var_name}: {updated_value}")
            
        except MyCANoeException as e:
            print(f"Failed to access environment variable: {e}")
            print("This example requires appropriate environment variables in your CANoe configuration.")
        
        return 0
        
    except MyCANoeException as e:
        print(f"MyCANoe Error: {str(e)}")
        return 1
    except Exception as e:
        print(f"Unexpected error: {str(e)}")
        return 1

if __name__ == "__main__":
    sys.exit(main())