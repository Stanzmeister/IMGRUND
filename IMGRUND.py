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
    # CSS mit !important für absolute Kontrolle
    st.markdown("""
    <style>
    /* Zentriert ALLE Elemente */
    [data-testid="stAppViewContainer"] > .main {
        display: flex !important;
        flex-direction: column !important;
        align-items: center !important;
        text-align: center !important;
    }
    
    /* Logo-Container */
    .logo-container {
        margin: 0 auto 1rem auto !important;
        text-align: center !important;
    }
    
    /* Instagram-Bereich */
    .instagram-box {
        margin: 1.5rem auto !important;
        max-width: 300px !important;
    }
    
    /* Radio-Buttons zentrieren */
    [data-testid="stRadio"] > div {
        display: flex !important;
        justify-content: center !important;
    }
    
    /* Buttons zentrieren */
    [data-testid="stButton"] > button {
        margin: 0 auto !important;
    }
    
    /* Spalten-Container für WLAN */
    [data-testid="column"] {
        align-items: center !important;
    }
    </style>
    """, unsafe_allow_html=True)

    # 1. Logo (absolut zentriert)
    with st.container():
        st.markdown('<div class="logo-container">', unsafe_allow_html=True)
        try:
            st.image("LOGO_IM_GRUND.png", width=200, use_container_width=False)
        except:
            st.title("🍽️ Restaurant IM GRUND")
        st.subheader("Vielen Dank für Ihren Besuch!")
        st.markdown('</div>', unsafe_allow_html=True)

    # 2. Instagram-Bereich (perfekt zentriert)
    with st.container():
        st.markdown('<div class="instagram-box">', unsafe_allow_html=True)
        st.markdown(
            f'<a href="{INSTAGRAM_LINK}" target="_blank">'
            '<button style="'
            'background: linear-gradient(45deg, #f09433, #e6683c, #dc2743, #cc2366, #bc1888);'
            'color: white; border: none; padding: 12px 30px; border-radius: 30px;'
            'font-size: 18px; font-weight: bold; margin: 10px 0; cursor: pointer;'
            'box-shadow: 0 4px 15px rgba(225, 48, 108, 0.3);">'
            'Folge uns auf Instagram'
            '</button>'
            '</a>'
            '<p style="margin-top: 8px; font-size: 16px;">'
            'Verpasse keine Angebote und Geschenke! 🎁'
            '</p>',
            unsafe_allow_html=True
        )
        st.markdown('</div>', unsafe_allow_html=True)

    # 3. Auswahl (zentriert)
    choice = st.radio(
        "Möchten Sie uns auf Google Maps bewerten?",
        ("⭐ Ja, gerne!", "📶 Nein, ich möchte nur WLAN nutzen"),
        index=None
    )

    # 4. Aktionen
    if choice == "⭐ Ja, gerne!":
        st.link_button("📝 Bewertung schreiben", GOOGLE_MAPS_LINK)
    
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
                <div style="font-size:14px; margin-top:15px; text-align:left">
                    <strong>Für iPhone:</strong><br>
                    1. Einstellungen > WLAN<br>
                    2. {WLAN_SSID} wählen<br>
                    3. Passwort einfügen
                </div>
            """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()
