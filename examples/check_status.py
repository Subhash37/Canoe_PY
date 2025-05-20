"""
Example script to check CANoe status
"""

import sys
import logging
import os

# Add the parent directory to the path so we can import the library
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from my_canoe_lib import MyCANoe, MyCANoeException

def main():
    try:
        # Create MyCANoe instance with debug logging
        canoe = MyCANoe(log_level=logging.INFO)
        
        # Get and print status
        status = canoe.get_status()
        
        print("\nCANoe Status:")
        print(f"  Version: {status['version']}")
        print(f"  Measurement running: {'Yes' if status['measurement_running'] else 'No'}")
        print(f"  Configuration: {status['configuration']}")
        print(f"  Timestamp: {status['timestamp']}")
        
        return 0
        
    except MyCANoeException as e:
        print(f"MyCANoe Error: {str(e)}")
        return 1
    except Exception as e:
        print(f"Unexpected error: {str(e)}")
        return 1

if __name__ == "__main__":
    sys.exit(main())