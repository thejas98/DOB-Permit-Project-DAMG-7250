#!/usr/bin/env python
# coding: utf-8

# In[ ]:


(/, Load, data, from, CSV, files)

LOAD CSV WITH HEADERS FROM "file:///small_clean.csv" AS row
CREATE (:Permit {
    permit_sequence__:row.permit_sequence__,
    permit_status:row.permit_status,
    permit_si_no:row.permit_si_no,
    issuance_date:row.issuance_date,
    expiration_date:row.expiration_date,
    job_start_date:row.job_start_date
})

CREATE (:Permit details {
  permit_type: row.permit_type,
  permit_subtype: row.permit_subtype,
  self_cert: row.self_cert,
  work_type: row.work_type
})

CREATE (:Job {
  job__: row.job__,
  job_doc___: row.job_doc___,
  job_type: row.job_type
})

CREATE (:Permittee {
  permittee_s_first_name: row.permittee_s_first_name,
  permittee_s_last_name: row.permittee_s_last_name,
  permittee_s_phone__: row.permittee_s_phone__,
  permittee_s_license__:row.permittee_s_license__,
    
})

CREATE (:Filing {
  filing_date: row.filing_date,
  filing_status: row.filing_status
})

CREATE (:Building {
    bin__: row.bin__,
    community_board: row.community_board,
    house__: row.house__,
    bldg_type:row.bldg_type,
    residential:row.residential,
    site_fill:row.site_fill,
    non_profit:row.non_profit
    
})

CREATE (:Borough {
  borough: row.borough
})

CREATE (:Location {
    street_name: row.street_name,
    zip_code: row.zip_code,
    gis_latitude: row.gis_latitude,
    gis_longitude:row.gis_longitude,
    block:row.block,
    lot:row.lot,
    gis_council_district:row.gis_council_district,
    gis_census_tract:row.gis_census_tract,
    gis_nta_name:row.gis_nta_name,
    
})

CREATE (:SuperIntendent {
  superintendent_first___last_name: row.superintendent_first___last_name,
  superintendent_business_name: row.superintendent_business_name
    
})

CREATE (:Owner {
  owner_s_business_type: row.owner_s_business_type,
  owner_s_first_name: row.owner_s_first_name,
  owner_s_last_name: row.owner_s_last_name,
  owner_s_phone__:row.owner_s_phone__,
  owner_s_business_name:row.owner_s_business_name
    
})

CREATE (:Address {
  owner_s_house__: row.owner_s_house__,
  owner_s_house_street_name: row.owner_s_house_street_name,
  city: row.city,
  state:row.state,
  owner_s_zip_code:row.owner_s_zip_code
    
})

