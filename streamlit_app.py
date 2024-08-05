import streamlit as st
import pandas as pd

# long_ic_theme.py content
def set_theme(theme):
    if theme == "Gradient":
        st.markdown(
            """
            <style>
            body {
                background: linear-gradient(135deg, #3C7CE2, #17A4AA);
                color: #000000;
            }
            .stApp {
                background: linear-gradient(135deg, #3C7CE2, #17A4AA);
            }
            .stNumberInput > div > div > input {
                width: 80px !important;
                background: #ffffff;
                color: #000000;
            }
            .stCheckbox > div {
                margin-top: -10px;
                color: #000000;
            }
            .stButton > button {
                background: #4CAF50;
                color: white;
                border: none;
                padding: 10px 24px;
                text-align: center;
                text-decoration: none;
                display: inline-block;
                font-size: 16px;
                margin: 4px 2px;
                cursor: pointer;
                border-radius: 16px;
            }
            .stButton > button:hover {
                background-color: #45a049;
            }
            </style>
            """,
            unsafe_allow_html=True
        )
    elif theme == "Dark":
        st.markdown(
            """
            <style>
            body {
                background: #2E2E2E;
                color: #FFFFFF;
            }
            .stApp {
                background: #2E2E2E;
            }
            .stNumberInput > div > div > input {
                width: 80px !important;
                background: #555555;
                color: #FFFFFF;
            }
            .stCheckbox > div, .stRadio > div, .stSelectbox > div, .stMultiSelect > div {
                color: #FFFFFF !important;
            }
            .stMarkdown h1, .stMarkdown h2, .stMarkdown h3, .stMarkdown p, .stMarkdown ul, .stMarkdown li {
                color: #FFFFFF !important;
            }
            .stButton > button {
                background: #333333;
                color: white;
                border: none;
                padding: 10px 24px;
                text-align: center;
                text-decoration: none;
                display: inline-block;
                font-size: 16px;
                margin: 4px 2px;
                cursor: pointer;
                border-radius: 16px;
            }
            .stButton > button:hover {
                background-color: #444444;
            }
            </style>
            """,
            unsafe_allow_html=True
        )
    elif theme == "Light":
        st.markdown(
            """
            <style>
            body {
                background: #FFFFFF;
                color: #000000;
            }
            .stApp {
                background: #FFFFFF;
            }
            .stNumberInput > div > div > input {
                width: 80px !important;
                background: #ffffff;
                color: #000000;
            }
            .stCheckbox > div {
                margin-top: -10px;
                color: #000000;
            }
            .stButton > button {
                background: #008CBA;
                color: white;
                border: none;
                padding: 10px 24px;
                text-align: center;
                text-decoration: none;
                display: inline-block;
                font-size: 16px;
                margin: 4px 2px;
                cursor: pointer;
                border-radius: 16px;
            }
            .stButton > button:hover {
                background-color: #007BB5;
            }
            </style>
            """,
            unsafe_allow_html=True
        )
    elif theme == "Blue Ocean":
        st.markdown(
            """
            <style>
            body {
                background: linear-gradient(135deg, #1e3c72 0%, #2a5298 100%);
                color: #FFFFFF;
            }
            .stApp {
                background: linear-gradient(135deg, #008CBA, #8434a5);
            }
            .stNumberInput > div > div > input {
                width: 80px !important;
                background: #ffffff;
                color: #000000;
            }
            .stCheckbox > div, .stRadio > div, .stSelectbox > div, .stMultiSelect > div {
                color: #FFFFFF !important;
            }
            .stMarkdown h1, .stMarkdown h2, .stMarkdown h3, .stMarkdown p, .stMarkdown ul, .stMarkdown li {
                color: #FFFFFF !important;
            }
            .stButton > button {
                background: #005f99;
                color: white;
                border: none;
                padding: 10px 24px;
                text-align: center;
                text-decoration: none;
                display: inline-block;
                font-size: 16px;
                margin: 4px 2px;
                cursor: pointer;
                border-radius: 16px;
            }
            .stButton > button:hover {
                background-color: #004080;
            }
            </style>
            """,
            unsafe_allow_html=True
        )
    elif theme == "Forest Green":
        st.markdown(
            """
            <style>
            body {
                background: linear-gradient(135deg, #2e8b57 0%, #3cb371 100%);
                color: #FFFFFF;
            }
            .stApp {
                background: linear-gradient(135deg, #2e8b57 0%, #3cb371 100%);
            }
            .stNumberInput > div > div > input {
                width: 80px !important;
                background: #ffffff;
                color: #000000;
            }
            .stCheckbox > div, .stRadio > div, .stSelectbox > div, .stMultiSelect > div {
                color: #FFFFFF !important;
            }
            .stMarkdown h1, .stMarkdown h2, .stMarkdown h3, .stMarkdown p, .stMarkdown ul, .stMarkdown li {
                color: #FFFFFF !important;
            }
            .stButton > button {
                background: #228b22;
                color: white;
                border: none;
                padding: 10px 24px;
                text-align: center;
                text-decoration: none;
                display: inline-block;
                font-size: 16px;
                margin: 4px 2px;
                cursor: pointer;
                border-radius: 16px;
            }
            .stButton > button:hover {
                background-color: #006400;
            }
            </style>
            """,
            unsafe_allow_html=True
        )
    # Add other themes here...

# long_IC_matrix.py content
if 'wide_layout' not in st.session_state:
    st.session_state.wide_layout = False

if 'allocation' not in st.session_state:
    st.session_state.allocation = 100

def initialize_state():
    if 'original_account_size' not in st.session_state:
        st.session_state.original_account_size = 50000.00
    if 'account_size' not in st.session_state:
        st.session_state.account_size = 50000.00
    if 'trade_price' not in st.session_state:
        st.session_state.trade_price = 2.00
    if 'loss' not in st.session_state:
        st.session_state.loss = st.session_state.trade_price
    if 'commission_per_contract' not in st.session_state:
        st.session_state.commission_per_contract = 5.00
    for i in range(1, 15):
        if f"level_{i}" not in st.session_state:
            st.session_state[f"level_{i}"] = True
        if f"contracts_{i}" not in st.session_state:
            st.session_state[f"contracts_{i}"] = 1
        if f"trade_price_Level {i}" not in st.session_state:
            st.session_state[f"trade_price_Level {i}"] = 2.00
        if f"stop_Level {i}" not in st.session_state:
            st.session_state[f"stop_Level {i}"] = 0.00
        if f"full_ic_close_Level {i}" not in st.session_state:
            st.session_state[f"full_ic_close_Level {i}"] = False
        if f"one_side_close_Level {i}" not in st.session_state:
            st.session_state[f"one_side_close_Level {i}"] = False
        if f"inside_Level {i}" not in st.session_state:
            st.session_state[f"inside_Level {i}"] = False

initialize_state()

def toggle_wide_layout():
    st.session_state.wide_layout = not st.session_state.wide_layout
    st.experimental_rerun()

def reset_values():
    st.session_state.update({
        'original_account_size': 50000.00,
        'account_size': 50000.00,
        'trade_price': 2.00,
        'loss': 2.00,
        'commission_per_contract': 5.00,
        'allocation': 100,
    })
    for i in range(1, 15):
        st.session_state.update({
            f"level_{i}": True,
            f"contracts_{i}": 1,
            f"trade_price_Level {i}": 2.00,
            f"stop_Level {i}": 0.00,
            f"full_ic_close_Level {i}": False,
            f"one_side_close_Level {i}": False,
            f"inside_Level {i}": False,
        })

def update_loss():
    st.session_state.loss = st.session_state.trade_price

def ensure_single_close(level, close_type):
    if close_type == 'full_ic_close':
        st.session_state[f"one_side_close_Level {level}"] = False
        st.session_state[f"inside_Level {level}"] = False
    elif close_type == 'one_side_close':
        st.session_state[f"full_ic_close_Level {level}"] = False
        st.session_state[f"inside_Level {level}"] = False
    elif close_type == 'inside':
        st.session_state[f"full_ic_close_Level {level}"] = False
        st.session_state[f"one_side_close_Level {level}"] = False

def update_allocation(allocation):
    st.session_state.allocation = allocation
    st.session_state.account_size = st.session_state.original_account_size * (allocation / 100)

def main():
    st.set_page_config(layout="wide" if st.session_state.wide_layout else "centered")

    theme = st.selectbox("Theme", ["Gradient", "Dark", "Light", "Blue Ocean", "Forest Green"])
    set_theme(theme)

    st.title("SPX Program Matrix Calc")

    st.checkbox("Wide Layout", value=st.session_state.wide_layout, on_change=toggle_wide_layout)

    if st.button("Reset", on_click=reset_values):
        st.experimental_rerun()

    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.checkbox("100% Allocation", value=st.session_state.allocation == 100, on_change=update_allocation, args=(100,))
    with col2:
        st.checkbox("75% Allocation", value=st.session_state.allocation == 75, on_change=update_allocation, args=(75,))
    with col3:
        st.checkbox("50% Allocation", value=st.session_state.allocation == 50, on_change=update_allocation, args=(50,))
    with col4:
        st.checkbox("25% Allocation", value=st.session_state.allocation == 25, on_change=update_allocation, args=(25,))

    original_account_size = st.number_input("Original Account Size:", value=st.session_state.original_account_size, step=500.00, key='original_account_size', on_change=lambda: update_allocation(st.session_state.allocation))
    account_size = st.number_input("Current Account Size:", value=st.session_state.account_size, step=500.00, key='account_size', disabled=True)
    trade_price = st.number_input("Trade Price:", value=st.session_state.trade_price, step=0.05, key='trade_price', on_change=update_loss)
    loss = st.number_input("Loss:", value=st.session_state.loss, step=0.01, disabled=True, key='loss')
    commission_per_contract = st.number_input("Commission per Contract:", value=st.session_state.commission_per_contract, step=0.01, key='commission_per_contract')

    st.markdown("### Levels 1 to 14")
    col1, col2 = st.columns(2)
    with col1:
        for i in range(1, 8):
            st.checkbox(f"Level {i}", value=st.session_state[f"level_{i}"], key=f"level_{i}")
            st.number_input("", value=st.session_state[f"contracts_{i}"], step=1, key=f"contracts_{i}")
    with col2:
        for i in range(8, 15):
            st.checkbox(f"Level {i}", value=st.session_state[f"level_{i}"], key=f"level_{i}")
            st.number_input("", value=st.session_state[f"contracts_{i}"], step=1, key=f"contracts_{i}")

    st.subheader("Static Matrix Chart")
    data = {
        "Level": [f"Level {i}" for i in range(1, 15)],
        "Contracts": [st.session_state[f"contracts_{i}"] for i in range(1, 15)],
        "Debit": [st.session_state.trade_price * st.session_state[f"contracts_{i}"] * 100 for i in range(1, 15)],
        "Commission": [st.session_state.commission_per_contract * st.session_state[f"contracts_{i}"] for i in range(1, 15)],
        "BP": [st.session_state.trade_price * st.session_state[f"contracts_{i}"] * 100 + st.session_state.commission_per_contract * st.session_state[f"contracts_{i}"] for i in range(1, 15)],
        "Profit": [(500 * st.session_state[f"contracts_{i}"]) - st.session_state.trade_price * st.session_state[f"contracts_{i}"] * 100 - st.session_state.commission_per_contract * st.session_state[f"contracts_{i}"] for i in range(1, 15)],
        "Loss": [-1 * (st.session_state.trade_price * st.session_state[f"contracts_{i}"] * 100 + st.session_state.commission_per_contract * st.session_state[f"contracts_{i}"]) for i in range(1, 15)],
        "Cumulative Loss": [0 for i in range(1, 15)],
        "Series Gain/Loss": [0 for i in range(1, 15)],
        "After Win": [0 for i in range(1, 15)],
        "Gain%": [0 for i in range(1, 15)],
        "After Loss": [0 for i in range(1, 15)],
        "Loss%": [0 for i in range(1, 15)],
    }

    df = pd.DataFrame(data)

    df['Cumulative Loss'] = df['Loss'].cumsum()

    df['Series Gain/Loss'].iloc[0] = df['Profit'].iloc[0]

    for i in range(1, len(df)):
        df.at[i, 'Series Gain/Loss'] = df.at[i - 1, 'Series Gain/Loss'] + df.at[i, 'Profit']

    for i in range(1, len(df)):
        df.at[i, 'After Win'] = df.at[i - 1, 'After Win'] + (500 * df.at[i, 'Contracts']) if df.at[i, 'Profit'] > 0 else df.at[i - 1, 'After Win']
        df.at[i, 'After Loss'] = df.at[i - 1, 'After Loss'] + df.at[i, 'Loss'] if df.at[i, 'Profit'] <= 0 else df.at[i - 1, 'After Loss']
        df.at[i, 'Gain%'] = (df.at[i, 'After Win'] / df.at[i - 1, 'After Win']) * 100 if df.at[i - 1, 'After Win'] > 0 else 0
        df.at[i, 'Loss%'] = (df.at[i, 'After Loss'] / df.at[i - 1, 'After Loss']) * 100 if df.at[i - 1, 'After Loss'] > 0 else 0

    st.dataframe(df)

if __name__ == "__main__":
    main()
