cmake_minimum_required(VERSION 3.22.1 FATAL_ERROR)

project(PIDExecute)

# Find the Gazebo Transport library
find_package(gz-transport14 QUIET REQUIRED OPTIONAL_COMPONENTS log)
find_package(gz-math7 REQUIRED)

set(GZ_TRANSPORT_VER ${gz-transport14_VERSION_MAJOR})

include_directories(${CMAKE_BINARY_DIR})


if (EXISTS "${CMAKE_SOURCE_DIR}/PIDControl.cc")
  add_executable(PIDControl PIDControl.cc)
  target_link_libraries(PIDControl
    gz-math7::gz-math7
    gz-transport${GZ_TRANSPORT_VER}::core
  )
endif()


if (MSVC)
  # Suppress Protobuf message generation warnings.
  set (CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} /wd4018 /wd4100 /wd4127 /wd4244 /wd4267 /wd4512")

  # Suppress the "decorated name length exceed" warning (inside the STL).
  set (CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} /wd4503")

  add_definitions(-DBUILDING_STATIC_LIBS -DWIN32_LEAN_AND_MEAN)

  # Don't pull in the Windows min/max macros
  add_definitions(-DNOMINMAX)

endif()
