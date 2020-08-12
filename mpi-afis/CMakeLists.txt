cmake_minimum_required(VERSION 3.7)
project(mpi-afis)

set(CMAKE_CXX_STANDARD 11)

find_package(MPI REQUIRED)
set(IDIR include)
set(CDIR commons)
set(JIANGDIR MatcherJiang)
set(MCCDIR MCC)
set(PDIR Parallel)

set(CMAKE_CXX_FLAGS "-Wall -O2 -fopenmp")
include_directories(${MPI_INCLUDE_PATH} ${IDIR} ${JIANGDIR} ${MCCDIR})
add_definitions(-D COMPILE_USING_MPI)


SET(CMAKE_CXX_COMPILER mpicxx)
SET(CMAKE_C_COMPILER  mpicc)


set(SOURCE_FILES
        Parallel/IOHandler.cpp
        Parallel/ParallelHandler.cpp
        Parallel/ParallelMaster.cpp
        Parallel/ParallelSlave.cpp
        MCC/Cylinder.cpp
        MCC/MCC.cpp
        MatcherJiang/FingerprintJiang.cpp
        commons/File19794.cpp
        commons/Fingerprint.cpp
        commons/Functions.cpp
        commons/GrahamScanConvexHull.cpp
        commons/Minutia.cpp
        commons/Munkres.cpp
        commons/Score.cpp
        )
add_executable(genericMatching ${SOURCE_FILES} Parallel/genericMatching.cpp)
add_executable(DPDDFF ${SOURCE_FILES} Parallel/DPDDFF.cpp)