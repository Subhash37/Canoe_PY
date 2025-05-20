"""
Example demonstrating connection and basic configuration functions
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
        
        # Get version
        version = canoe.get_version()
        print(f"CANoe version: {version}")
        
        # Get status
        status = canoe.get_status()
        print(f"CANoe status: {status}")
        
        # Create new configuration
        canoe.new(auto_save=False, prompt_user=False)
        print("Created new configuration")
        
        # Example configuration path - update with a valid path for your system
        config_path = os.path.abspath("../tests/demo_cfg/demo.cfg")
        if os.path.exists(config_path):
            # Open configuration
            canoe.open_configuration(config_path)
            print(f"Opened configuration: {config_path}")
        
        # Save configuration
        canoe.save_configuration()
        print("Saved configuration")
        
        # Save configuration as
        new_config_path = os.path.abspath("../tests/demo_cfg/my_test_config.cfg")
        canoe.save_configuration_as(new_config_path)
        print(f"Saved configuration as: {new_config_path}")
        
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