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

Usage: 

To open gripper:

```bash
./examples/gripper_run  172.16.0.2 1
```

To close gripper:

```bash
./examples/gripper_run  172.16.0.2 0
```
