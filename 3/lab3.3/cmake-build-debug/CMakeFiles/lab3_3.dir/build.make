# CMAKE generated file: DO NOT EDIT!
# Generated by "MinGW Makefiles" Generator, CMake Version 3.17

# Delete rule output on recipe failure.
.DELETE_ON_ERROR:


#=============================================================================
# Special targets provided by cmake.

# Disable implicit rules so canonical targets will work.
.SUFFIXES:


# Disable VCS-based implicit rules.
% : %,v


# Disable VCS-based implicit rules.
% : RCS/%


# Disable VCS-based implicit rules.
% : RCS/%,v


# Disable VCS-based implicit rules.
% : SCCS/s.%


# Disable VCS-based implicit rules.
% : s.%


.SUFFIXES: .hpux_make_needs_suffix_list


# Command-line flag to silence nested $(MAKE).
$(VERBOSE)MAKESILENT = -s

# Suppress display of executed commands.
$(VERBOSE).SILENT:


# A target that is always out of date.
cmake_force:

.PHONY : cmake_force

#=============================================================================
# Set environment variables for the build.

SHELL = cmd.exe

# The CMake executable.
CMAKE_COMMAND = "C:\Program Files\JetBrains\CLion 2020.2.1\bin\cmake\win\bin\cmake.exe"

# The command to remove a file.
RM = "C:\Program Files\JetBrains\CLion 2020.2.1\bin\cmake\win\bin\cmake.exe" -E rm -f

# Escaping for special characters.
EQUALS = =

# The top-level source directory on which CMake was run.
CMAKE_SOURCE_DIR = C:\Users\Artem\Desktop\Univ\Algorythms\Labs\3\lab3.3

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = C:\Users\Artem\Desktop\Univ\Algorythms\Labs\3\lab3.3\cmake-build-debug

# Include any dependencies generated for this target.
include CMakeFiles/lab3_3.dir/depend.make

# Include the progress variables for this target.
include CMakeFiles/lab3_3.dir/progress.make

# Include the compile flags for this target's objects.
include CMakeFiles/lab3_3.dir/flags.make

CMakeFiles/lab3_3.dir/main.cpp.obj: CMakeFiles/lab3_3.dir/flags.make
CMakeFiles/lab3_3.dir/main.cpp.obj: ../main.cpp
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=C:\Users\Artem\Desktop\Univ\Algorythms\Labs\3\lab3.3\cmake-build-debug\CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Building CXX object CMakeFiles/lab3_3.dir/main.cpp.obj"
	C:\PROGRA~1\MINGW-~1\X86_64~1.0-P\mingw64\bin\G__~1.EXE  $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -o CMakeFiles\lab3_3.dir\main.cpp.obj -c C:\Users\Artem\Desktop\Univ\Algorythms\Labs\3\lab3.3\main.cpp

CMakeFiles/lab3_3.dir/main.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/lab3_3.dir/main.cpp.i"
	C:\PROGRA~1\MINGW-~1\X86_64~1.0-P\mingw64\bin\G__~1.EXE $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E C:\Users\Artem\Desktop\Univ\Algorythms\Labs\3\lab3.3\main.cpp > CMakeFiles\lab3_3.dir\main.cpp.i

CMakeFiles/lab3_3.dir/main.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/lab3_3.dir/main.cpp.s"
	C:\PROGRA~1\MINGW-~1\X86_64~1.0-P\mingw64\bin\G__~1.EXE $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S C:\Users\Artem\Desktop\Univ\Algorythms\Labs\3\lab3.3\main.cpp -o CMakeFiles\lab3_3.dir\main.cpp.s

# Object files for target lab3_3
lab3_3_OBJECTS = \
"CMakeFiles/lab3_3.dir/main.cpp.obj"

# External object files for target lab3_3
lab3_3_EXTERNAL_OBJECTS =

lab3_3.exe: CMakeFiles/lab3_3.dir/main.cpp.obj
lab3_3.exe: CMakeFiles/lab3_3.dir/build.make
lab3_3.exe: CMakeFiles/lab3_3.dir/linklibs.rsp
lab3_3.exe: CMakeFiles/lab3_3.dir/objects1.rsp
lab3_3.exe: CMakeFiles/lab3_3.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --bold --progress-dir=C:\Users\Artem\Desktop\Univ\Algorythms\Labs\3\lab3.3\cmake-build-debug\CMakeFiles --progress-num=$(CMAKE_PROGRESS_2) "Linking CXX executable lab3_3.exe"
	$(CMAKE_COMMAND) -E cmake_link_script CMakeFiles\lab3_3.dir\link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
CMakeFiles/lab3_3.dir/build: lab3_3.exe

.PHONY : CMakeFiles/lab3_3.dir/build

CMakeFiles/lab3_3.dir/clean:
	$(CMAKE_COMMAND) -P CMakeFiles\lab3_3.dir\cmake_clean.cmake
.PHONY : CMakeFiles/lab3_3.dir/clean

CMakeFiles/lab3_3.dir/depend:
	$(CMAKE_COMMAND) -E cmake_depends "MinGW Makefiles" C:\Users\Artem\Desktop\Univ\Algorythms\Labs\3\lab3.3 C:\Users\Artem\Desktop\Univ\Algorythms\Labs\3\lab3.3 C:\Users\Artem\Desktop\Univ\Algorythms\Labs\3\lab3.3\cmake-build-debug C:\Users\Artem\Desktop\Univ\Algorythms\Labs\3\lab3.3\cmake-build-debug C:\Users\Artem\Desktop\Univ\Algorythms\Labs\3\lab3.3\cmake-build-debug\CMakeFiles\lab3_3.dir\DependInfo.cmake --color=$(COLOR)
.PHONY : CMakeFiles/lab3_3.dir/depend

