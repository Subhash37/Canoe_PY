"""
Example demonstrating environment variable functions
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
        
        # Example environment variable - update with valid values for your configuration
        env_var_name = "int_var"
        
        try:
            # Set environment variable
            env_var_value = 100
            canoe.set_environment_variable_value(env_var_name, env_var_value)
            print(f"Set environment variable {env_var_name} to {env_var_value}")
            
            # Get environment variable
            retrieved_env_var_value = canoe.get_environment_variable_value(env_var_name)
            print(f"Retrieved environment variable {env_var_name}: {retrieved_env_var_value}")
            
            # Set different types of environment variables
            canoe.set_environment_variable_value("float_var", 123.456)
            print("Set float environment variable")
            
            canoe.set_environment_variable_value("string_var", "Hello from Python")
            print("Set string environment variable")
            
            canoe.set_environment_variable_value("data_var", (1, 2, 3, 4, 5))
            print("Set data environment variable")
        except MyCANoeException as e:
            print(f"Environment variable operation failed: {e}")
            print("This may be due to missing environment variables in your configuration")
        
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