#!/usr/bin/env python
# coding: utf-8

# In[ ]:




-Permit
permit_type
permit_subtype
permit_status
permit_sequence__
permit_si_no
work_type
self_cert
filing_status

-Permittee
permittee_s_license_type
permittee_s_business_name
act_as_superintendent
permittee_s_license__
permittee_s_phone__
permittee_s_last_name
permittee_s_first_name

-Job
job__
job_start_date
job_doc___
job_type

-House
house__

-SuperIntendent
superintendent_business_name
superintendent_first___last_name

-Owner
owner_s_first_name
owner_s_last_name
owner_s_business_name
owner_s_phone__
owner_s_business_type

-Address
owner_s_zip_code
state
city
owner_s_house_street_name
owner_s_house__

-Building
bin__
bldg_type
residential
non_profit

-Location
street_name
zip_code
gis_latitude
gis_longitude
block
lot
community_board
gis_council_district
gis_census_tract
gis_nta_name

-Borough
borough

-Has (Relationship between Job and Permit)
filing_date
issuance_date
expiration_date

Building IS PART OF Borough
Building HAS Location
House IS PART OF Building
House IS OWNED BY Owner
Owner HAS Address
House HAS SuperIntendent
House HAS Job
Job HAS Permit
Permit IS ISSUED TO Permittee

