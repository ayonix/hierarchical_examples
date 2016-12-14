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
buildings.0.2.2

Customs: # List of custom propositions

RegionFile: # Relative path of region description file
buildings.0.2.2.regions

Sensors: # List of sensor propositions and their state (enabled = 1, disabled = 0)


======== SPECIFICATION ========

RegionMapping: # Mapping between region names and their decomposed counterparts
11 = p12
13 = p10
12 = p11
21 = p9
22 = p8
23 = p7
33 = p4
32 = p5
31 = p6
exit_0_2_1 = p3
exit_0_2_3 = p2
others = 
exit_1_2_3 = p1

Spec: # Specification in structured English
go to 31

