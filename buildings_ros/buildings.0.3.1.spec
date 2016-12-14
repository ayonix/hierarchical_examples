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
0.3.1

Customs: # List of custom propositions

RegionFile: # Relative path of region description file
buildings.0.3.1.regions

Sensors: # List of sensor propositions and their state (enabled = 1, disabled = 0)


======== SPECIFICATION ========

RegionMapping: # Mapping between region names and their decomposed counterparts
1 = p3
others = 
exit_1_3_1 = p2
exit_1_3_2 = p1

Spec: # Specification in structured English
go to exit_1_3_2

