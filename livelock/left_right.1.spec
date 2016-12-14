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
highlevel

Customs: # List of custom propositions
vleft
vright

RegionFile: # Relative path of region description file
left_right.1.regions

Sensors: # List of sensor propositions and their state (enabled = 1, disabled = 0)


======== SPECIFICATION ========

RegionMapping: # Mapping between region names and their decomposed counterparts
right = p1
mid = p2
others = 
left = p3

Spec: # Specification in structured English
if not vleft then visit left
if not vright then visit right

vleft is set on left and reset on false
vright is set on right and reset on false

