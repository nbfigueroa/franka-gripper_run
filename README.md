# franka_gripper_run
Standalone non-ROS C++ executable to open/close gripper.


**Installation**

1. Clone repo
2. Compile
```bash
cd ~/franka_gripper_run/
mkdir build
cd build
cmake -DCMAKE_BUILD_TYPE=Release ..
cmake --build .
```

**Usage (from terminal)** 

To open gripper:

```bash
cd ~/franka_gripper_run/
./build/franka_gripper_run 1
```

To close gripper:

```bash
cd ~/franka_gripper_run/
./build/franka_gripper_run 0
```

**Usage from PYTHON**
You could call this line from a python script as follows:

```python
import subprocess 
proc = subprocess.Popen(["/home/panda2/franka_gripper_run/build/franka_gripper_run", "1"])
```

**Usage from PYTHON-GUI**
In the ``./python_gui`` folder there is a simple GUI that enables open/close the gripper by pressing a button, as follows:

 <p align="center"><img src="https://github.com/nbfigueroa/franka_gripper_run/blob/main/img/gripper_gui.png" width="500"></>
  <p align="center">
  <img src="https://github.com/nbfigueroa/franka_gripper_run/blob/main/img/gripper_gui_close.png" width="250"><img src="https://github.com/nbfigueroa/franka_gripper_run/blob/main/img/gripper_gui_open.png" width="250"></>

Run:
```bash
cd ~/franka_gripper_run/
python3 python_gui/gui_gripper_run.py
```

**Usage from ROS**  
Write a node that wraps these commands (i.e. add it to [franka_interactive_controllers](https://github.com/nbfigueroa/franka_interactive_controllers) == TODO NEXT). 
