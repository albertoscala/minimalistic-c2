# Minimalistic C2
[![License](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)

## Overview
Minimalistic C2 is a straightforward Command and Control (C2) server and beacon designed with simplicity and educational purposes in mind. 
Stripped down to essential functionalities, this minimalistic C2 server provides a clear understanding of the core concepts involved in C2 operations without unnecessary complexity. It serves as an ideal starting point for those looking to explore and learn about command and control systems in a controlled and simplified environment.

## Features

- **Python C2 Server:**
    - **Centralized Management:**
        - Effectively manage and control multiple Go-based beacon from a centralized Python C&C server.
    - **Web-based GUI:**
        - Web-based graphical user interface (GUI) for seamless and user-friendly control of the C&C server.
- **Go beacon:**
    - **Lightweight Beacon:**
        - Deploy a lightweight and efficient beacon written in Go for covert and stealthy communication.
    - **Autonomous Functionality:**
        - Enable autonomous functionality in the Go beacon for discrete operations without compromising the system.

## Prerequisites

- Python 3.x
- Go 1.x

## Setup

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/albertoscala/Minimalistic-C2.git
   cd Minimalistic-C2
   ```
2. **Install Dependencies:**
   ```bash
   # Python dependencies
   pip install -r requirements.txt
   ```

## Usage

1. **Run the startup script:**
    ```bash
    ./startup.ps1
    ```

2. **Compile and Run the Beacon:**
    ```bash
    go build target.go
    ./target
    ```

## Contributing

Feel free to contribute by opening issues or submitting pull requests.

## License

[MIT](https://choosealicense.com/licenses/mit/)