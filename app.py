import streamlit as st
import pandas as pd
import numpy as np
import pygwalker as pyg
from pygwalker.api.streamlit import StreamlitRenderer
import io

st.set_page_config(
    page_title="CSV Explorer",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

def validate_csv_structure(df, min_rows=1, required_columns=None):
    """Validate CSV structure meets requirements."""
    if required_columns is None:
        required_columns = []
    
    # Check minimum rows
    if len(df) < min_rows:
        return False, f"CSV must have minimum {min_rows} rows, but has {len(df)}"
    
    # Check required columns
    missing_columns = set(required_columns) - set(df.columns)
    if missing_columns:
        return False, f"Missing required columns: {', '.join(missing_columns)}"
    
    return True, ""

def load_csv_data(uploaded_file):
    """Load and validate CSV data from uploaded file."""
    try:
        # Read CSV file
        df = pd.read_csv(uploaded_file)
        return df, None
    except pd.errors.EmptyDataError:
        return None, "The uploaded file is empty."
    except pd.errors.ParserError as e:
        return None, f"Error parsing CSV file: {str(e)}"
    except Exception as e:
        return None, f"Unexpected error loading file: {str(e)}"

def display_data_summary(df):
    """Display basic data summary and statistics."""
    st.subheader("📈 Data Summary")
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric("Rows", len(df))
    with col2:
        st.metric("Columns", len(df.columns))
    with col3:
        st.metric("Memory Usage", f"{df.memory_usage(deep=True).sum() / 1024:.1f} KB")
    with col4:
        st.metric("Missing Values", df.isnull().sum().sum())
    
    # Data types
    st.subheader("📋 Column Information")
    col_info = pd.DataFrame({
        'Column': df.columns,
        'Data Type': df.dtypes.astype(str),
        'Non-Null Count': df.count(),
        'Null Count': df.isnull().sum(),
        'Unique Values': df.nunique()
    })
    st.dataframe(col_info, use_container_width=True)

def main():
    st.title("📊 CSV Explorer")
    st.markdown("Upload a CSV file to explore and analyze your data interactively using advanced analytics tools.")
    
    # Sidebar for file upload and options
    with st.sidebar:
        st.header("🔧 Data Upload")
        uploaded_file = st.file_uploader(
            "Choose a CSV file",
            type=['csv'],
            help="Upload a CSV file to start exploring your data"
        )
        
        if uploaded_file is not None:
            st.success(f"File uploaded: {uploaded_file.name}")
            file_size = len(uploaded_file.getvalue())
            st.info(f"File size: {file_size / 1024:.1f} KB")
    
    # Main content area
    if uploaded_file is not None:
        # Load data
        with st.spinner("Loading data..."):
            df, error = load_csv_data(uploaded_file)
        
        if error:
            st.error(f"❌ {error}")
            st.stop()
        
        if df is not None and not df.empty:
            # Display data summary
            display_data_summary(df)
            
            # Data preview
            st.subheader("👀 Data Preview")
            preview_rows = st.slider("Number of rows to preview", 5, min(100, len(df)), 10)
            st.dataframe(df.head(preview_rows), use_container_width=True)
            
            # Interactive visualization with pygwalker
            st.subheader("🔍 Interactive Data Explorer")
            st.markdown("Use the interactive interface below to create visualizations and explore your data:")
            
            # Initialize pygwalker
            try:
                renderer = StreamlitRenderer(df, spec="./gw_config.json", debug=False)
                renderer.explorer()
            except Exception as e:
                st.error(f"Error initializing data explorer: {str(e)}")
                st.info("Falling back to basic pygwalker interface...")
                pyg_html = pyg.to_html(df)
                st.components.v1.html(pyg_html, height=1000, scrolling=True)
        else:
            st.warning("⚠️ The uploaded file appears to be empty.")
    
    else:
        # Welcome message when no file is uploaded
        st.info("👆 Please upload a CSV file using the sidebar to begin exploring your data.")
        
        # Sample data section
        st.subheader("🎯 What you can do:")
        st.markdown("""
        - **Upload any CSV file** and instantly see data summary statistics
        - **Preview your data** with customizable row counts
        - **Create interactive visualizations** using drag-and-drop interface
        - **Explore relationships** between different columns in your dataset
        - **Generate insights** through advanced analytics tools
        - **Export visualizations** for reports and presentations
        """)
        
        # Demo with sample data
        if st.button("🚀 Try with Sample Data"):
            sample_data = pd.DataFrame({
                'Date': pd.date_range('2024-01-01', periods=100, freq='D'),
                'Sales': np.random.randint(1000, 5000, 100),
                'Region': np.random.choice(['North', 'South', 'East', 'West'], 100),
                'Product': np.random.choice(['A', 'B', 'C'], 100)
            })
            st.session_state['sample_data'] = sample_data
            st.rerun()
    
    # Handle sample data
    if 'sample_data' in st.session_state:
        df = st.session_state['sample_data']
        st.success("📊 Sample data loaded!")
        display_data_summary(df)
        
        st.subheader("👀 Data Preview")
        st.dataframe(df.head(10), use_container_width=True)
        
        st.subheader("🔍 Interactive Data Explorer")
        try:
            renderer = StreamlitRenderer(df, spec="./gw_config.json", debug=False)
            renderer.explorer()
        except Exception as e:
            pyg_html = pyg.to_html(df)
            st.components.v1.html(pyg_html, height=1000, scrolling=True)

if __name__ == "__main__":
    main()