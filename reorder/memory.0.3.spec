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
memory.0.3.regions

Sensors: # List of sensor propositions and their state (enabled = 1, disabled = 0)


======== SPECIFICATION ========

RegionMapping: # Mapping between region names and their decomposed counterparts
11 = p11
13 = p9
12 = p10
21 = p8
22 = p7
23 = p6
33 = p3
32 = p4
31 = p5
others = 
exit_0_3_1 = p2
exit_0_3_4 = p1

Spec: # Specification in structured English
go to exit_0_3_4

