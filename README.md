# Installation
If you want to use ROS consider using Ubuntu (16.04 for example, to use with ROS Kinetic Kame)
  
## LTLMoP
To get the code, clone the repository and change to the branch `hier_ros`:
`git clone https://github.com/ayonix/ltlmop -b hier_ros`

Then, install according to
https://github.com/VerifiableRobotics/LTLMoP/wiki/Installation-Guide, the
packages here are names of Ubuntu, but the guide handles other OS as well:

- java (GROne/jtlv)
  - `default-jdk`
  - `default-jre`
- Python (2.7.x?)
  - numpy/scipy (matrix operations and computations)
  - `python-numpy`
  - `python-scipy`
- Polygon (for regions)
  - `python-polygon2` (not sure, maybe have to do it via `pip install Polygon2`, might need `python-pip`)
- wxPython (GUI)
  - `python-wxtools`

## ROS
I've used ROS Kinetic Kame (http://wiki.ros.org/kinetic/Installation/Ubuntu)
with the `ros-kinetic-desktop` metapackage. Additionally some specific
packages were installed (some might still be missing). Generally turtlebot,
gazebo and rviz packages have to be installed.

- `ros-kinetic-turtlebot`
- `ros-kinetic-turtlebot-simulator`
- `ros-kinetic-turtlebot-gazebo`
- `ros-kinetic-gazebo-ros`

# Usage
## Without ROS
Create a scenario or take an example from
https://github.com/ayonix/hierarchical_examples. To use LTLMoP (to edit or
create scenarios), go to the src folder in LTLMoP and use `python
specEditor.py`, with the path to a scenario as an optional argument. In
order to run the scenario, give hierarchical.py the path to the top level of
the scenario: `python hierarchical.py /path/to/top_level.spec`.

## With ROS
We assume the user starts Gazebo and ROS, for our examples a launch file
that starts the needed ROS nodes is included: 
`roslaunch name.launch world_file:=path/to/world.world map_file:=path/to/map_file.yaml custom_param_file:=path/to/params.yaml`

Additionally, before LTLMoP is
started, `Gazebo` has to be launched and optionally the Rviz visualization for
the navigation via `roslaunch turtlebot_rviz_launchers
view_navigation.launch`.

Then, the scenario can be started, again with `python hierarchical.py path/to/top_level.spec`
