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
Untitled configuration

Customs: # List of custom propositions
v1
v2
v3
v4

RegionFile: # Relative path of region description file
memory.1.regions

Sensors: # List of sensor propositions and their state (enabled = 1, disabled = 0)


======== SPECIFICATION ========

RegionMapping: # Mapping between region names and their decomposed counterparts
1 = p4
3 = p2
2 = p3
4 = p1
others = 

Spec: # Specification in structured English
if not v1 then visit 1
if not v2 then visit 2
if not v3 then visit 3
if not v4 then visit 4

v1 is set on 1 and reset on false
v2 is set on 2 and reset on false
v3 is set on 3 and reset on false
v4 is set on 4 and reset on false

