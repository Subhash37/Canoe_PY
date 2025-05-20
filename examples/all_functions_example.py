"""
Comprehensive example demonstrating all functions in the MyCANoe library
"""

import sys
import logging
import os
import time
from typing import Dict, Any

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
        print("\n=== MyCANoe Library - All Functions Example ===\n")
        
        # === Basic Connection and Configuration ===
        print("\n--- Basic Connection and Configuration ---")
        
        # Connect to CANoe
        canoe._connect_to_canoe()
        print("✓ Connected to CANoe")
        
        # Get version
        version = canoe.get_version()
        print(f"✓ CANoe version: {version}")
        
        # Get status
        status = canoe.get_status()
        print(f"✓ CANoe status: {status}")
        
        # Create new configuration
        canoe.new(auto_save=False, prompt_user=False)
        print("✓ Created new configuration")
        
        # Example configuration path - update with a valid path for your system
        demo_config_path = os.path.abspath("../tests/demo_cfg/demo.cfg")
        if os.path.exists(demo_config_path):
            # Open configuration
            canoe.open_configuration(demo_config_path)
            print(f"✓ Opened configuration: {demo_config_path}")
        else:
            print(f"✗ Configuration not found: {demo_config_path}")
            print("  Continuing with new configuration")
        
        # Save configuration
        canoe.save_configuration()
        print("✓ Saved configuration")
        
        # Save configuration as
        new_config_path = os.path.abspath("../tests/demo_cfg/my_test_config.cfg")
        canoe.save_configuration_as(new_config_path)
        print(f"✓ Saved configuration as: {new_config_path}")
        
        # === Measurement Control ===
        print("\n--- Measurement Control ---")
        
        # Start measurement
        canoe.start_measurement()
        print("✓ Started measurement")
        time.sleep(1)  # Wait for measurement to start
        
        # Check if measurement is running
        is_running = canoe.is_measurement_running()
        print(f"✓ Measurement running: {is_running}")
        
        # Reset measurement
        canoe.reset_measurement()
        print("✓ Reset measurement")
        time.sleep(1)  # Wait for reset to complete
        
        # Stop measurement
        canoe.stop_measurement()
        print("✓ Stopped measurement")
        time.sleep(1)  # Wait for stop to complete
        
        # === Signal Handling ===
        print("\n--- Signal Handling ---")
        
        # Start measurement again for signal operations
        canoe.start_measurement()
        print("✓ Started measurement for signal operations")
        time.sleep(1)  # Wait for measurement to start
        
        # Example signal parameters - update with valid values for your configuration
        bus = "CAN"
        channel = 1
        message = "LightState"
        signal = "FlashLight"
        
        try:
            # Get signal full name
            signal_full_name = canoe.get_signal_full_name(bus, channel, message, signal)
            print(f"✓ Signal full name: {signal_full_name}")
            
            # Get signal value
            signal_value = canoe.get_signal_value(bus, channel, message, signal)
            print(f"✓ Signal value: {signal_value}")
            
            # Set signal value
            new_signal_value = 1
            canoe.set_signal_value(bus, channel, message, signal, new_signal_value)
            print(f"✓ Set signal value to {new_signal_value}")
            
            # Verify new signal value
            updated_signal_value = canoe.get_signal_value(bus, channel, message, signal)
            print(f"✓ Updated signal value: {updated_signal_value}")
        except MyCANoeException as e:
            print(f"✗ Signal operation failed: {e}")
            print("  This may be due to missing signals in your configuration")
        
        # === Environment Variables ===
        print("\n--- Environment Variables ---")
        
        # Example environment variable - update with valid values for your configuration
        env_var_name = "int_var"
        
        try:
            # Set environment variable
            env_var_value = 100
            canoe.set_environment_variable_value(env_var_name, env_var_value)
            print(f"✓ Set environment variable {env_var_name} to {env_var_value}")
            
            # Get environment variable
            retrieved_env_var_value = canoe.get_environment_variable_value(env_var_name)
            print(f"✓ Retrieved environment variable {env_var_name}: {retrieved_env_var_value}")
            
            # Set different types of environment variables
            canoe.set_environment_variable_value("float_var", 123.456)
            print("✓ Set float environment variable")
            
            canoe.set_environment_variable_value("string_var", "Hello from Python")
            print("✓ Set string environment variable")
            
            canoe.set_environment_variable_value("data_var", (1, 2, 3, 4, 5))
            print("✓ Set data environment variable")
        except MyCANoeException as e:
            print(f"✗ Environment variable operation failed: {e}")
            print("  This may be due to missing environment variables in your configuration")
        
        # === System Variables ===
        print("\n--- System Variables ---")
        
        # Example system variable - update with valid values for your configuration
        sys_var_name = "sys_var_demo::speed"
        
        try:
            # Set system variable
            sys_var_value = 50
            canoe.set_system_variable_value(sys_var_name, sys_var_value)
            print(f"✓ Set system variable {sys_var_name} to {sys_var_value}")
            
            # Get system variable
            retrieved_sys_var_value = canoe.get_system_variable_value(sys_var_name)
            print(f"✓ Retrieved system variable {sys_var_name}: {retrieved_sys_var_value}")
            
            # Set system variable array
            array_var_name = "sys_var_demo::int_array_var"
            array_values = (10, 20, 30, 40, 50)
            canoe.set_system_variable_array_values(array_var_name, array_values)
            print(f"✓ Set system variable array {array_var_name} to {array_values}")
            
            # Get system variable array
            retrieved_array = canoe.get_system_variable_value(array_var_name)
            print(f"✓ Retrieved system variable array {array_var_name}: {retrieved_array}")
        except MyCANoeException as e:
            print(f"✗ System variable operation failed: {e}")
            print("  This may be due to missing system variables in your configuration")
        
        # === CAPL Functions ===
        print("\n--- CAPL Functions ---")
        
        try:
            # Compile all CAPL nodes
            compile_result = canoe.compile_all_capl_nodes()
            print(f"✓ Compilation result: {compile_result}")
            
            # Call CAPL function with parameters
            canoe.call_capl_function("addition_function", 10, 20)
            print("✓ Called CAPL function 'addition_function' with parameters 10, 20")
            
            # Call CAPL function without parameters
            canoe.call_capl_function("hello_world")
            print("✓ Called CAPL function 'hello_world' without parameters")
        except MyCANoeException as e:
            print(f"✗ CAPL function operation failed: {e}")
            print("  This may be due to missing CAPL functions in your configuration")
        
        # === Database Management ===
        print("\n--- Database Management ---")
        
        # Example database path - update with a valid path for your system
        db_path = os.path.abspath("../tests/demo_cfg/Databases/demo.dbc")
        
        try:
            # Add database
            canoe.add_database(db_path)
            print(f"✓ Added database: {db_path}")
            
            # Remove database
            canoe.remove_database(db_path)
            print(f"✓ Removed database: {db_path}")
        except MyCANoeException as e:
            print(f"✗ Database operation failed: {e}")
            print("  This may be due to an invalid database path")
        
        # Stop measurement before quitting
        canoe.stop_measurement()
        print("✓ Stopped measurement before quitting")
        
        # Quit CANoe
        canoe.quit()
        print("✓ Quit CANoe")
        
        print("\n=== Example Complete ===")
        return 0
        
    except MyCANoeException as e:
        print(f"\n✗ MyCANoe Error: {str(e)}")
        return 1
    except Exception as e:
        print(f"\n✗ Unexpected error: {str(e)}")
        return 1

if __name__ == "__main__":
    sys.exit(main())