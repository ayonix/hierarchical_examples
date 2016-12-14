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
buildings.1.1

Customs: # List of custom propositions
d1
d3
d2

RegionFile: # Relative path of region description file
buildings.1.1.regions

Sensors: # List of sensor propositions and their state (enabled = 1, disabled = 0)


======== SPECIFICATION ========

RegionMapping: # Mapping between region names and their decomposed counterparts
1 = p5
3 = p3
2 = p4
exit_1_1_3 = p2
others = 

Spec: # Specification in structured English
if not d1 then visit 1
if not d2 then visit 2
if not d3 then visit 3

d1 is set on 1 and reset on exit_1_1_3
d2 is set on 2 and reset on exit_1_1_3
d3 is set on 3 and reset on exit_1_1_3

go to exit_1_1_3

