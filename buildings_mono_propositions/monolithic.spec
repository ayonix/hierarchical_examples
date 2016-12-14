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
monolithic

Customs: # List of custom propositions
d1
d2
d3
d4
d5
d7
d6

RegionFile: # Relative path of region description file
monolithic.regions

Sensors: # List of sensor propositions and their state (enabled = 1, disabled = 0)


======== SPECIFICATION ========

RegionMapping: # Mapping between region names and their decomposed counterparts
1_3_22 = 1_3_22
1_1_14 = 1_1_14
2_1_12 = 2_1_12
1_3_21 = 1_3_21
1_1_11 = 1_1_11
2_1_33 = 2_1_33
1_1_13 = 1_1_13
1_1_12 = 1_1_12
2_1_21 = 2_1_21
1_1_34 = 1_1_34
1_1_33 = 1_1_33
1_1_32 = 1_1_32
1_1_31 = 1_1_31
1_3_32 = 1_3_32
2_1_14 = 2_1_14
1_2_21 = 1_2_21
1_3_41 = 1_3_41
1_2_23 = 1_2_23
1_2_22 = 1_2_22
1_3_42 = 1_3_42
2_2_11 = 2_2_11
2_2_13 = 2_2_13
1_3_43 = 1_3_43
2_1_23 = 2_1_23
2_3_32 = 2_3_32
2_2_33 = 2_2_33
2_2_32 = 2_2_32
2_2_31 = 2_2_31
2_1_31 = 2_1_31
2_1_24 = 2_1_24
2_1_22 = 2_1_22
1_3_23 = 1_3_23
2_3_51 = 2_3_51
2_3_12 = 2_3_12
2_3_52 = 2_3_52
2_1_34 = 2_1_34
2_3_11 = 2_3_11
1_3_31 = 1_3_31
1_1_21 = 1_1_21
1_1_22 = 1_1_22
1_1_23 = 1_1_23
1_1_24 = 1_1_24
1_2_11 = 1_2_11
1_2_12 = 1_2_12
1_2_13 = 1_2_13
1_3_13 = 1_3_13
1_3_12 = 1_3_12
1_3_11 = 1_3_11
2_2_12 = 2_2_12
2_1_11 = 2_1_11
3_1_1 = 3_1_1
1_2_32 = 1_2_32
1_2_33 = 1_2_33
1_2_31 = 1_2_31
2_3_31 = 2_3_31
2_3_22 = 2_3_22
2_3_21 = 2_3_21
1_3_33 = 1_3_33
2_2_21 = 2_2_21
2_2_22 = 2_2_22
2_2_23 = 2_2_23
2_3_41 = 2_3_41
2_1_32 = 2_1_32
2_3_42 = 2_3_42
2_1_13 = 2_1_13
2_3_62 = 2_3_62
2_3_61 = 2_3_61

Spec: # Specification in structured English
if not d1 then visit 1_3_12
if not d2 then visit 1_2_11
if not d3 then visit 1_3_11

if not d4 then visit 3_1_1

if not d5 then visit 2_2_11
if not d6 then visit 2_3_11
if not d7 then visit 2_1_11

d1 is set on 1_3_12 and reset on false
d2 is set on 1_2_11 and reset on false
d3 is set on 1_3_11 and reset on false
d4 is set on 3_1_1 and reset on false
d5 is set on 2_2_11 and reset on false
d6 is set on 2_3_11 and reset on false
d7 is set on 2_1_11 and reset on false

