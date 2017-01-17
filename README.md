# Installation
If you want to use ROS consider using Ubuntu (16.04 for example, to use with ROS Kinetic Kame).
We have used ROS Kinetic Kame, because it supports the Gazebo simulator in version 7, which has a building editor included.

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
  
Once this is done LTLMoP has to be set up by running `python dist/setup.py` in
the LTLMoP project, which will for example compile the java used by LTLMoP to check realizability of the specification.

A general guide to how LTLMoP can be used for a scenario can be found [in their wiki](https://github.com/VerifiableRobotics/LTLMoP/wiki/Tutorial).

## ROS
I've used ROS Kinetic Kame (http://wiki.ros.org/kinetic/Installation/Ubuntu)
with the `ros-kinetic-desktop` metapackage. Additionally some specific
packages were installed (some might still be missing). Generally turtlebot,
gazebo and rviz packages have to be installed.

- `ros-kinetic-turtlebot`
- `ros-kinetic-turtlebot-simulator`
- `ros-kinetic-turtlebot-gazebo`
- `ros-kinetic-turtlebot-navigation`
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

# Conventions
- File names: `basename.hierarchy_level.path_of_game.extension`, joined by
  periods, example: `example.0.3.2.spec`, in order to find the specification
  files. The basename should not contain contain any period.
- Goals: Use `go to` for goals, `visit` for temporary goals, both get translated to
    `globally eventually goal`, used to differentiate between the goals by another
    level and goals of the current level
- Exits to other games: named `exit_level_from_to#identifier`, `#identifier` is optional if
  there is only one exit between regions `from` and `to`
- Regions: regions should not contain any characters but alphanumerical and
  underscores, since other characters can lead to problems if decomposing is
  turned off

# Specifics
## mappings.json
As an example for the file:
```json
{
    "1": {
        "1": {
            "1.1_3": "1.11"
        },
        "0": {
            "1.1_3": "11",
            "0.1_2": "12",
            "0.1_3": "12",
            "0.3_1": "34",
            "0.2_1": "32"
        }
    },
    "2": {
    }
}
```
The mapping is used when the border to an exit is reached. Since exits have the
names `exit_level_from_to`, we can use that information to find out where the
exit is heading. To do so we use either the region or our id, depending on if we
are on the highest level or not, which decides the first nesting level of the
file. The next nesting level is decided by abstraction level of the layer below:
`level - 1`.

Finally, the key on the lowest level is the level the layer corresponds to
concatenated with a period and the regions `from_to`. The value of the pair then
is the id of the region with respect to its layer. So `1.11` in the first group
means the initial region will be `11` in region `1`, therefore we need to use
`1.11` as value. The additional information is not needed on the lowest level,
which can be seen in the next group, where the region of the lowest level is
used directly.

The code where it is used can be found [here](https://github.com/ayonix/LTLMoP/blob/hier_ros/src/lib/handlers/share/MotionControl/AbstractHandler.py#L162).
