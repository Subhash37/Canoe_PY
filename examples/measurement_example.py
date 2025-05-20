"""
Example demonstrating measurement control functions
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
        
        # Start measurement
        canoe.start_measurement()
        print("Started measurement")
        time.sleep(2)  # Wait for measurement to start
        
        # Check if measurement is running
        is_running = canoe.is_measurement_running()
        print(f"Measurement running: {is_running}")
        
        # Reset measurement
        canoe.reset_measurement()
        print("Reset measurement")
        time.sleep(2)  # Wait for reset to complete
        
        # Stop measurement
        canoe.stop_measurement()
        print("Stopped measurement")
        time.sleep(1)  # Wait for stop to complete
        
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