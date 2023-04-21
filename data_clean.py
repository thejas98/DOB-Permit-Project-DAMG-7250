import pandas as pd
import csv
import numpy as np
import re
# Load the data
df =pd.read_csv('data/DOB_Permit_Issuance.csv',low_memory=False)




#Columns 42-60
# Rename columns
df.rename(columns={
    "BOROUGH": "borough",
    "Bin #": "bin__",
    "House #": "house__",
    "Street Name": "street_name",
    "Job #": "job__",
    "Job doc. #": "job_doc___",
    "Job Type": "job_type",
    "Self_Cert": "self_cert",
    "Block": "block",
    "Lot": "lot",
    "Community Board": "community_board",
    "Zip Code": "zip_code",
    "Bldg Type": "bldg_type",
    "Residential": "residential",
    "Special District 1": "special_district_1",
    "Special District 2": "special_district_2",
    "Work Type": "work_type",
    "Permit Status": "permit_status",
    "Filing Status": "filing_status",
    "Permit Type": "permit_type",
    "Permit Sequence #": "permit_sequence__",
    "Permit Subtype": "permit_subtype",
    "Oil Gas": "oil_gas",
    "Site Fill": "site_fill",
    "Filing Date": "filing_date",
    "Issuance Date": "issuance_date",
    "Expiration Date": "expiration_date",
    "Job Start Date": "job_start_date",
    "Permittee's First Name": "permittee_s_first_name",
    "Permittee's Last Name": "permittee_s_last_name",
    "Permittee's Business Name": "permittee_s_business_name",
    "Permittee's Phone #": "permittee_s_phone__",
    "Permittee's License Type": "permittee_s_license_type",
    "Permittee's License #": "permittee_s_license__",
    "Act as Superintendent": "act_as_superintendent",
    "Permittee's Other Title": "permittee_s_other_title",
    "HIC License": "hic_license",
    "Site Safety Mgr's First Name": "site_safety_mgr_s_first_name",
    "Site Safety Mgr's Last Name": "site_safety_mgr_s_last_name",
    "Site Safety Mgr Business Name": "site_safety_mgr_business_name",
    "Superintendent First & Last Name": "superintendent_first___last_name",
    "Superintendent Business Name": "superintendent_business_name",
    "Owner's Business Type": "owner_s_business_type",
    "Non-Profit": "non_profit",
    "Owner's Business Name": "owner_s_business_name",
    "Owner's First Name": "owner_s_first_name",
    "Owner's Last Name": "owner_s_last_name",
    "Owner's House #": "owner_s_house__",
    "Owner's House Street Name": "owner_s_house_street_name",
    "Owner’s House City": "city",
    "Owner’s House State": "state",
    "Owner’s House Zip Code": "owner_s_zip_code",
    "Owner's Phone #": "owner_s_phone__",
    "DOBRunDate": "dobrundate",
    "PERMIT_SI_NO": "permit_si_no",
    "LATITUDE": "gis_latitude",
    "LONGITUDE": "gis_longitude",
    "COUNCIL_DISTRICT": "gis_council_district",
    "CENSUS_TRACT": "gis_census_tract",
    "NTA_NAME": "gis_nta_name"
}, inplace=True)

#borough needs no replacement
#bin needs no replacement
df["house__"].fillna("-1", inplace=True)
df["street_name"].fillna("Not Available", inplace=True)
#job no needs no replacement
#job doc no needs no replacement
#job type needs no replacement
df["self_cert"].fillna("N", inplace=True)
df["block"].fillna("00000", inplace=True)
df["lot"].fillna("00000", inplace=True)
df["community_board"].fillna("000", inplace=True)
df["zip_code"].fillna("00000", inplace=True)
df["bldg_type"].fillna(2, inplace=True)
df["residential"].fillna("N", inplace=True)
df["special_district_1"].fillna("Not Available", inplace=True)
df["special_district_2"].fillna("Not Available", inplace=True)
df["work_type"].fillna("OT",inplace=True)
df["permit_status"].fillna("IN PROCESS", inplace=True)
#filing status no replacement
df["permit_type"].fillna("SG",inplace=True)
df["permit_subtype"].fillna("OT", inplace=True)
df["oil_gas"].fillna("N", inplace=True)
df["site_fill"].fillna("Not Available", inplace=True)


df["filing_date"].fillna("12/31/9999", inplace=True)
df["issuance_date"].fillna("12/31/9999", inplace=True)
df["expiration_date"].fillna("12/31/9999", inplace=True)
df["job_start_date"].fillna("12/31/9999", inplace=True)


df["permittee_s_first_name"].fillna("John", inplace=True)
df['permittee_s_first_name'] = df['permittee_s_first_name'].apply(lambda x: x if re.match("^[a-zA-Z]+$", x) else 'John')

df["permittee_s_last_name"].fillna("Doe", inplace=True)
df['permittee_s_last_name'] = df['permittee_s_last_name'].apply(lambda x: x if re.match("^[a-zA-Z]+$", x) else 'Doe')

df["permittee_s_business_name"].fillna("John Doe Inc", inplace=True)
df['permittee_s_business_name'] = df['permittee_s_business_name'].apply(lambda x: x if re.match("^[a-zA-Z]+$", x) else 'John Doe Inc')

df["permittee_s_phone__"].fillna("9999999999", inplace=True)
df["permittee_s_license_type"].fillna("GC", inplace=True)
df["permittee_s_license__"].fillna(0, inplace=True)
df['permittee_s_license__'] = df['permittee_s_license__'].astype(str).apply(lambda x: x if re.match("^[0-9]+$", x) else '0')

df["act_as_superintendent"].fillna("N", inplace=True)


# df = df.drop('permittee_s_other_title', axis=1,inplace=True)
# df = df.drop('hic_license', axis=1,inplace=True)
# df = df.drop('site_safety_mgr_s_first_name', axis=1,inplace=True)
# df = df.drop('site_safety_mgr_s_last_name', axis=1,inplace=True)
# df = df.drop('permittee_s_other_title', axis=1,inplace=True)

df['permittee_s_other_title'] = 'Not Available'
df['hic_license'] = 'Not Available'
df['site_safety_mgr_s_first_name'] = 'Not Available'
df['site_safety_mgr_s_last_name'] = 'Not Available'
df['site_safety_mgr_business_name'] = 'Not Available'



df["superintendent_first___last_name"].fillna("John Doe", inplace=True)
df['superintendent_first___last_name'] = df['superintendent_first___last_name'].apply(lambda x: x if re.match("^[a-zA-Z]+$", x) else 'John Doe')

df["superintendent_business_name"].fillna("John Doe Inc", inplace=True)
df['superintendent_business_name'] = df['superintendent_business_name'].apply(lambda x: x if re.match("^[a-zA-Z]+$", x) else 'John Doe Inc')

df["owner_s_business_type"].fillna("Unknown", inplace=True)
df["non_profit"].fillna("N", inplace=True)
df["owner_s_business_name"].fillna("John Doe Inc", inplace=True)
df['owner_s_business_name'] = df['owner_s_business_name'].str.rstrip('\\')
df['owner_s_business_name'] = df['owner_s_business_name'].apply(lambda x: x if re.match("^[a-zA-Z]+$", x) else 'John Doe Inc')
df["owner_s_first_name"].fillna("John", inplace=True)
df["owner_s_last_name"].fillna("Doe", inplace=True)
df["owner_s_house__"].fillna("-1", inplace=True)
df["owner_s_house_street_name"].fillna("Missing street name", inplace=True)
df["city"].fillna("Not Available", inplace=True)
df["state"].fillna("Not Available", inplace=True)
df["owner_s_zip_code"].fillna("00000", inplace=True)
df["owner_s_phone__"].fillna("9999999999", inplace=True)
df['dobrundate'] = pd.to_datetime(df['dobrundate']).dt.date
df['dobrundate'].fillna('12/31/9999', inplace=True)

df["gis_latitude"].fillna("00", inplace=True)
df["gis_longitude"].fillna("00", inplace=True)
df["gis_council_district"].fillna("Not Available", inplace=True)
df["gis_census_tract"].fillna("Not Available", inplace=True)
df["gis_nta_name"].fillna("Not Available", inplace=True)

df['house_id'] = df.apply(lambda x: f"{x['house__']}_{x['gis_latitude']}_{x['gis_longitude']}", axis=1)

df['location_id'] = df['zip_code'].astype(str) + '-' + df['block'].astype(str) + '-' + df['lot'].astype(str)

df['owner_id'] = df['owner_s_first_name'].astype(str) + '-' + df['owner_s_last_name'].astype(str) + '-' + df['owner_s_phone__'].astype(str)


df.to_csv('data/DOB_Permit_Issuance_clean.csv', index=False)
# print(df.columns)