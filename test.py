#Column name - BOROUGH
df.rename(columns={"BOROUGH": "borough"}, inplace=True)

#Column name - Bin #
df.rename(columns={"Bin #": "bin__"}, inplace=True)

#Column name - House #
df.rename(columns={"House #": "house__"}, inplace=True)
df['house__'] = df['house__'].replace('', np.NaN)

#Column name - Street Name
df.rename(columns={"Street Name": "street_name"}, inplace=True)
df['street_name'] = df['street_name'].replace('', np.NaN)

#Column name - Job #
df.rename(columns={"Job #": "job__"}, inplace=True)

#Column name - Job doc. #
df.rename(columns={"Job doc. #": "job_doc___"}, inplace=True)

#Column name - Job Type
df.rename(columns={"Job Type": "job_type"}, inplace=True)

#Column name - Self_Cert
df.rename(columns={"Self_Cert": "self_cert"}, inplace=True)
df['self_cert'] = df['self_cert'].replace('R', 'Y').replace('J', np.NaN).replace('X', np.NaN)

#Column name - Block
df.rename(columns={"Block": "block"}, inplace=True)
df['block'] = df['block'].replace('', np.NaN)

#Column name - Lot
df.rename(columns={"Lot": "lot"}, inplace=True)
df['lot'] = df['lot'].replace('', np.NaN)

#Column name - Community Board
df.rename(columns={"Community Board": "community_board"}, inplace=True)
df['community_board'] = df['community_board'].replace('', np.NaN)

#Column name - Zip Code
df.rename(columns={"Zip Code": "zip_code"}, inplace=True)
df['zip_code'] = df['zip_code'].replace('', np.NaN)

#Column name - Bldg Type
df.rename(columns={"Bldg Type": "bldg_type"}, inplace=True)
df['bldg_type'] = df['bldg_type'].replace(np.NaN, 2).replace('', 2)

#Column name - Residential
df.rename(columns={"Residential": "residential"}, inplace=True)
df['residential'] = df['residential'].replace('', np.NaN)

#Column name - Special District 1
df.rename(columns={"Special District 1": "special_district_1"}, inplace=True)
df['special_district_1'] = df['special_district_1'].replace('', np.NaN)

#Column name - Special District 2
df.rename(columns={"Special District 2": "special_district_2"}, inplace=True)
df['special_district_2'] = df['special_district_2'].replace('', np.NaN)

#Column name - Work Type
df.rename(columns={"Work Type": "work_type"}, inplace=True)
df['work_type'] = df['work_type'].replace('', 'OT')

#Column name - Permit Status
df.rename(columns={"Permit Status": "permit_status"}, inplace=True)
df['permit_status'] = df['permit_status'].replace('', 'IN PROCESS')

#Column name - Filing Status
df.rename(columns={"Filing Status": "filing_status"}, inplace=True)

#Column name - Permit Type
df.rename(columns={"Permit Type": "permit_type"}, inplace=True)
df['permit_type'] = df['permit_type'].replace('', 'SG')

#columns 21-42

#Column name - Permit Sequence #
df.rename(columns={"Permit Sequence #": "permit_sequence__"}, inplace=True)


#Column name - Permit Subtype
df.rename(columns={"Permit Subtype": "permit_subtype"}, inplace=True)
df['permit_subtype'] = df['permit_subtype'].replace('', np.NaN)


#Column name - Oil Gas
df.rename(columns={"Oil Gas": "oil_gas"}, inplace=True)
df['oil_gas'] = df['oil_gas'].replace('', 'blank')


#Column name - Site Fill
df.rename(columns={"Site Fill": "site_fill"}, inplace=True)
df['site_fill'] = df['site_fill'].replace('', 'blank')


#Column name - Filing Date
df.rename(columns={"Filing Date": "filing_date"}, inplace=True)
df['filing_date'] = df['filing_date'].replace('', np.NaN)
df['filing_date'] = pd.to_datetime(df['filing_date'], errors='coerce')
df['filing_date'] = df['filing_date'].fillna(pd.NaT)


#Column name - Issuance Date
df.rename(columns={"Issuance Date": "issuance_date"}, inplace=True)
df['issuance_date'] = df['issuance_date'].replace('', np.NaN)
df['issuance_date'] = pd.to_datetime(df['issuance_date'], errors='coerce')
df['issuance_date'] = df['issuance_date'].fillna(pd.NaT)


#Column name - Expiration Date
df.rename(columns={"Expiration Date": "expiration_date"}, inplace=True)
df['expiration_date'] = df['expiration_date'].replace('', np.NaN)
df['expiration_date'] = pd.to_datetime(df['expiration_date'], errors='coerce')
df['expiration_date'] = df['expiration_date'].fillna(pd.NaT)


#Column name - Job Start Date
df.rename(columns={"Job Start Date": "job_start_date"}, inplace=True)
df['job_start_date'] = df['job_start_date'].replace('', np.NaN)
df['job_start_date'] = pd.to_datetime(df['job_start_date'], errors='coerce')
df['job_start_date'] = df['job_start_date'].fillna(pd.NaT)


#Column name - Permittee's First Name
df.rename(columns={"Permittee's First Name": "permittee_s_first_name"}, inplace=True)
df['permittee_s_first_name'] = df['permittee_s_first_name'].replace('', np.NaN)


#Column name - Permittee's Last Name
df.rename(columns={"Permittee's Last Name": "permittee_s_last_name"}, inplace=True)
df['permittee_s_last_name'] = df['permittee_s_last_name'].replace('', np.NaN)


#Column name - Permittee's Business Name
df.rename(columns={"Permittee's Business Name": "permittee_s_business_name"}, inplace=True)
df['permittee_s_business_name'] = df['permittee_s_business_name'].replace('', np.NaN)


#Column name - Permittee's Phone #
df.rename(columns={"Permittee's Phone #": "permittee_s_phone__"}, inplace=True)
df['permittee_s_phone__'].fillna(0, inplace=True)


#Column name - Permittee's License Type
df.rename(columns={"Permittee's License Type": "permittee_s_license_type"}, inplace=True)
df['permittee_s_license_type'] = df['permittee_s_license_type'].replace('', np.NaN)


#Column name - Permittee's License #
df.rename(columns={"Permittee's License #": "permittee_s_license__"}, inplace=True)
df['permittee_s_license__'].fillna(0, inplace=True)


#Column name - Act as Superintendent
df.rename(columns={"Act as Superintendent": "act_as_superintendent"}, inplace=True)
df['site_fill'] = df['site_fill'].replace('', 'blank')


#Column name - Permittee's Other Title
df.rename(columns={"Permittee's Other Title": "permittee_s_other_title"}, inplace=True)
df['permittee_s_other_title'] = df['permittee_s_other_title'].replace('', np.NaN)


#Column name - HIC License
df.rename(columns={"HIC License": "hic_license"}, inplace=True)
df['hic_license'].fillna(0, inplace=True)


#Column name - Site Safety Mgr's First Name
df.rename(columns={"Site Safety Mgr's First Name": "site_safety_mgr_s_first_name"}, inplace=True)
df['site_safety_mgr_s_first_name'] = df['site_safety_mgr_s_first_name'].replace('', np.NaN)


#Column name - Site Safety Mgr's Last Name
df.rename(columns={"Site Safety Mgr's Last Name": "site_safety_mgr_s_last_name"}, inplace=True)
df['site_safety_mgr_s_last_name'] = df['site_safety_mgr_s_last_name'].replace('', np.NaN)


#Column name - Site Safety Mgr Business Name
df.rename(columns={"Site Safety Mgr Business Name": "site_safety_mgr_business_name"}, inplace=True)
df['site_safety_mgr_business_name'] = df['site_safety_mgr_business_name'].replace('', np.NaN)


