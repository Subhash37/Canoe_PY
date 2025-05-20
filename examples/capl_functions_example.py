"""
Example demonstrating CAPL function calls
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
        canoe = MyCANoe(
            log_level=logging.INFO, 
            user_capl_functions=('addition_function', 'hello_world')
        )
        
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
        
        try:
            # Compile all CAPL nodes
            compile_result = canoe.compile_all_capl_nodes()
            print(f"Compilation result: {compile_result}")
            
            # Call CAPL function with parameters
            result = canoe.call_capl_function("addition_function", 10, 20)
            print(f"Called CAPL function 'addition_function' with parameters 10, 20. Result: {result}")
            
            # Call CAPL function without parameters
            canoe.call_capl_function("hello_world")
            print("Called CAPL function 'hello_world' without parameters")
        except MyCANoeException as e:
            print(f"CAPL function operation failed: {e}")
            print("This may be due to missing CAPL functions in your configuration")
        
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