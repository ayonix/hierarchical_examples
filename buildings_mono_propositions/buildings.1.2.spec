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
buildings.1.2

Customs: # List of custom propositions

RegionFile: # Relative path of region description file
buildings.1.2.regions

Sensors: # List of sensor propositions and their state (enabled = 1, disabled = 0)


======== SPECIFICATION ========

RegionMapping: # Mapping between region names and their decomposed counterparts
1 = p5
3 = p3
2 = p4
exit_1_2_3 = p2
others = 

Spec: # Specification in structured English
visit 1
visit 2
visit 3

go to exit_1_2_3

