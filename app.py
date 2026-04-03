import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(
    page_title="Australian Open Predictor",
    layout="wide"
)

def load_data():
    return pd.read_csv("ao_final_predictions.csv")

data = load_data()

st.title("Australian Open Winner Prediction")
st.markdown("Win probabilities based on historical performance and statistics.")

st.sidebar.header("Navigation")
option = st.sidebar.selectbox(
    "Choose view",
    ["Top Contenders", "Player Lookup", "Dataset Overview"]
)

if option == "Top Contenders":
    st.subheader("Top 10 Contenders")

    top10 = (
        data[["player", "win_probability"]]
        .sort_values("win_probability", ascending=False)
        .head(10)
    )

    st.dataframe(top10, use_container_width=True)

    fig, ax = plt.subplots(figsize=(8, 5))
    ax.barh(top10["player"], top10["win_probability"])
    ax.invert_yaxis()
    ax.set_xlabel("Win Probability")
    ax.set_title("Top Players")

    st.pyplot(fig)

elif option == "Player Lookup":
    st.subheader("Player Lookup")

    player = st.selectbox("Select player", sorted(data["player"].unique()))
    prob = data.loc[data["player"] == player, "win_probability"].values[0]

    st.metric("Win Probability", f"{prob:.2%}")

    st.dataframe(
        data[data["player"] == player],
        use_container_width=True
    )

else:
    st.subheader("Dataset Overview")
    st.write("Dataset shape:", data.shape)
    st.dataframe(data.head(20), use_container_width=True)
