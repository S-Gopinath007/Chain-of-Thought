import os

def setup_sandbox():
    print("Generating local workspace directory and mock log target")

    mock_logs = (
        "INFO: System initialized\n"
        "DEBUG: Port listening\n"
        "CRITICAL: Database connection lost\n"
        "INFO: Attempting reconnect\n"
        "FATAL: Memory corruption at segment 0x4F\n"
    )

    with open("mock_data.log", "w") as f:
        f.write(mock_logs)

    print("Mock environments configured locally at `mock_data.log`.")
