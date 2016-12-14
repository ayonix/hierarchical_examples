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
0.1.3

Customs: # List of custom propositions

RegionFile: # Relative path of region description file
buildings.0.1.3.regions

Sensors: # List of sensor propositions and their state (enabled = 1, disabled = 0)


======== SPECIFICATION ========

RegionMapping: # Mapping between region names and their decomposed counterparts
11 = p16
13 = p14
12 = p15
21 = p13
22 = p11, p12, p19, p20
23 = p9
33 = p11, p17, p18
32 = p6, p12
31 = p7, p8
42 = p3
43 = p2
41 = p4, p8
others = 
exit_0_3_1 = p1

Spec: # Specification in structured English
visit 43
go to exit_0_3_1

