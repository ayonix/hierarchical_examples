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
24 = p7
11 = p14
13 = p12
12 = p13
14 = p11
22 = p9
23 = p8
33 = p4
32 = p5
31 = p6
exit_0_1_2 = p2
exit_0_1_3 = p1
34 = p3
others = 
21 = p10

Spec: # Specification in structured English
go to exit_0_1_2

always not exit_0_1_2

