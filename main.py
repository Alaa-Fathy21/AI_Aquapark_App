import streamlit as st
import random

def monitor_water_quality():
    return {
        "pH": round(random.uniform(6.5, 8.5), 2),
        "chlorine": round(random.uniform(1.0, 3.0), 2),
        "temperature": round(random.uniform(20, 30), 1)
    }

def optimize_energy_usage(visitor_count):
    base_energy = 1000  # Base energy consumption in kWh
    energy_usage = base_energy + (visitor_count * 10)
    return energy_usage

def visitor_flow_optimization():
    peak_hours = [12, 15, 18]
    current_hour = random.choice(range(24))
    return "High Traffic" if current_hour in peak_hours else "Normal Traffic"

st.title("AI-Powered Aquapark Optimization")

st.sidebar.header("Navigation")
page = st.sidebar.selectbox("Select a Page", ["Home Map", "AI Guide", "Rewards"])

if page == "Home Map":
    st.header("Real-time Park Monitoring")
    water_quality = monitor_water_quality()
    visitor_count = random.randint(100, 1000)
    energy_usage = optimize_energy_usage(visitor_count)
    traffic_status = visitor_flow_optimization()
    
    st.subheader("Water Quality")
    st.write(water_quality)
    
    st.subheader("Energy Usage")
    st.write(f"Current energy usage: {energy_usage} kWh")
    
    st.subheader("Visitor Flow")
    st.write(f"Traffic Status: {traffic_status}")

elif page == "AI Guide":
    st.header("AI Visitor Assistance")
    st.write("\n- Navigate the park easily with AI guidance.")
    st.write("\n- Get eco-tips for sustainable park usage.")
    st.write("\n- Receive crowd alerts to avoid busy areas.")

elif page == "Rewards":
    st.header("Eco-Friendly Rewards Program")
    st.write("Earn loyalty points and discounts for engaging in eco-friendly initiatives!")
    if st.button("Claim Reward"):
        st.success("Reward Claimed! Keep making eco-friendly choices.")
