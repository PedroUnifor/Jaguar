# Install script for directory: /home/pedro/catkin_ws/src/drrobotV2_player-master

# Set the install prefix
if(NOT DEFINED CMAKE_INSTALL_PREFIX)
  set(CMAKE_INSTALL_PREFIX "/home/pedro/catkin_ws/install")
endif()
string(REGEX REPLACE "/$" "" CMAKE_INSTALL_PREFIX "${CMAKE_INSTALL_PREFIX}")

# Set the install configuration name.
if(NOT DEFINED CMAKE_INSTALL_CONFIG_NAME)
  if(BUILD_TYPE)
    string(REGEX REPLACE "^[^A-Za-z0-9_]+" ""
           CMAKE_INSTALL_CONFIG_NAME "${BUILD_TYPE}")
  else()
    set(CMAKE_INSTALL_CONFIG_NAME "")
  endif()
  message(STATUS "Install configuration: \"${CMAKE_INSTALL_CONFIG_NAME}\"")
endif()

# Set the component getting installed.
if(NOT CMAKE_INSTALL_COMPONENT)
  if(COMPONENT)
    message(STATUS "Install component: \"${COMPONENT}\"")
    set(CMAKE_INSTALL_COMPONENT "${COMPONENT}")
  else()
    set(CMAKE_INSTALL_COMPONENT)
  endif()
endif()

# Install shared libraries without execute permission?
if(NOT DEFINED CMAKE_INSTALL_SO_NO_EXE)
  set(CMAKE_INSTALL_SO_NO_EXE "1")
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/drrobot_jaguarV2_player/msg" TYPE FILE FILES
    "/home/pedro/catkin_ws/src/drrobotV2_player-master/msg/CustomSensor.msg"
    "/home/pedro/catkin_ws/src/drrobotV2_player-master/msg/IMUInfo.msg"
    "/home/pedro/catkin_ws/src/drrobotV2_player-master/msg/MotorInfo.msg"
    "/home/pedro/catkin_ws/src/drrobotV2_player-master/msg/MotorInfoArray.msg"
    "/home/pedro/catkin_ws/src/drrobotV2_player-master/msg/PowerInfo.msg"
    "/home/pedro/catkin_ws/src/drrobotV2_player-master/msg/Range.msg"
    "/home/pedro/catkin_ws/src/drrobotV2_player-master/msg/RangeArray.msg"
    "/home/pedro/catkin_ws/src/drrobotV2_player-master/msg/StandardSensor.msg"
    )
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/drrobot_jaguarV2_player/cmake" TYPE FILE FILES "/home/pedro/catkin_ws/build/drrobotV2_player-master/catkin_generated/installspace/drrobot_jaguarV2_player-msg-paths.cmake")
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/include" TYPE DIRECTORY FILES "/home/pedro/catkin_ws/devel/include/drrobot_jaguarV2_player")
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/roseus/ros" TYPE DIRECTORY FILES "/home/pedro/catkin_ws/devel/share/roseus/ros/drrobot_jaguarV2_player")
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/common-lisp/ros" TYPE DIRECTORY FILES "/home/pedro/catkin_ws/devel/share/common-lisp/ros/drrobot_jaguarV2_player")
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/gennodejs/ros" TYPE DIRECTORY FILES "/home/pedro/catkin_ws/devel/share/gennodejs/ros/drrobot_jaguarV2_player")
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  execute_process(COMMAND "/usr/bin/python" -m compileall "/home/pedro/catkin_ws/devel/lib/python2.7/dist-packages/drrobot_jaguarV2_player")
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/python2.7/dist-packages" TYPE DIRECTORY FILES "/home/pedro/catkin_ws/devel/lib/python2.7/dist-packages/drrobot_jaguarV2_player")
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/pkgconfig" TYPE FILE FILES "/home/pedro/catkin_ws/build/drrobotV2_player-master/catkin_generated/installspace/drrobot_jaguarV2_player.pc")
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/drrobot_jaguarV2_player/cmake" TYPE FILE FILES "/home/pedro/catkin_ws/build/drrobotV2_player-master/catkin_generated/installspace/drrobot_jaguarV2_player-msg-extras.cmake")
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/drrobot_jaguarV2_player/cmake" TYPE FILE FILES
    "/home/pedro/catkin_ws/build/drrobotV2_player-master/catkin_generated/installspace/drrobot_jaguarV2_playerConfig.cmake"
    "/home/pedro/catkin_ws/build/drrobotV2_player-master/catkin_generated/installspace/drrobot_jaguarV2_playerConfig-version.cmake"
    )
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/drrobot_jaguarV2_player" TYPE FILE FILES "/home/pedro/catkin_ws/src/drrobotV2_player-master/package.xml")
endif()

