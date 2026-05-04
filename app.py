import streamlit as st
import pickle
import json
import pandas as pd
import altair as alt

# ===============================
# 1. PAGE CONFIG
# ===============================
st.set_page_config(
    page_title="Vehicle Health Prediction Dashboard",
    layout="wide"
)

# ===============================
# 2. LOAD MODEL + FILES
# ===============================
with open("model.pkl", "rb") as f:
    model = pickle.load(f)

with open("comparison_metrics.json", "r") as f:
    comparison_metrics = json.load(f)

with open("label_classes.json", "r") as f:
    label_classes = json.load(f)

df_metrics = pd.DataFrame(comparison_metrics).T

# ===============================
# 3. CONSTANTS FROM DATASET
# ===============================
vehicle_types = ["Sedan X", "SUV Z", "Hatchback Y", "Compact A"]

components = [
    "Brake Pads",
    "Car Battery",
    "Oil Filter",
    "Shock Absorber",
    "Clutch Plate"
]

expected_life_map = {
    "Brake Pads": 40000,
    "Car Battery": 60000,
    "Oil Filter": 10000,
    "Shock Absorber": 80000,
    "Clutch Plate": 90000
}

# ===============================
# 4. TITLE
# ===============================
st.title("Predictive Vehicle Health Maintenance Dashboard")
st.markdown("Enter vehicle details to predict component health and view model performance.")

st.markdown("---")

# ===============================
# 5. USER INPUTS
# ===============================
st.subheader("Input Details")

col1, col2 = st.columns(2)

with col1:
    vehicle_type = st.selectbox("Vehicle Type", ["Select"] + vehicle_types)
    mileage = st.number_input("Mileage", min_value=0.0, step=1000.0, value=0.0)

with col2:
    component = st.selectbox("Component", ["Select"] + components)
    quantity_used = st.number_input("Quantity Used", min_value=0, value=0, step=1, format="%d")

# ===============================
# 6. PREDICTION
# ===============================
is_valid = (
    vehicle_type != "Select" and
    component != "Select"
)

if not is_valid:
    st.info("Please select Vehicle Type and Component to enable prediction.")

predict_clicked = st.button("Predict", disabled=not is_valid)

if predict_clicked:
    total_life = expected_life_map[component]
    estimated_usage = mileage * quantity_used
    remaining_life = total_life - estimated_usage

    input_data = [[mileage, quantity_used, estimated_usage, remaining_life]]
    pred_num = model.predict(input_data)[0]
    pred_label = label_classes[pred_num]

    st.subheader("Prediction Result")

    c1, c2, c3 = st.columns(3)
    with c1:
        st.metric("Vehicle Type", vehicle_type)
    with c2:
        st.metric("Component", component)
    with c3:
        st.metric("Predicted Health Status", pred_label)

    c4, c5, c6 = st.columns(3)
    with c4:
        st.metric("Expected Life (km)", total_life)
    with c5:
        st.metric("Estimated Usage (km)", estimated_usage)
    with c6:
        st.metric("Remaining Life (km)", remaining_life)

    if pred_label.lower() == "warning":
        st.error("Warning: This component may require maintenance.")
    else:
        st.success("Healthy: This component appears to be in a safe condition.")

st.markdown("---")

# ===============================
# 7. METRICS TABLE
# ===============================
st.subheader("Model Performance Metrics")
st.dataframe(df_metrics)

st.markdown("---")

# ===============================
# 8. MODEL COMPARISON GRAPH
#    Grouped vertical bars
# ===============================
st.subheader("Model Comparison Graph")

metrics_long = (
    df_metrics.reset_index()
    .rename(columns={"index": "Model"})
    .melt(id_vars="Model", var_name="Metric", value_name="Score")
)

comparison_chart = (
    alt.Chart(metrics_long)
    .mark_bar()
    .encode(
        x=alt.X("Model:N", title="Model"),
        xOffset="Metric:N",
        y=alt.Y("Score:Q", title="Score"),
        color=alt.Color("Metric:N", title="Metric"),
        tooltip=["Model", "Metric", "Score"]
    )
    .properties(height=400)
)

st.altair_chart(comparison_chart, use_container_width=True)

st.markdown("---")

# ===============================
# 9. FEATURE IMPORTANCE GRAPH
#    Proper horizontal bars
# ===============================
st.subheader("Feature Importance Graph")

if hasattr(model, "feature_importances_"):
    feature_df = pd.DataFrame({
        "Feature": ["Mileage", "Quantity_Used", "Estimated_Usage_km", "Remaining_Life_km"],
        "Importance": model.feature_importances_
    })

    feature_chart = (
        alt.Chart(feature_df)
        .mark_bar()
        .encode(
            x=alt.X("Importance:Q", title="Importance"),
            y=alt.Y("Feature:N", sort="-x", title="Feature"),
            tooltip=["Feature", "Importance"]
        )
        .properties(height=300)
    )

    st.altair_chart(feature_chart, use_container_width=True)
else:
    st.warning("Feature importance is not available for this model.")