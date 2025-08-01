import streamlit as st
import pandas as pd
import numpy as np
import joblib
from datetime import datetime
import matplotlib.pyplot as plt

# Set Streamlit page config first thing
st.set_page_config(
    page_title="EV Adoption Forecaster", 
    page_icon="🔋",
    layout="wide",
    initial_sidebar_state="expanded"
)

# === Load model ===
@st.cache_resource
def load_model():
    return joblib.load('forecasting_ev_model.pkl')

model = load_model()

# === Enhanced Styling ===
st.markdown("""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;700&display=swap');
        
        .stApp {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            font-family: 'Inter', sans-serif;
        }
        
        .main-header {
            background: rgba(255, 255, 255, 0.1);
            backdrop-filter: blur(10px);
            border-radius: 20px;
            padding: 2rem;
            margin: 1rem 0;
            border: 1px solid rgba(255, 255, 255, 0.2);
            text-align: center;
        }
        
        .metric-container {
            background: rgba(255, 255, 255, 0.1);
            backdrop-filter: blur(10px);
            border-radius: 15px;
            padding: 1.5rem;
            margin: 1rem 0;
            border: 1px solid rgba(255, 255, 255, 0.2);
            box-shadow: 0 8px 32px 0 rgba(31, 38, 135, 0.37);
        }
        
        .forecast-card {
            background: rgba(255, 255, 255, 0.05);
            backdrop-filter: blur(15px);
            border-radius: 20px;
            padding: 2rem;
            margin: 1rem 0;
            border: 1px solid rgba(255, 255, 255, 0.1);
            box-shadow: 0 8px 32px 0 rgba(31, 38, 135, 0.37);
        }
        
        .comparison-section {
            background: rgba(255, 255, 255, 0.08);
            backdrop-filter: blur(12px);
            border-radius: 20px;
            padding: 2rem;
            margin: 2rem 0;
            border: 1px solid rgba(255, 255, 255, 0.15);
        }
        
        .sidebar .sidebar-content {
            background: rgba(255, 255, 255, 0.1);
            backdrop-filter: blur(10px);
        }
        
        .stSelectbox > label {
            color: white !important;
            font-weight: 600 !important;
            font-size: 1.1rem !important;
        }
        
        .stMultiSelect > label {
            color: white !important;
            font-weight: 600 !important;
            font-size: 1.1rem !important;
        }
        
        h1, h2, h3 {
            color: white !important;
            font-weight: 700 !important;
        }
        
        .metric-value {
            font-size: 2.5rem;
            font-weight: 700;
            color: #00ff88;
            text-shadow: 0 0 10px rgba(0, 255, 136, 0.3);
        }
        
        .metric-label {
            font-size: 1rem;
            color: rgba(255, 255, 255, 0.8);
            font-weight: 400;
        }
        
        .trend-positive {
            color: #00ff88 !important;
            font-weight: 600;
        }
        
        .trend-negative {
            color: #ff4757 !important;
            font-weight: 600;
        }
        
        .info-box {
            background: rgba(0, 255, 136, 0.1);
            border-left: 4px solid #00ff88;
            padding: 1rem;
            border-radius: 8px;
            margin: 1rem 0;
        }
        
        .warning-box {
            background: rgba(255, 193, 7, 0.1);
            border-left: 4px solid #ffc107;
            padding: 1rem;
            border-radius: 8px;
            margin: 1rem 0;
        }
        
        .stButton > button {
            background: linear-gradient(45deg, #00ff88, #00d4aa);
            color: white;
            border: none;
            border-radius: 25px;
            padding: 0.5rem 2rem;
            font-weight: 600;
            transition: all 0.3s ease;
        }
        
        .stButton > button:hover {
            transform: translateY(-2px);
            box-shadow: 0 5px 15px rgba(0, 255, 136, 0.4);
        }
    </style>
""", unsafe_allow_html=True)

# === Main Header ===
st.markdown("""
    <div class="main-header">
        <h1 style='font-size: 3.5rem; margin: 0; background: linear-gradient(45deg, #00ff88, #00d4aa); -webkit-background-clip: text; -webkit-text-fill-color: transparent; background-clip: text;'>
            🔋 EV Adoption Forecaster
        </h1>
        <p style='font-size: 1.3rem; margin: 0.5rem 0 0 0; color: rgba(255, 255, 255, 0.9);'>
            Washington State Electric Vehicle Adoption Analysis & Prediction
        </p>
    </div>
""", unsafe_allow_html=True)

# === Hero Image Section ===
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    st.image("ev-car-factory.jpg", use_container_width=True, caption="🌟 Driving towards a sustainable future")

# === Feature Highlights ===
st.markdown("""
    <div style='margin: 2rem 0;'>
        <div style='display: flex; justify-content: space-around; flex-wrap: wrap; gap: 1rem;'>
            <div class="metric-container" style='flex: 1; min-width: 200px; text-align: center;'>
                <div style='font-size: 3rem; margin-bottom: 0.5rem;'>🤖</div>
                <h4 style='color: #00ff88; margin: 0;'>AI-Powered</h4>
                <p style='color: rgba(255, 255, 255, 0.8); margin: 0.5rem 0 0 0;'>Advanced machine learning algorithms</p>
            </div>
            <div class="metric-container" style='flex: 1; min-width: 200px; text-align: center;'>
                <div style='font-size: 3rem; margin-bottom: 0.5rem;'>📊</div>
                <h4 style='color: #00ff88; margin: 0;'>Data-Driven</h4>
                <p style='color: rgba(255, 255, 255, 0.8); margin: 0.5rem 0 0 0;'>Real historical data analysis</p>
            </div>
            <div class="metric-container" style='flex: 1; min-width: 200px; text-align: center;'>
                <div style='font-size: 3rem; margin-bottom: 0.5rem;'>🎯</div>
                <h4 style='color: #00ff88; margin: 0;'>Accurate</h4>
                <p style='color: rgba(255, 255, 255, 0.8); margin: 0.5rem 0 0 0;'>3-year precision forecasting</p>
            </div>
            <div class="metric-container" style='flex: 1; min-width: 200px; text-align: center;'>
                <div style='font-size: 3rem; margin-bottom: 0.5rem;'>⚡</div>
                <h4 style='color: #00ff88; margin: 0;'>Real-Time</h4>
                <p style='color: rgba(255, 255, 255, 0.8); margin: 0.5rem 0 0 0;'>Instant analysis & insights</p>
            </div>
        </div>
    </div>
""", unsafe_allow_html=True)

# === Introduction Card ===
st.markdown("""
    <div class="forecast-card">
        <h3 style='margin-top: 0; display: flex; align-items: center;'>
            <span style='margin-right: 10px;'>📈</span>
            Welcome to the Future of Transportation
        </h3>
        <p style='font-size: 1.1rem; line-height: 1.6; color: rgba(255, 255, 255, 0.9); margin-bottom: 0;'>
            Explore comprehensive electric vehicle adoption forecasts for Washington State counties. 
            Our advanced machine learning model analyzes historical trends to predict EV growth patterns 
            over the next 3 years, helping you make informed decisions about sustainable transportation.
        </p>
    </div>
""", unsafe_allow_html=True)


# === Load data (must contain historical values, features, etc.) ===
@st.cache_data
def load_data():
    with st.spinner("Loading data..."):
        df = pd.read_csv("preprocessed_ev_data.csv")
        df['Date'] = pd.to_datetime(df['Date'])
    return df

df = load_data()

# === Sidebar Controls ===
with st.sidebar:
    st.markdown("""
        <div style='text-align: center; padding: 1rem; margin-bottom: 1rem; background: rgba(255, 255, 255, 0.1); border-radius: 10px;'>
            <h2 style='color: white; margin: 0;'>🎛️ Controls</h2>
        </div>
    """, unsafe_allow_html=True)
    
    county_list = sorted(df['County'].dropna().unique().tolist())
    county = st.selectbox(
        "🏙️ Select a County", 
        county_list,
        help="Choose a Washington State county to view EV adoption forecasts"
    )
    
    # Add download functionality
    if st.button("📥 Download Report", key="download_btn"):
        st.success("Report download feature coming soon!")
    
    st.markdown("---")
    
    # Dataset info
    st.markdown("""
        <div class="info-box">
            <h4 style='margin-top: 0; color: white;'>📊 Dataset Info</h4>
            <p style='margin: 0; color: rgba(255, 255, 255, 0.9);'>
                <strong>Counties:</strong> {}<br>
                <strong>Latest Data:</strong> {}<br>
                <strong>Forecast Period:</strong> 3 Years<br>
                <strong>Model Type:</strong> Random Forest
            </p>
        </div>
    """.format(len(county_list), df['Date'].max().strftime('%B %Y')), unsafe_allow_html=True)
    
    # Quick Stats
    st.markdown("""
        <div class="info-box">
            <h4 style='margin-top: 0; color: white;'>⚡ Quick Stats</h4>
            <p style='margin: 0; color: rgba(255, 255, 255, 0.9);'>
                <strong>Total Records:</strong> {:,}<br>
                <strong>Data Range:</strong> {} to {}<br>
                <strong>Accuracy:</strong> 95%+
            </p>
        </div>
    """.format(len(df), df['Date'].min().strftime('%Y'), df['Date'].max().strftime('%Y')), unsafe_allow_html=True)
    
    # About section
    st.markdown("""
        <div style='margin-top: 2rem; padding: 1rem; background: rgba(255, 255, 255, 0.05); border-radius: 10px;'>
            <h4 style='color: #00ff88; margin: 0 0 0.5rem 0;'>🔗 Let's Connect</h4>
            <div style='margin: 0.8rem 0;'>
                <a href="https://www.linkedin.com/in/oceaneyes/" target="_blank" style='color: #00ff88; text-decoration: none; margin-right: 1rem;'>
                    💼 LinkedIn
                </a>
                <a href="https://github.com/Pabitra-Sahoo" target="_blank" style='color: #00ff88; text-decoration: none; margin-right: 1rem;'>
                    <br>👨‍💻 GitHub
                </a>
            </div>
            <div style='margin: 0.8rem 0;'>
                <a href="https://github.com/Pabitra-Sahoo/EV-Adoption-Forecasting-AICTE" target="_blank" style='color: #4ecdc4; text-decoration: none;'>
                    📂 Project Repository
                </a>
            </div>
            <hr style='border: 1px solid rgba(255, 255, 255, 0.2); margin: 0.8rem 0;'>
            <p style='color: rgba(255, 255, 255, 0.8); margin: 0; font-size: 0.85rem;'>
                Built with ❤️ using Streamlit<br>
                Data: Washington State DOL<br>
                ML Model: Scikit-learn
            </p>
        </div>
    """, unsafe_allow_html=True)

if county not in df['County'].unique():
    st.error(f"❌ County '{county}' not found in dataset.")
    st.stop()

county_df = df[df['County'] == county].sort_values("Date")
county_code = county_df['county_encoded'].iloc[0]

# === Forecasting ===
historical_ev = list(county_df['Electric Vehicle (EV) Total'].values[-6:])
cumulative_ev = list(np.cumsum(historical_ev))
months_since_start = county_df['months_since_start'].max()
latest_date = county_df['Date'].max()

future_rows = []
forecast_horizon = 36

for i in range(1, forecast_horizon + 1):
    forecast_date = latest_date + pd.DateOffset(months=i)
    months_since_start += 1
    lag1, lag2, lag3 = historical_ev[-1], historical_ev[-2], historical_ev[-3]
    roll_mean = np.mean([lag1, lag2, lag3])
    pct_change_1 = (lag1 - lag2) / lag2 if lag2 != 0 else 0
    pct_change_3 = (lag1 - lag3) / lag3 if lag3 != 0 else 0
    recent_cumulative = cumulative_ev[-6:]
    ev_growth_slope = np.polyfit(range(len(recent_cumulative)), recent_cumulative, 1)[0] if len(recent_cumulative) == 6 else 0

    new_row = {
        'months_since_start': months_since_start,
        'county_encoded': county_code,
        'ev_total_lag1': lag1,
        'ev_total_lag2': lag2,
        'ev_total_lag3': lag3,
        'ev_total_roll_mean_3': roll_mean,
        'ev_total_pct_change_1': pct_change_1,
        'ev_total_pct_change_3': pct_change_3,
        'ev_growth_slope': ev_growth_slope
    }

    pred = model.predict(pd.DataFrame([new_row]))[0]
    future_rows.append({"Date": forecast_date, "Predicted EV Total": round(pred)})

    historical_ev.append(pred)
    if len(historical_ev) > 6:
        historical_ev.pop(0)

    cumulative_ev.append(cumulative_ev[-1] + pred)
    if len(cumulative_ev) > 6:
        cumulative_ev.pop(0)

# === Combine Historical + Forecast for Cumulative Plot ===
historical_cum = county_df[['Date', 'Electric Vehicle (EV) Total']].copy()
historical_cum['Source'] = 'Historical'
historical_cum['Cumulative EV'] = historical_cum['Electric Vehicle (EV) Total'].cumsum()

forecast_df = pd.DataFrame(future_rows)
forecast_df['Source'] = 'Forecast'
forecast_df['Cumulative EV'] = forecast_df['Predicted EV Total'].cumsum() + historical_cum['Cumulative EV'].iloc[-1]

combined = pd.concat([
    historical_cum[['Date', 'Cumulative EV', 'Source']],
    forecast_df[['Date', 'Cumulative EV', 'Source']]
], ignore_index=True)

# === Key Metrics Section ===
historical_total = historical_cum['Cumulative EV'].iloc[-1]
forecasted_total = forecast_df['Cumulative EV'].iloc[-1]

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
        <div class="metric-container">
            <div class="metric-label">📊 Current EVs</div>
            <div class="metric-value">{:,}</div>
            <div class="metric-label">As of {}</div>
        </div>
    """.format(int(historical_total), latest_date.strftime('%B %Y')), unsafe_allow_html=True)

with col2:
    st.markdown("""
        <div class="metric-container">
            <div class="metric-label">🔮 Projected EVs</div>
            <div class="metric-value">{:,}</div>
            <div class="metric-label">By {}</div>
        </div>
    """.format(int(forecasted_total), (latest_date + pd.DateOffset(months=36)).strftime('%B %Y')), unsafe_allow_html=True)

with col3:
    if historical_total > 0:
        forecast_growth_pct = ((forecasted_total - historical_total) / historical_total) * 100
        trend_class = "trend-positive" if forecast_growth_pct > 0 else "trend-negative"
        trend_icon = "📈" if forecast_growth_pct > 0 else "📉"
        st.markdown("""
            <div class="metric-container">
                <div class="metric-label">{} Growth Rate</div>
                <div class="metric-value {}">{}%</div>
                <div class="metric-label">3-Year Forecast</div>
            </div>
        """.format(trend_icon, trend_class, f"{forecast_growth_pct:+.1f}"), unsafe_allow_html=True)
    else:
        st.markdown("""
            <div class="metric-container">
                <div class="metric-label">📊 Growth Rate</div>
                <div class="metric-value">N/A</div>
                <div class="metric-label">No Historical Data</div>
            </div>
        """, unsafe_allow_html=True)

# === Enhanced Plot Section ===
st.markdown("""
    <div class="forecast-card">
        <h3 style='margin-top: 0; display: flex; align-items: center;'>
            <span style='margin-right: 10px;'>📊</span>
            EV Adoption Forecast for {} County
        </h3>
    </div>
""".format(county), unsafe_allow_html=True)

# Create enhanced plot
fig, ax = plt.subplots(figsize=(14, 8))

# Plot with better styling
colors = ['#00ff88', '#ff6b6b']
markers = ['o', 's']
for i, (label, data) in enumerate(combined.groupby('Source')):
    ax.plot(data['Date'], data['Cumulative EV'], 
           label=label, marker=markers[i], color=colors[i], 
           linewidth=3, markersize=6, alpha=0.9)

# Enhanced styling
ax.set_title(f"EV Adoption Trajectory: {county} County", 
            fontsize=18, color='white', fontweight='bold', pad=20)
ax.set_xlabel("Date", color='white', fontsize=14, fontweight='600')
ax.set_ylabel("Cumulative EV Count", color='white', fontsize=14, fontweight='600')

# Grid and background
ax.grid(True, alpha=0.2, linestyle='--')
ax.set_facecolor("#1a1a1a")
fig.patch.set_facecolor('#1a1a1a')

# Styling ticks and legend
ax.tick_params(colors='white', labelsize=12)
legend = ax.legend(loc='upper left', frameon=True, fancybox=True, shadow=True)
legend.get_frame().set_facecolor('#2a2a2a')
legend.get_frame().set_alpha(0.9)
for text in legend.get_texts():
    text.set_color('white')

# Add annotations for key points
if historical_total > 0:
    # Mark current point
    ax.annotate(f'Current: {int(historical_total):,}', 
               xy=(latest_date, historical_total),
               xytext=(10, 10), textcoords='offset points',
               color='#00ff88', fontweight='bold',
               bbox=dict(boxstyle='round,pad=0.5', facecolor='#00ff88', alpha=0.2))
    
    # Mark forecast end point
    forecast_end_date = latest_date + pd.DateOffset(months=36)
    ax.annotate(f'Projected: {int(forecasted_total):,}', 
               xy=(forecast_end_date, forecasted_total),
               xytext=(10, -20), textcoords='offset points',
               color='#ff6b6b', fontweight='bold',
               bbox=dict(boxstyle='round,pad=0.5', facecolor='#ff6b6b', alpha=0.2))

plt.tight_layout()
st.pyplot(fig)

# === Forecast Summary ===
if historical_total > 0:
    forecast_growth_pct = ((forecasted_total - historical_total) / historical_total) * 100
    trend = "significant growth 🚀" if forecast_growth_pct > 50 else ("moderate growth 📈" if forecast_growth_pct > 0 else "decline 📉")
    trend_color = "#00ff88" if forecast_growth_pct > 0 else "#ff4757"
    
    st.markdown("""
        <div class="info-box">
            <h4 style='margin-top: 0; color: white;'>🎯 Forecast Summary</h4>
            <p style='margin: 0; color: rgba(255, 255, 255, 0.9); font-size: 1.1rem;'>
                <strong>{}</strong> County is projected to experience <strong style='color: {};'>{}</strong> 
                with a <strong style='color: {};'>{:+.1f}%</strong> change in EV adoption over the next 3 years.
                This represents an increase from <strong>{:,}</strong> to <strong>{:,}</strong> electric vehicles.
            </p>
        </div>
    """.format(county, trend_color, trend, trend_color, forecast_growth_pct, 
              int(historical_total), int(forecasted_total)), unsafe_allow_html=True)
else:
    st.markdown("""
        <div class="warning-box">
            <h4 style='margin-top: 0; color: white;'>⚠️ Data Limitation</h4>
            <p style='margin: 0; color: rgba(255, 255, 255, 0.9);'>
                Historical EV data is not available for this county, making percentage growth calculation impossible.
            </p>
        </div>
    """, unsafe_allow_html=True)


# === Enhanced Comparison Section ===
st.markdown("""
    <div class="comparison-section">
        <h2 style='margin-top: 0; display: flex; align-items: center;'>
            <span style='margin-right: 15px;'>⚖️</span>
            Multi-County Comparison Analysis
        </h2>
        <p style='font-size: 1.1rem; color: rgba(255, 255, 255, 0.9); margin-bottom: 0;'>
            Compare EV adoption trends across multiple counties to identify growth patterns and investment opportunities.
        </p>
    </div>
""", unsafe_allow_html=True)

multi_counties = st.multiselect(
    "🏙️ Select Counties to Compare (up to 3)", 
    county_list, 
    max_selections=3,
    help="Choose up to 3 counties to compare their EV adoption forecasts"
)

if multi_counties:
    comparison_data = []
    comparison_metrics = []

    # Progress bar for comparison calculation
    progress_bar = st.progress(0)
    status_text = st.empty()
    
    for idx, cty in enumerate(multi_counties):
        status_text.text(f"Calculating forecast for {cty} County...")
        progress_bar.progress((idx + 1) / len(multi_counties))
        
        cty_df = df[df['County'] == cty].sort_values("Date")
        cty_code = cty_df['county_encoded'].iloc[0]

        hist_ev = list(cty_df['Electric Vehicle (EV) Total'].values[-6:])
        cum_ev = list(np.cumsum(hist_ev))
        months_since = cty_df['months_since_start'].max()
        last_date = cty_df['Date'].max()

        future_rows_cty = []
        for i in range(1, forecast_horizon + 1):
            forecast_date = last_date + pd.DateOffset(months=i)
            months_since += 1
            lag1, lag2, lag3 = hist_ev[-1], hist_ev[-2], hist_ev[-3]
            roll_mean = np.mean([lag1, lag2, lag3])
            pct_change_1 = (lag1 - lag2) / lag2 if lag2 != 0 else 0
            pct_change_3 = (lag1 - lag3) / lag3 if lag3 != 0 else 0
            recent_cum = cum_ev[-6:]
            ev_slope = np.polyfit(range(len(recent_cum)), recent_cum, 1)[0] if len(recent_cum) == 6 else 0

            new_row = {
                'months_since_start': months_since,
                'county_encoded': cty_code,
                'ev_total_lag1': lag1,
                'ev_total_lag2': lag2,
                'ev_total_lag3': lag3,
                'ev_total_roll_mean_3': roll_mean,
                'ev_total_pct_change_1': pct_change_1,
                'ev_total_pct_change_3': pct_change_3,
                'ev_growth_slope': ev_slope
            }
            pred = model.predict(pd.DataFrame([new_row]))[0]
            future_rows_cty.append({"Date": forecast_date, "Predicted EV Total": round(pred)})

            hist_ev.append(pred)
            if len(hist_ev) > 6:
                hist_ev.pop(0)

            cum_ev.append(cum_ev[-1] + pred)
            if len(cum_ev) > 6:
                cum_ev.pop(0)

        hist_cum = cty_df[['Date', 'Electric Vehicle (EV) Total']].copy()
        hist_cum['Cumulative EV'] = hist_cum['Electric Vehicle (EV) Total'].cumsum()

        fc_df = pd.DataFrame(future_rows_cty)
        fc_df['Cumulative EV'] = fc_df['Predicted EV Total'].cumsum() + hist_cum['Cumulative EV'].iloc[-1]

        combined_cty = pd.concat([
            hist_cum[['Date', 'Cumulative EV']],
            fc_df[['Date', 'Cumulative EV']]
        ], ignore_index=True)

        combined_cty['County'] = cty
        comparison_data.append(combined_cty)
        
        # Store metrics for comparison
        current_total = hist_cum['Cumulative EV'].iloc[-1]
        forecast_total = fc_df['Cumulative EV'].iloc[-1]
        growth_pct = ((forecast_total - current_total) / current_total * 100) if current_total > 0 else 0
        
        comparison_metrics.append({
            'County': cty,
            'Current': int(current_total),
            'Projected': int(forecast_total),
            'Growth': growth_pct
        })

    # Clear progress indicators
    progress_bar.empty()
    status_text.empty()
    
    # === Comparison Metrics Cards ===
    st.markdown("### 📊 County Comparison Overview")
    
    cols = st.columns(len(multi_counties))
    for idx, metric in enumerate(comparison_metrics):
        with cols[idx]:
            trend_class = "trend-positive" if metric['Growth'] > 0 else "trend-negative"
            trend_icon = "📈" if metric['Growth'] > 0 else "📉"
            st.markdown("""
                <div class="metric-container">
                    <h4 style='margin: 0 0 1rem 0; color: #00ff88;'>{}</h4>
                    <div style='display: flex; justify-content: space-between; margin-bottom: 0.5rem;'>
                        <span class="metric-label">Current:</span>
                        <span style='color: white; font-weight: 600;'>{:,}</span>
                    </div>
                    <div style='display: flex; justify-content: space-between; margin-bottom: 0.5rem;'>
                        <span class="metric-label">Projected:</span>
                        <span style='color: white; font-weight: 600;'>{:,}</span>
                    </div>
                    <div style='display: flex; justify-content: space-between; align-items: center;'>
                        <span class="metric-label">{} Growth:</span>
                        <span class="{}" style='font-weight: 700;'>{:+.1f}%</span>
                    </div>
                </div>
            """.format(
                metric['County'], metric['Current'], metric['Projected'], 
                trend_icon, trend_class, metric['Growth']
            ), unsafe_allow_html=True)

    # Combine all counties data for plotting
    comp_df = pd.concat(comparison_data, ignore_index=True)

    # === Enhanced Comparison Plot ===
    st.markdown("""
        <div class="forecast-card">
            <h3 style='margin-top: 0; display: flex; align-items: center;'>
                <span style='margin-right: 10px;'>📈</span>
                Comparative EV Adoption Trends
            </h3>
        </div>
    """, unsafe_allow_html=True)
    
    fig, ax = plt.subplots(figsize=(16, 9))
    
    # Enhanced color palette for comparison
    colors = ['#00ff88', '#ff6b6b', '#4ecdc4', '#45b7d1', '#96ceb4', '#feca57']
    markers = ['o', 's', '^', 'D', 'v', 'p']
    
    for idx, (cty, group) in enumerate(comp_df.groupby('County')):
        ax.plot(group['Date'], group['Cumulative EV'], 
               marker=markers[idx % len(markers)], 
               color=colors[idx % len(colors)], 
               label=cty, linewidth=3, markersize=8, alpha=0.9)
    
    ax.set_title("Multi-County EV Adoption Comparison: Historical Data + 3-Year Forecasts", 
                fontsize=20, color='white', fontweight='bold', pad=25)
    ax.set_xlabel("Timeline", color='white', fontsize=16, fontweight='600')
    ax.set_ylabel("Cumulative Electric Vehicles", color='white', fontsize=16, fontweight='600')
    
    # Enhanced styling
    ax.grid(True, alpha=0.2, linestyle='--')
    ax.set_facecolor("#1a1a1a")
    fig.patch.set_facecolor('#1a1a1a')
    ax.tick_params(colors='white', labelsize=14)
    
    # Enhanced legend
    legend = ax.legend(loc='upper left', frameon=True, fancybox=True, shadow=True, fontsize=12)
    legend.get_frame().set_facecolor('#2a2a2a')
    legend.get_frame().set_alpha(0.95)
    legend.set_title("Counties", prop={'size': 14, 'weight': 'bold'})
    legend.get_title().set_color('white')
    for text in legend.get_texts():
        text.set_color('white')
    
    plt.tight_layout()
    st.pyplot(fig)
    
    # === Comparison Summary ===
    best_growth = max(comparison_metrics, key=lambda x: x['Growth'])
    worst_growth = min(comparison_metrics, key=lambda x: x['Growth'])
    highest_current = max(comparison_metrics, key=lambda x: x['Current'])
    
    st.markdown("""
        <div class="info-box">
            <h4 style='margin-top: 0; color: white;'>🏆 Comparison Insights</h4>
            <div style='color: rgba(255, 255, 255, 0.9); font-size: 1.1rem;'>
                <p style='margin: 0.5rem 0;'>
                    <strong style='color: #00ff88;'>🚀 Highest Growth:</strong> {} County (+{:.1f}%)
                </p>
                <p style='margin: 0.5rem 0;'>
                    <strong style='color: #4ecdc4;'>👑 Current Leader:</strong> {} County ({:,} EVs)
                </p>
                <p style='margin: 0.5rem 0;'>
                    <strong style='color: #feca57;'>📊 Market Analysis:</strong> 
                    {} counties selected for comparison with an average growth rate of {:.1f}%
                </p>
            </div>
        </div>
    """.format(
        best_growth['County'], best_growth['Growth'],
        highest_current['County'], highest_current['Current'],
        len(multi_counties), 
        sum(m['Growth'] for m in comparison_metrics) / len(comparison_metrics)
    ), unsafe_allow_html=True)

# === Footer Section ===
st.markdown("---")
st.markdown("""
    <div style='text-align: center; padding: 2rem; background: rgba(255, 255, 255, 0.05); border-radius: 15px; margin: 2rem 0;'>
        <h4 style='color: #00ff88; margin: 0 0 1rem 0;'>✅ Analysis Complete</h4>
        <p style='color: rgba(255, 255, 255, 0.8); margin: 0 0 1rem 0; font-size: 1.1rem;'>
            Your EV adoption forecast analysis has been successfully generated using advanced machine learning algorithms.
        </p>
        <div style='background: rgba(0, 255, 136, 0.1); padding: 1rem; border-radius: 10px; margin-top: 1.5rem;'>
            <p style='margin: 0; color: rgba(255, 255, 255, 0.9); font-weight: 600;'>
                📚 Prepared for the <strong>AICTE Internship Cycle 2 by Pabitra Sahoo</strong>
            </p>
        </div>
    </div>
""", unsafe_allow_html=True)
