# -*- coding: utf-8 -*-
"""
Created on Wed Jun 25 00:20:43 2025

@author: Lenovo
"""

import streamlit as st
import qrcode
from PIL import Image
import io
import pyperclip

# Konfiguration
GOOGLE_MAPS_LINK = "https://g.page/r/CYlp_8vxjK6dEBM/review"
WLAN_SSID = "FRIT7.18x 6690"
WLAN_PASSWORD = "3281_3052_8091_6979_1072"
ANDROID_WIFI_LINK = f"https://wifi.example.com/connect?ssid={WLAN_SSID}&password={WLAN_PASSWORD}"
INSTAGRAM_LINK = "https://www.instagram.com/restaurant_imgrund_boeblingen"

def generate_wifi_qr():
    wifi_config = f"WIFI:S:{WLAN_SSID};T:WPA;P:{WLAN_PASSWORD};;"
    qr = qrcode.QRCode()
    qr.add_data(wifi_config)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    img_byte_arr = io.BytesIO()
    img.save(img_byte_arr, format='PNG')
    return img_byte_arr.getvalue()

def main():
    # Custom CSS für Zentrierung
    st.markdown("""
    <style>
    .main-container {
        display: flex;
        flex-direction: column;
        align-items: center;
        text-align: center;
        max-width: 600px;
        margin: 0 auto;
        padding: 20px;
    }
    .logo-container {
        margin-bottom: 20px;
    }
    .instagram-container {
        margin: 25px 0;
        width: 100%;
    }
    .instagram-button {
        background: linear-gradient(45deg, #f09433, #e6683c, #dc2743, #cc2366, #bc1888);
        color: white !important;
        border: none;
        padding: 12px 30px;
        border-radius: 30px;
        font-size: 18px;
        font-weight: bold;
        margin: 10px 0;
        cursor: pointer;
        box-shadow: 0 4px 15px rgba(225, 48, 108, 0.3);
        text-decoration: none;
        display: inline-block;
    }
    </style>
    """, unsafe_allow_html=True)
    
    # Hauptcontainer
    st.markdown('<div class="main-container">', unsafe_allow_html=True)
    
    # Logo-Bereich (zentriert)
    st.markdown('<div class="logo-container">', unsafe_allow_html=True)
    try:
        st.image("LOGO_IM_GRUND.png", width=200, use_container_width=False)
    except:
        st.title("🍽️ Restaurant IM GRUND")
    st.subheader("Vielen Dank für Ihren Besuch!")
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Instagram-Bereich (zentriert)
    st.markdown('<div class="instagram-container">', unsafe_allow_html=True)
    st.markdown(
        f'<a href="{INSTAGRAM_LINK}" target="_blank" class="instagram-button">Folge uns auf Instagram</a>',
        unsafe_allow_html=True
    )
    st.markdown("Verpasse keine Angebote und Geschenke! 🎁")
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Auswahl-Bereich
    choice = st.radio(
        "Möchten Sie uns auf Google Maps bewerten?",
        ("⭐ Ja, gerne!", "📶 Nein, ich möchte nur WLAN nutzen"),
        index=None
    )
    
    # Bewertungsoption
    if choice == "⭐ Ja, gerne!":
        st.link_button("📝 Bewertung schreiben", GOOGLE_MAPS_LINK)
    
    # WLAN-Option
    elif choice == "📶 Nein, ich möchte nur WLAN nutzen":
        st.subheader("WLAN-Zugang")
        col1, col2 = st.columns(2)
        
        with col1:
            st.image(generate_wifi_qr(), caption="Scan für WLAN", use_container_width=True)
        
        with col2:
            if st.button("📋 Passwort kopieren"):
                pyperclip.copy(WLAN_PASSWORD)
                st.success("Kopiert!")
            
            st.markdown(f"""
                <a href="{ANDROID_WIFI_LINK}" style="text-decoration:none">
                    <button style="
                        background:#4CAF50; color:white; border:none;
                        padding:10px; border-radius:5px; margin-top:10px;
                        width:100%; cursor:pointer">
                        🔗 Auto-Connect (Android)
                    </button>
                </a>
            """, unsafe_allow_html=True)
            
            st.markdown(f"""
                <div style="font-size:14px; margin-top:15px; text-align:left">
                    <strong>Für iPhone:</strong><br>
                    1. Einstellungen > WLAN<br>
                    2. {WLAN_SSID} wählen<br>
                    3. Passwort einfügen
                </div>
            """, unsafe_allow_html=True)
    
    st.markdown('</div>', unsafe_allow_html=True)  # Ende main-container

if __name__ == "__main__":
    main()
