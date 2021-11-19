# franka_gripper_run

Installation:

1. Download this file and place it in: ``./libfranka/examples``  
2. Add the name of this file to ``./libfranka/examples/CMakeLists.txt``
3. Compile libfranka 
```bash
cd build
cmake -DCMAKE_BUILD_TYPE=Release ..
cmake --build .
```

**Usage (from terminal):** 

To open gripper:

```bash
./examples/gripper_run  172.16.0.2 1
```

To close gripper:

```bash
./examples/gripper_run  172.16.0.2 0
```


**Usage from ROS:**

Either you write a node that wraps these commands (i.e. add it to franka_ros) or you could call this line from a python script as follows:

```python
proc = subprocess.Popen(["/home/thavishi/code/libfranka/build/examples/gripper_run", "172.16.0.2", "1"])
```
