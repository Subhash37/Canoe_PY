"""
Example demonstrating system variable functions
"""

import sys
import logging
import os
import time

# Add the parent directory to the path so we can import the library
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from Canoe_PY import MyCANoe, MyCANoeException

def main():
    try:
        # Create MyCANoe instance
        canoe = MyCANoe(log_level=logging.INFO)
        
        # Connect to CANoe
        canoe._connect_to_canoe()
        print("Connected to CANoe")
        
        # Example configuration path - update with a valid path for your system
        config_path = os.path.abspath("../tests/demo_cfg/demo.cfg")
        if os.path.exists(config_path):
            # Open configuration
            canoe.open_configuration(config_path)
            print(f"Opened configuration: {config_path}")
        
        # Start measurement
        canoe.start_measurement()
        print("Started measurement")
        time.sleep(2)  # Wait for measurement to start
        
        # Example system variable - update with valid values for your configuration
        sys_var_name = "sys_var_demo::speed"
        
        try:
            # Set system variable
            sys_var_value = 50
            canoe.set_system_variable_value(sys_var_name, sys_var_value)
            print(f"Set system variable {sys_var_name} to {sys_var_value}")
            
            # Get system variable
            retrieved_sys_var_value = canoe.get_system_variable_value(sys_var_name)
            print(f"Retrieved system variable {sys_var_name}: {retrieved_sys_var_value}")
            
            # Set system variable array
            array_var_name = "sys_var_demo::int_array_var"
            array_values = (10, 20, 30, 40, 50)
            canoe.set_system_variable_array_values(array_var_name, array_values)
            print(f"Set system variable array {array_var_name} to {array_values}")
            
            # Get system variable array
            retrieved_array = canoe.get_system_variable_value(array_var_name)
            print(f"Retrieved system variable array {array_var_name}: {retrieved_array}")
        except MyCANoeException as e:
            print(f"System variable operation failed: {e}")
            print("This may be due to missing system variables in your configuration")
        
        # Stop measurement
        canoe.stop_measurement()
        print("Stopped measurement")
        
        # Quit CANoe
        canoe.quit()
        print("Quit CANoe")
        
        return 0
        
    except MyCANoeException as e:
        print(f"MyCANoe Error: {str(e)}")
        return 1
    except Exception as e:
        print(f"Unexpected error: {str(e)}")
        return 1

if __name__ == "__main__":
    sys.exit(main())

