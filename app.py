import os
import pandas as pd
import streamlit as st

st.title("Factory Search System")

# قراءة ملفات Excel
files = os.listdir("ExcelFiles")

# إزالة .xlsx من الاسم المعروض
sector_names = [file.replace(".xlsx", "") for file in files]

selected_sector_name = st.selectbox(
    "Select Industrial Sector",
    sector_names
)

# الحصول على اسم الملف الحقيقي
selected_file = files[sector_names.index(selected_sector_name)]

file_path = os.path.join("ExcelFiles", selected_file)

# قراءة المدن
excel_file = pd.ExcelFile(file_path)

cities = excel_file.sheet_names

city = st.selectbox(
    "Select City",
    cities
)

# قراءة بيانات المدينة
df = pd.read_excel(file_path, sheet_name=city)

# قراءة الأعمدة
columns = list(df.columns)

selected_column = st.selectbox(
    "Select Information Type",
    columns
)

# البحث
if st.button("Search"):

    company_column = df.columns[0]

    # إذا اختار المستخدم اسم المصنع نفسه
    if selected_column == company_column:
        results = df[[company_column]].dropna()

    # إذا اختار أي عمود آخر
    else:
        results = df[[company_column, selected_column]].dropna()

    st.subheader("Results")

    st.dataframe(
        results,
        use_container_width=True,
        hide_index=True
    )