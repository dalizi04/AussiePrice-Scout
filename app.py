import streamlit as st
import pandas as pd

# Page Config
st.set_page_config(page_title="AussiePrice Scout", page_icon="🛒", layout="wide")

st.title("🛒 AussiePrice Scout v2.1")
st.markdown("Compare grocery prices and click **Store Link** to verify or buy.")

@st.cache_data
def load_data():
    return pd.read_csv("scout_results.csv")

try:
    df = load_data()
    
    # Sidebar Filters
    search_query = st.sidebar.text_input("Product Search (English/中文):", "")
    sort_by = st.sidebar.selectbox("Sort results by:", ["unit_price", "price", "gap"])
    
    # Filter
    if search_query:
        filtered_df = df[
            df['name'].str.contains(search_query, case=False, na=False) | 
            df['chinese_name'].str.contains(search_query, case=False, na=False)
        ]
    else:
        filtered_df = df.head(100)

    filtered_df = filtered_df.sort_values(by=sort_by)

    # Display with Link Configuration
    st.subheader(f"Results ({len(filtered_df)} items)")
    
    st.data_editor(
        filtered_df,
        column_config={
            "chinese_name": "中文名称",
            "name": "Original Name",
            "unit_price": st.column_config.NumberColumn("Unit Price ($/kg or L)", format="$%.2f"),
            "price": st.column_config.NumberColumn("Price", format="$%.2f"),
            "min_p": st.column_config.NumberColumn("Min", format="$%.2f"),
            "gap": st.column_config.NumberColumn("Gap", format="$%.2f"),
            "url": st.column_config.LinkColumn("Store Link", display_text="Open Store 🔗") # 【关键更新】
        },
        disabled=True, # 防止用户在网页端修改数据
        hide_index=True,
        use_container_width=True
    )

    st.divider()
    st.caption("Credits: Data from Grocermatic. Built with Python & Streamlit.")

except Exception as e:
    st.error(f"Error loading dashboard: {e}")
    st.info("Make sure 'scout_results.csv' exists.")
