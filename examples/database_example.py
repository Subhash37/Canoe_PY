"""
Example demonstrating database management functions
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
        
        # Create new configuration
        canoe.new(auto_save=False, prompt_user=False)
        print("Created new configuration")
        
        # Example database path - update with a valid path for your system
        db_path = os.path.abspath("../tests/demo_cfg/Databases/demo.dbc")
        
        try:
            # Add database
            canoe.add_database(db_path)
            print(f"Added database: {db_path}")
            
            # Wait a moment to ensure database is loaded
            time.sleep(1)
            
            # Remove database
            canoe.remove_database(db_path)
            print(f"Removed database: {db_path}")
        except MyCANoeException as e:
            print(f"Database operation failed: {e}")
            print("This may be due to an invalid database path")
        
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