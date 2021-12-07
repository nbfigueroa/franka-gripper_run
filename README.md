# franka_gripper_run

Installation:

1. Clone repo
2. Compile
```bash
mkdir build
cd build
cmake -DCMAKE_BUILD_TYPE=Release ..
cmake --build .
```

**Usage (from terminal):** 

To open gripper:

```bash
./build/franka_gripper_run 1
```

To close gripper:

```bash
./build/franka_gripper_run 0
```

**Usage from ROS:**

Either you write a node that wraps these commands (i.e. add it to franka_ros) or you could call this line from a python script as follows:

```python
import subprocess 
proc = subprocess.Popen(["/home/panda2/franka_gripper_run/gripper_run", "1"])
```
