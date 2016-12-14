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
memory.0.4.regions

Sensors: # List of sensor propositions and their state (enabled = 1, disabled = 0)


======== SPECIFICATION ========

RegionMapping: # Mapping between region names and their decomposed counterparts
exit_0_4_3 = p1
exit_0_4_2 = p2
13 = p9
12 = p10
21 = p8
22 = p7
23 = p6
33 = p3
32 = p4
31 = p5
others = 
11 = p11

Spec: # Specification in structured English
always not exit_0_4_2
go to exit_0_4_2

