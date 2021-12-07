# franka_gripper_run
Standalone non-ROS C++ executable to open/close gripper.


**Installation**

1. Clone repo
2. Compile
```bash
mkdir build
cd build
cmake -DCMAKE_BUILD_TYPE=Release ..
cmake --build .
```

**Usage (from terminal)** 

To open gripper:

```bash
./build/franka_gripper_run 1
```

To close gripper:

```bash
./build/franka_gripper_run 0
```

**Usage from PYTHON**
You could call this line from a python script as follows:

```python
import subprocess 
proc = subprocess.Popen(["/home/panda2/franka_gripper_run/build/franka_gripper_run", "1"])
```

**Usage from ROS**  
Write a node that wraps these commands (i.e. add it to [franka_interactive_controllers](https://github.com/nbfigueroa/franka_interactive_controllers) == TODO NEXT). 
