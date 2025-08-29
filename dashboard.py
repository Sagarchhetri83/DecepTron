import streamlit as st
import pandas as pd
import sqlite3
from pathlib import Path

# --- Page Configuration ---
st.set_page_config(
    page_title="DecepTron SOC Dashboard",
    page_icon="🛡️",
    layout="wide"
)

# --- Database Connection ---
DB_PATH = Path(__file__).parent / "data" / "deceptron_logs.db"


def load_data():
    """Connects to the SQLite DB and returns interactions as a DataFrame."""
    if not DB_PATH.exists():
        st.error(f"Database not found at {DB_PATH}. Please run the honeypot first to create the database.")
        return pd.DataFrame() # Return empty dataframe
    
    try:
        conn = sqlite3.connect(DB_PATH)
        df = pd.read_sql_query("SELECT * FROM interactions ORDER BY timestamp DESC", conn)
        conn.close()
        return df
    except Exception as e:
        st.error(f"An error occurred while reading the database: {e}")
        return pd.DataFrame()

# --- Dashboard UI ---
st.title("🛡️ DecepTron - Live Threat Intelligence Dashboard")

# Auto-refreshing container
placeholder = st.empty()

def draw_dashboard():
    df = load_data()

    if df.empty:
        with placeholder.container():
            st.warning("No attack data yet. Start the honeypot and try connecting to it.")
        return

    with placeholder.container():
        _extracted_from_draw_dashboard_10(df)


# TODO Rename this here and in `draw_dashboard`
def _extracted_from_draw_dashboard_10(df):
    st.header("Attack Analytics")

    # Top Metrics
    total_interactions = len(df)
    unique_attackers = df['ip_address'].nunique()

    col1, col2 = st.columns(2)
    col1.metric("Total Interactions", total_interactions)
    col2.metric("Unique Attacker IPs", unique_attackers)

    # Charts
    st.subheader("Top 5 Attacker IPs")
    top_ips = df['ip_address'].value_counts().head(5)
    st.bar_chart(top_ips)

    st.header("Live Interaction Log")
    st.dataframe(df, width='stretch')

draw_dashboard()