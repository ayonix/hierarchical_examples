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
buildings.2

Customs: # List of custom propositions

RegionFile: # Relative path of region description file
buildings.2.regions

Sensors: # List of sensor propositions and their state (enabled = 1, disabled = 0)
goto3, 1


======== SPECIFICATION ========

RegionMapping: # Mapping between region names and their decomposed counterparts
1 = p3
3 = p1
2 = p2
others = 

Spec: # Specification in structured English
Group buildings is 1,2
visit all buildings

#visit 1

#infinitely often not goto3
#if you are activating goto3 then always 3
#if you are activating goto1 then always not 1

