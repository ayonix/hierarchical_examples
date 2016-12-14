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
buildings.0.1.2

Customs: # List of custom propositions

RegionFile: # Relative path of region description file
buildings.0.1.2.regions

Sensors: # List of sensor propositions and their state (enabled = 1, disabled = 0)


======== SPECIFICATION ========

RegionMapping: # Mapping between region names and their decomposed counterparts
11 = p10, p11
13 = p8
12 = p9, p11
21 = p7
22 = p6
23 = p5
33 = p2
32 = p3
31 = p4
exit_0_2_1 = p1
others = 

Spec: # Specification in structured English
go to exit_0_2_1

