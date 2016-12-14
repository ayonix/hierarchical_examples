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
0.2.1

Customs: # List of custom propositions

RegionFile: # Relative path of region description file
buildings.0.2.1.regions

Sensors: # List of sensor propositions and their state (enabled = 1, disabled = 0)


======== SPECIFICATION ========

RegionMapping: # Mapping between region names and their decomposed counterparts
24 = p6
11 = p13
13 = p11
12 = p12
21 = p9
22 = p8
23 = p7
33 = p3
32 = p4
31 = p5
exit_0_1_2 = p1
34 = p2
others = 
14 = p10

Spec: # Specification in structured English
visit 31
go to exit_0_1_2

