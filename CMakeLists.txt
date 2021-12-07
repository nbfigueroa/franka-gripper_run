cmake_minimum_required(VERSION 3.4)

project(franka-gripper-run CXX)

list(INSERT CMAKE_MODULE_PATH 0 ${CMAKE_CURRENT_LIST_DIR}/cmake)

set(CMAKE_CXX_STANDARD 14)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

find_package(Franka REQUIRED)
find_package(Eigen3 REQUIRED)

set(CONTROLLERS
  franka_gripper_run
)

foreach(controller_example ${CONTROLLERS})
  add_executable(${controller_example} ./src/${controller_example}.cpp)
    target_link_libraries(${controller_example} Franka::Franka Eigen3::Eigen3)
endforeach()


include(GNUInstallDirs)
install(TARGETS ${CONTROLLERS}
  LIBRARY DESTINATION ${CMAKE_INSTALL_LIBDIR}
  RUNTIME DESTINATION ${CMAKE_INSTALL_BINDIR}
)
