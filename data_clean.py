import pandas as pd
import csv
import numpy as np
# Load the data
df =pd.read_csv('data/small.csv')




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



print(df.columns)