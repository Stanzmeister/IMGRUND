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
import base64

# Konfiguration
GOOGLE_MAPS_LINK = "https://g.page/r/CYlp_8vxjK6dEBM/review"
WLAN_SSID = "FRIT7.18x 6690"
WLAN_PASSWORD = "3281_3052_8091_6979_1072"
ANDROID_WIFI_LINK = f"https://wifi.example.com/connect?ssid={WLAN_SSID}&password={WLAN_PASSWORD}"
INSTAGRAM_LINK = "https://www.instagram.com/restaurant_imgrund_boeblingen?utm_source=ig_web_button_share_sheet&igsh=ZDNlZDc0MzIxNw=="

# Funktion zum Generieren des WLAN-QR-Codes
def generate_wifi_qr():
    wifi_config = f"WIFI:S:{WLAN_SSID};T:WPA;P:{WLAN_PASSWORD};;"
    qr = qrcode.QRCode()
    qr.add_data(wifi_config)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    
    # Konvertiere PIL Image zu Bytes
    img_byte_arr = io.BytesIO()
    img.save(img_byte_arr, format='PNG')
    img_byte_arr = img_byte_arr.getvalue()
    return img_byte_arr

def set_bg_hack():
    st.markdown(
        """
        <style>
        .stApp {
            background: linear-gradient(rgba(255,255,255,0.9), rgba(255,255,255,0.9));
        }
        .content-container {
            background-color: rgba(255, 255, 255, 0.95);
            border-radius: 10px;
            padding: 2rem;
            box-shadow: 0 4px 8px rgba(0,0,0,0.1);
            margin: 2rem auto;
            max-width: 600px;
            text-align: center;
        }
        .logo-container {
            margin: 0 auto 1.5rem;
            text-align: center;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

# Hauptfunktion der App
def main():
    set_bg_hack()
    
    st.markdown('<div class="content-container">', unsafe_allow_html=True)
    
    # Logo in der Mitte
    st.markdown('<div class="logo-container">', unsafe_allow_html=True)
    try:
        st.image("LOGO_IM_GRUND.png", width=200)  # Stelle sicher, dass die Datei im selben Verzeichnis liegt
    except:
        st.title("🍽️ Restaurant IM GRUND")  # Fallback falls Logo nicht gefunden
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Untertitel unter dem Logo
    st.subheader("Vielen Dank für Ihren Besuch!")
    
    # Instagram-Link mit Angebotshinweis
    st.markdown(
        f"""
        <div style="margin: 1.5rem 0;">
            <a href="{INSTAGRAM_LINK}" target="_blank" style="
                display: inline-block;
                background: linear-gradient(45deg, #f09433, #e6683c, #dc2743, #cc2366, #bc1888);
                color: white;
                padding: 12px 25px;
                border-radius: 30px;
                text-decoration: none;
                font-weight: bold;
                font-size: 18px;
                box-shadow: 0 4px 15px rgba(225, 48, 108, 0.5);
            ">
                @restaurant_im_grund
            </a>
            <p style="font-size: 16px; margin-top: 10px;">
                Verpasse keine Angebote und Geschenke! 🎁
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )
    
    # Auswahl
    choice = st.radio(
        "Möchten Sie uns auf Google Maps bewerten?",
        ("⭐ Ja, gerne!", "📶 Nein, ich möchte nur WLAN nutzen"),
        index=None
    )
    
    if choice == "⭐ Ja, gerne!":
        st.link_button("📝 Bewertung schreiben", GOOGLE_MAPS_LINK)
    elif choice == "📶 Nein, ich möchte nur WLAN nutzen":
        st.subheader("WLAN-Zugang")
        
        col1, col2 = st.columns(2)
        
        with col1:
            qr_img = generate_wifi_qr()
            st.image(qr_img, caption="Scan für WLAN")
        
        with col2:
            if st.button("📋 Passwort kopieren", 
                        help="Klicken, um WLAN-Passwort in die Zwischenablage zu kopieren"):
                pyperclip.copy(WLAN_PASSWORD)
                st.success("Passwort kopiert!")
            
            st.markdown(f"""
                <a href="{ANDROID_WIFI_LINK}" target="_blank">
                    <button style="
                        background: #4CAF50;
                        color: white;
                        border: none;
                        padding: 10px 20px;
                        border-radius: 5px;
                        cursor: pointer;
                        margin-top: 10px;
                        width: 100%;
                    ">
                        🔗 Automatisch verbinden (Android)
                    </button>
                </a>
            """, unsafe_allow_html=True)
            
            st.markdown(f"""
                <div style="margin-top: 15px; font-size: 14px;">
                    <strong>Für iPhone:</strong><br>
                    1. Gehe zu <em>Einstellungen > WLAN</em><br>
                    2. Wähle <strong>{WLAN_SSID}</strong><br>
                    3. Passwort einfügen
                </div>
            """, unsafe_allow_html=True)
    
    st.markdown("</div>", unsafe_allow_html=True)

if __name__ == "__main__":
    main()
