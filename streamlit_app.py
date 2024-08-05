# app.py

import streamlit as st
import pandas as pd
import math

# The content of long_ic_theme.py
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
    trade_price = st.number_input("TradePrice:", value=st.session_state.trade_price, step=0.05, key='trade_price', on_change=update_loss)
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
        df['Series Gain/Loss'].iloc[i] = df['Profit'].iloc[i] + df['Cumulative Loss'].iloc[i-1]

    df['After Win'] = st.session_state.account_size + df['Series Gain/Loss']

    df['Gain%'] = (df['Series Gain/Loss'] / st.session_state.account_size) * 100

    df['After Loss'] = st.session_state.account_size + df['Cumulative Loss']

    df['Loss%'] = (df['Cumulative Loss'] / st.session_state.account_size) * 100

    def style_table(df):
        def color_negative_red(val):
            try:
                val = float(val)
                color = 'red' if val < 0 else 'black'
            except ValueError:
                color = 'black'
            return f'color: {color}'

        if 'Loss' in df.columns and 'Cumulative Loss' in df.columns and 'Series Gain/Loss' in df.columns and 'Gain%' in df.columns and 'Loss%' in df.columns:
            df_styled = df.style.applymap(color_negative_red, subset=['Loss', 'Cumulative Loss', 'Series Gain/Loss', 'Gain%', 'Loss%'])
        else:
            df_styled = df.style

        df_styled = df_styled.format({
            'Contracts': '{:.2f}',
            'Debit': '{:.2f}',
            'Stop': '{:.2f}',
            'Commission': '{:.2f}',
            'BP': '{:.2f}',
            'Profit': '{:.2f}',
            'Loss': '{:.2f}',
            'Cumulative Loss': '{:.2f}',
            'Series Gain/Loss': '{:.2f}',
            'After Win': '{:.2f}',
            'Gain%': '{:.2f}%',
            'After Loss': '{:.2f}',
            'Loss%': '{:.2f}%'
        })

        styles = [
            dict(selector="th", props=[
                ("font-size", "110%"),
                ("text-align", "center"),
                ("background-color", "#f0f0f0"),
                ("padding", "10px"),
                ("border", "1px solid #ddd")
            ]),
            dict(selector="td", props=[
                ("text-align", "center"),
                ("padding", "10px"),
                ("border", "1px solid #ddd")
            ]),
            dict(selector="tr:nth-child(even)", props=[("background-color", "#ffffff")]),
            dict(selector="tr:nth-child(odd)", props=[("background-color", "#ffffff")]),
            dict(selector="tr:hover", props=[("background-color", "#f1f1f1")]),
            dict(selector="table", props=[
                ("border-collapse", "collapse"),
                ("width", "100%")
            ]),
            dict(selector="caption", props=[
                ("caption-side", "bottom"),
                ("text-align", "center"),
                ("padding", "10px"),
                ("font-weight", "bold")
            ]),
        ]

        return df_styled.set_table_styles(styles).hide(axis='index')

    filtered_df = df[df['Level'].apply(lambda x: st.session_state[f"level_{int(x.split()[1])}"])]

    styled_df = style_table(filtered_df)
    st.write(styled_df.to_html(), unsafe_allow_html=True)

    st.subheader("Dynamic Matrix Premium")

    col4, col5 = st.columns(2)

    with col4:
        for i in range(1, 8):
            level_name = f"Level {i}"
            st.number_input(f"TradePrice {level_name}", value=st.session_state[f"trade_price_Level {i}"], step=0.05, key=f"trade_price_{level_name}")
            st.number_input(f"Stop {level_name}", value=st.session_state[f"stop_Level {i}"], step=0.01, key=f"stop_{level_name}")
            st.checkbox("Full IC Close", value=st.session_state[f"full_ic_close_Level {i}"], key=f"full_ic_close_{level_name}", on_change=ensure_single_close, args=(i, 'full_ic_close'))
            st.checkbox("One Side Close", value=st.session_state[f"one_side_close_Level {i}"], key=f"one_side_close_{level_name}", on_change=ensure_single_close, args=(i, 'one_side_close'))
            st.checkbox("Inside", value=st.session_state[f"inside_Level {i}"], key=f"inside_{level_name}", on_change=ensure_single_close, args=(i, 'inside'))

    with col5:
        for i in range(8, 15):
            level_name = f"Level {i}"
            st.number_input(f"TradePrice {level_name}", value=st.session_state[f"trade_price_Level {i}"], step=0.05, key=f"trade_price_{level_name}")
            st.number_input(f"Stop {level_name}", value=st.session_state[f"stop_Level {i}"], step=0.01, key=f"stop_{level_name}")
            st.checkbox("Full IC Close", value=st.session_state[f"full_ic_close_Level {i}"], key=f"full_ic_close_{level_name}", on_change=ensure_single_close, args=(i, 'full_ic_close'))
            st.checkbox("One Side Close", value=st.session_state[f"one_side_close_Level {i}"], key=f"one_side_close_{level_name}", on_change=ensure_single_close, args=(i, 'one_side_close'))
            st.checkbox("Inside", value=st.session_state[f"inside_Level {i}"], key=f"inside_{level_name}", on_change=ensure_single_close, args=(i, 'inside'))

    st.subheader("Dynamic Matrix Chart")

    dynamic_data = {
        "Level": [f"Level {i}" for i in range(1, 15)],
        "Contracts": [st.session_state[f"contracts_{i}"] for i in range(1, 15)],
        "Debit": [st.session_state[f"trade_price_Level {i}"] * st.session_state[f"contracts_{i}"] * 100 for i in range(1, 15)],
        "Stop": [round(st.session_state[f"stop_Level {i}"] * 100 * st.session_state[f"contracts_{i}"], 2) if st.session_state[f"full_ic_close_Level {i}"] or st.session_state[f"one_side_close_Level {i}"] else 0.00 for i in range(1, 15)],
        "Commission": [
                st.session_state.commission_per_contract * st.session_state[f"contracts_{i}"] * 2 if st.session_state[f"full_ic_close_Level {i}"]
            else st.session_state.commission_per_contract * st.session_state[f"contracts_{i}"] + st.session_state.commission_per_contract * st.session_state[f"contracts_{i}"] / 2 if st.session_state[f"one_side_close_Level {i}"]
            else st.session_state.commission_per_contract * st.session_state[f"contracts_{i}"]
            for i in range(1, 15)
        ],
        "BP": [st.session_state[f"trade_price_Level {i}"] * st.session_state[f"contracts_{i}"] * 100 + (
            st.session_state.commission_per_contract * st.session_state[f"contracts_{i}"] * 2 if st.session_state[f"full_ic_close_Level {i}"]
            else st.session_state.commission_per_contract * st.session_state[f"contracts_{i}"] + st.session_state.commission_per_contract * st.session_state[f"contracts_{i}"] / 2 if st.session_state[f"one_side_close_Level {i}"]
            else st.session_state.commission_per_contract * st.session_state[f"contracts_{i}"]
        ) for i in range(1, 15)],
        "Profit": [
            0 if st.session_state[f"inside_Level {i}"] else max(0, (st.session_state[f"trade_price_Level {i}"] * st.session_state[f"contracts_{i}"] * 100) - (
                st.session_state[f"stop_Level {i}"] * 100 * st.session_state[f"contracts_{i}"] + (
                    st.session_state.commission_per_contract * st.session_state[f"contracts_{i}"] * 2 if st.session_state[f"full_ic_close_Level {i}"]
                    else st.session_state.commission_per_contract * st.session_state[f"contracts_{i}"] + st.session_state.commission_per_contract * st.session_state[f"contracts_{i}"] / 2 if st.session_state[f"one_side_close_Level {i}"]
                    else st.session_state.commission_per_contract * st.session_state[f"contracts_{i}"]
                )
            )) for i in range(1, 15)
        ],
        "Loss": [
            -((st.session_state[f"trade_price_Level {i}"] * st.session_state[f"contracts_{i}"] * 100) + (
                st.session_state.commission_per_contract * st.session_state[f"contracts_{i}"] * 2 if st.session_state[f"full_ic_close_Level {i}"]
                else st.session_state.commission_per_contract * st.session_state[f"contracts_{i}"] + st.session_state.commission_per_contract * st.session_state[f"contracts_{i}"] / 2 if st.session_state[f"one_side_close_Level {i}"]
                else st.session_state.commission_per_contract * st.session_state[f"contracts_{i}"]
            )) if st.session_state[f"inside_Level {i}"] or (st.session_state[f"trade_price_Level {i}"] * st.session_state[f"contracts_{i}"] * 100) - (
                st.session_state[f"stop_Level {i}"] * 100 * st.session_state[f"contracts_{i}"] + (
                    st.session_state.commission_per_contract * st.session_state[f"contracts_{i}"] * 2 if st.session_state[f"full_ic_close_Level {i}"]
                    else st.session_state.commission_per_contract * st.session_state[f"contracts_{i}"] + st.session_state.commission_per_contract * st.session_state[f"contracts_{i}"] / 2 if st.session_state[f"one_side_close_Level {i}"]
                    else st.session_state.commission_per_contract * st.session_state[f"contracts_{i}"]
                )
            ) <= 0 else 0 for i in range(1, 15)
        ],
        "Cumulative Loss": [0 for i in range(1, 15)],
        "Series Gain/Loss": [0 for i in range(1, 15)],
        "After Win": [0 for i in range(1, 15)],
        "Gain%": [0 for i in range(1, 15)],
        "After Loss": [0 for i in range(1, 15)],
        "Loss%": [0 for i in range(1, 15)],
    }

    dynamic_df = pd.DataFrame(dynamic_data)

    dynamic_df['Cumulative Loss'] = dynamic_df['Loss'].cumsum()

    dynamic_df['Series Gain/Loss'].iloc[0] = dynamic_df['Profit'].iloc[0] if dynamic_df['Profit'].iloc[0] > 0 else -abs(dynamic_df['Cumulative Loss'].iloc[0])
    for i in range(1, len(dynamic_df)):
        if dynamic_df['Profit'].iloc[i] > 0:
            dynamic_df['Series Gain/Loss'].iloc[i] = dynamic_df['Profit'].iloc[i]
        else:
            dynamic_df['Series Gain/Loss'].iloc[i] = -abs(dynamic_df['Cumulative Loss'].iloc[i])

    dynamic_df['After Win'] = st.session_state.account_size + dynamic_df['Series Gain/Loss']

    dynamic_df['Gain%'] = (dynamic_df['Series Gain/Loss'] / st.session_state.account_size) * 100

    dynamic_df['After Loss'] = st.session_state.account_size + dynamic_df['Cumulative Loss']

    dynamic_df['Loss%'] = (dynamic_df['Cumulative Loss'] / st.session_state.account_size) * 100

    filtered_dynamic_df = dynamic_df[dynamic_df['Level'].apply(lambda x: st.session_state[f"level_{int(x.split()[1])}"])]

    styled_dynamic_df = style_table(filtered_dynamic_df)
    st.write(styled_dynamic_df.to_html(), unsafe_allow_html=True)

    st.subheader("Next Level Game Plan")

    # Assuming the last cumulative loss and commission are taken from dynamic_df and settings
    last_cumulative_loss = abs(dynamic_df['Cumulative Loss'].iloc[-1])  # Ensuring it's positive for calculations

    # Define debit values and calculate new BE Contracts dynamically
    debit_values = [2.50, 2.45, 2.40, 2.35, 2.30, 2.25, 2.20, 2.15, 2.10, 2.05, 2.00, 1.95, 1.90, 1.85, 1.80, 1.75, 1.70]
    be_contracts = [math.ceil(last_cumulative_loss / ((5 - debit) * 100)) for debit in debit_values]  # Round up to the nearest integer

    # Function to calculate gain, returning 0 if BE Contract is 0
    def calculate_gain(contract, debit, additional_contracts):
        if contract == 0:
            return 0
        return round(((contract + additional_contracts) * (5 - debit) * 100 - 
                    (contract + additional_contracts) * st.session_state.commission_per_contract) - 
                    last_cumulative_loss, 2)

    # Calculate BE+1 to BE+5 Gain
    be_plus_1_gain = [calculate_gain(contract, debit, 1) for debit, contract in zip(debit_values, be_contracts)]
    be_plus_2_gain = [calculate_gain(contract, debit, 2) for debit, contract in zip(debit_values, be_contracts)]
    be_plus_3_gain = [calculate_gain(contract, debit, 3) for debit, contract in zip(debit_values, be_contracts)]
    be_plus_4_gain = [calculate_gain(contract, debit, 4) for debit, contract in zip(debit_values, be_contracts)]
    be_plus_5_gain = [calculate_gain(contract, debit, 5) for debit, contract in zip(debit_values, be_contracts)]

    next_level_data = {
        "Debit": debit_values,
        "BE Contract": be_contracts,
        "BE+1 Gain": [f"{gain:.2f}" for gain in be_plus_1_gain],
        "BE+2 Gain": [f"{gain:.2f}" for gain in be_plus_2_gain],
        "BE+3 Gain": [f"{gain:.2f}" for gain in be_plus_3_gain],
        "BE+4 Gain": [f"{gain:.2f}" for gain in be_plus_4_gain],
        "BE+5 Gain": [f"{gain:.2f}" for gain in be_plus_5_gain]
    }

    next_level_df = pd.DataFrame(next_level_data)

    styled_next_level_df = style_table(next_level_df)
    st.write(styled_next_level_df.to_html(), unsafe_allow_html=True)

if __name__ == "__main__":
    main()
