if (WIN32)
  add_definitions(-D__BUILD_GADGETRON_NFFT__)
  add_definitions(-D_USE_MATH_DEFINES)
endif ()

if(WIN32)
  link_directories(${Boost_LIBRARY_DIRS})
endif()

include_directories( 
    ${CMAKE_SOURCE_DIR}/toolboxes/core
    ${CMAKE_SOURCE_DIR}/toolboxes/nfft
    ${CMAKE_SOURCE_DIR}/toolboxes/nfft/cpu
    ${CMAKE_BINARY_DIR}/toolboxes/core
    ${CMAKE_SOURCE_DIR}/toolboxes/core/cpu
    ${CMAKE_SOURCE_DIR}/toolboxes/core/cpu/math
    ${CMAKE_SOURCE_DIR}/toolboxes/core/cpu/hostutils
    ${CMAKE_SOURCE_DIR}/toolboxes/fft/cpu
    ${CMAKE_SOURCE_DIR}/toolboxes/operators
    ${Boost_INCLUDE_DIR}
    ${FFTW3_INCLUDE_DIR}
    ${ARMADILLO_INCLUDE_DIRS}
  )

add_library(gadgetron_toolbox_cpunfft SHARED 
    hoNFFT.h
    ../nfft_export.h
    ../NFFT.h
    ../NFFTOperator.h
    ../NFFTOperator.hpp
    ../NFFT.hpp
    ../KaiserBessel_kernel.h
    hoNFFT.cpp
    hoNFFT_sparseMatrix.cpp 
    hoNFFT_sparseMatrix.h 
    hoNFFTOperator.cpp)

set_target_properties(gadgetron_toolbox_cpunfft PROPERTIES VERSION ${GADGETRON_VERSION_STRING} SOVERSION ${GADGETRON_SOVERSION})

target_link_libraries(gadgetron_toolbox_cpunfft 
    gadgetron_toolbox_cpufft
    gadgetron_toolbox_cpucore
    gadgetron_toolbox_log
    gadgetron_toolbox_hostutils
  )

install(TARGETS gadgetron_toolbox_cpunfft DESTINATION lib COMPONENT main)

install(FILES 
    hoNFFT.h      
    DESTINATION ${GADGETRON_INSTALL_INCLUDE_PATH} COMPONENT main)
