# This is a specification definition file for the LTLMoP toolkit.
# Format details are described at the beginning of each section below.


======== SETTINGS ========

Actions: # List of action propositions and their state (enabled = 1, disabled = 0)

CompileOptions:
convexify: True
parser: structured
symbolic: False
use_region_bit_encoding: True
synthesizer: jtlv
fastslow: False
decompose: True

CurrentConfigName:
lowlevel

Customs: # List of custom propositions

RegionFile: # Relative path of region description file
memory.0.1.regions

Sensors: # List of sensor propositions and their state (enabled = 1, disabled = 0)


======== SPECIFICATION ========

RegionMapping: # Mapping between region names and their decomposed counterparts
exit_0_1_4 = p1
exit_0_1_2 = p3
exit_0_1_3 = p2
1 = p6
3 = p4
2 = p5
others = 

Spec: # Specification in structured English
go to exit_0_1_2

always not exit_0_1_3

