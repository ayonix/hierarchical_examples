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
decompose: False

CurrentConfigName:
buildings.0.1.1

Customs: # List of custom propositions

RegionFile: # Relative path of region description file
buildings.0.1.1.regions

Sensors: # List of sensor propositions and their state (enabled = 1, disabled = 0)
sensor1, 1
sensor2, 1
sensor3, 1
sensor4, 1
sensor5, 1


======== SPECIFICATION ========

RegionMapping: # Mapping between region names and their decomposed counterparts
24 = p8
11 = p15
13 = p13
12 = p14
14 = p12
22 = p10
23 = p9
33 = p5
32 = p6
31 = p7
34 = p4
exit_0_1_2 = p3
exit_0_1_3 = p2
others = 
exit_1_1_3 = p1
21 = p11

Spec: # Specification in structured English
if not sensor1 then visit 11
if not sensor2 then visit 12
if not sensor3 then visit 13
if not sensor4 then visit 23
if not sensor5 then visit 33
visit 32

go to exit_0_1_2

