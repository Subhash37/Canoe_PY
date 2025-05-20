"""
Example demonstrating signal handling functions
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
        
        # Example signal parameters - update with valid values for your configuration
        bus = "CAN"
        channel = 1
        message = "LightState"
        signal = "FlashLight"
        
        try:
            # Get signal full name
            signal_full_name = canoe.get_signal_full_name(bus, channel, message, signal)
            print(f"Signal full name: {signal_full_name}")
            
            # Get signal value
            signal_value = canoe.get_signal_value(bus, channel, message, signal)
            print(f"Signal value: {signal_value}")
            
            # Set signal value
            new_signal_value = 1
            canoe.set_signal_value(bus, channel, message, signal, new_signal_value)
            print(f"Set signal value to {new_signal_value}")
            
            # Verify new signal value
            updated_signal_value = canoe.get_signal_value(bus, channel, message, signal)
            print(f"Updated signal value: {updated_signal_value}")
        except MyCANoeException as e:
            print(f"Signal operation failed: {e}")
            print("This may be due to missing signals in your configuration")
        
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