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
0.1.1

Customs: # List of custom propositions

RegionFile: # Relative path of region description file
buildings.0.1.1.regions

Sensors: # List of sensor propositions and their state (enabled = 1, disabled = 0)


======== SPECIFICATION ========

RegionMapping: # Mapping between region names and their decomposed counterparts
24 = p9
11 = p16
13 = p14
12 = p15
14 = p13
22 = p11
23 = p10
33 = p6
32 = p7
31 = p8
exit_0_1_3 = p2
exit_0_1_2#1 = p4
exit_0_1_2#2 = p3
others = 
exit_1_1_3 = p1
34 = p5
21 = p12

Spec: # Specification in structured English
go to exit_0_1_2#1

