#!/usr/bin/env python
# coding: utf-8

# In[ ]:








# In[ ]:





# In[ ]:


#borough needs no replacement
#bin needs no replacement
df["house__"].fillna("NA", inplace=True)
df["street_name"].fillna("NA", inplace=True)
#job no needs no replacement
#job doc no needs no replacement
#job type needs no replacement
df["self_cert"].fillna("NA", inplace=True)
df["block"].fillna("NA", inplace=True)
df["lot"].fillna("NA", inplace=True)
df["community_board"].fillna("NA", inplace=True)
df["zip_code"].fillna("NA", inplace=True)
df["bldg_type"].fillna(2, inplace=True)
df["residential"].fillna("NA", inplace=True)

df["work_type"].fillna("OT",inplace=True)
df["permit_status"].fillna("IN PROCESS", inplace=True)
#filing status no replacement
df["permit_type"].fillna("SG",inplace=True)
df["permit_subtype"].fillna("NA", inplace=True)


df["filing_date"].fillna("NA", inplace=True)
df["issuance_date"].fillna("NA", inplace=True)
df["expiration_date"].fillna("NA", inplace=True)
df["job_start_date"].fillna("NA", inplace=True)
df["permittee_s_first_name"].fillna("NA", inplace=True)
df["permittee_s_last_name"].fillna("NA", inplace=True)
df["permittee_s_business_name"].fillna("NA", inplace=True)
df["permittee_s_phone__"].fillna(0, inplace=True)
df["permittee_s_license_type"].fillna("NA", inplace=True)
df["permittee_s_license__"].fillna(0, inplace=True)
df["act_as_superintendent"].fillna("blank", inplace=True)



df["superintendent_first___last_name"].fillna("NA", inplace=True)
df["superintendent_business_name"].fillna("NA", inplace=True)
df["owner_s_business_type"].fillna("NA", inplace=True)
df["non_profit"].fillna("N", inplace=True)
df["owner_s_business_name"].fillna("NA", inplace=True)
df["owner_s_first_name"].fillna("NA", inplace=True)
df["owner_s_last_name"].fillna("NA", inplace=True)
df["owner_s_house__"].fillna("NA", inplace=True)
df["owner_s_house_street_name"].fillna("NA", inplace=True)
df["city"].fillna("NA", inplace=True)
df["state"].fillna("NA", inplace=True)
df["owner_s_zip_code"].fillna("NA", inplace=True)
df["owner_s_phone__"].fillna("NA", inplace=True)
df['dobrundate'].fillna('NA', inplace=True)
df["gis_latitude"].fillna("NA", inplace=True)
df["gis_longitude"].fillna("NA", inplace=True)
df["gis_council_district"].fillna("NA", inplace=True)
df["gis_census_tract"].fillna("NA", inplace=True)
df["gis_nta_name"].fillna("NA", inplace=True)

