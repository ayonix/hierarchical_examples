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
buildings.0.2.3

Customs: # List of custom propositions

RegionFile: # Relative path of region description file
buildings.0.2.3.regions

Sensors: # List of sensor propositions and their state (enabled = 1, disabled = 0)


======== SPECIFICATION ========

RegionMapping: # Mapping between region names and their decomposed counterparts
11 = p13
12 = p12
21 = p11
22 = p10
51 = p5
31 = p9
others = 
42 = p6
52 = p4
61 = p3
62 = p2
32 = p8
exit_0_3_2 = p1
41 = p7

Spec: # Specification in structured English
go to exit_0_3_2

