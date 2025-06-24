# -*- coding: utf-8 -*-
"""
Created on Wed Jun 25 00:20:43 2025

@author: Lenovo
"""

import streamlit as st
import qrcode
from PIL import Image
import io
import base64

# Konfiguration
GOOGLE_MAPS_LINK = "https://g.page/r/CYlp_8vxjK6dEBM/review"
WLAN_SSID = "FRIT7.18x 6690"
WLAN_PASSWORD = "3281_3052_8091_6979_1072"
INSTAGRAM_LINK = "https://www.instagram.com/restaurant_imgrund_boeblingen?utm_source=ig_web_button_share_sheet&igsh=ZDNlZDc0MzIxNw=="  # Hier deinen Instagram-Link eintragen

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

# Funktion für Video-Hintergrund
def set_video_background(video_path):
    # Wir lesen das Video ein und kodieren es im Base64-Format
    with open(video_path, "rb") as video_file:
        video_bytes = video_file.read()
    video_base64 = base64.b64encode(video_bytes).decode('utf-8')
    
    st.markdown(
        f"""
        <style>
        #root > .stApp {{
            position: relative;
        }}
        #root > .stApp:before {{
            content: "";
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            z-index: -1;
            background: linear-gradient(rgba(0,0,0,0.3), rgba(0,0,0,0.3));
        }}
        #video-background {{
            position: fixed;
            right: 0;
            bottom: 0;
            min-width: 100%;
            min-height: 100%;
            width: auto;
            height: auto;
            z-index: -2;
            object-fit: cover;
        }}
        .content-container {{
            background: rgba(255, 255, 255, 0.85);
            border-radius: 15px;
            padding: 25px;
            box-shadow: 0 8px 32px rgba(0,0,0,0.2);
            margin: 20px auto;
            max-width: 600px;
        }}
        </style>
        <video id="video-background" autoplay loop muted playsinline>
            <source src="data:video/mp4;base64,{video_base64}" type="video/mp4">
        </video>
        """,
        unsafe_allow_html=True
    )

# Hauptfunktion der App
def main():
    # Video als Hintergrund setzen
    try:
        set_video_background("essen_vorbestellung.mp4")  # Stelle sicher, dass die Datei im selben Verzeichnis liegt
    except FileNotFoundError:
        # Fallback: Einfarbiger Hintergrund
        st.markdown(
            """
            <style>
            .stApp {
                background: linear-gradient(135deg, #1b5e20 0%, #388e3c 100%);
            }
            </style>
            """,
            unsafe_allow_html=True
        )
    
    # Container für den Inhalt mit weißem Hintergrund
    st.markdown('<div class="content-container">', unsafe_allow_html=True)
    
    st.title("🍽️ Restaurant im Grund")
    st.subheader("Vielen Dank für Ihren Besuch!")
    
    # Instagram-Folgen-Sektion
    st.markdown(
        f"""
        <div style="text-align: center; margin: 25px 0;">
            <h3 style="color: #e1306c;">Folge uns auf Instagram!</h3>
            <p style="font-size: 18px;">Verpasse keine Angebote und Geschenke 🎁</p>
            <a href="{INSTAGRAM_LINK}" target="_blank" style="
                display: inline-block;
                background: linear-gradient(45deg, #f09433, #e6683c, #dc2743, #cc2366, #bc1888);
                color: white;
                padding: 12px 25px;
                border-radius: 30px;
                text-decoration: none;
                font-weight: bold;
                font-size: 18px;
                margin: 15px 0;
                box-shadow: 0 4px 15px rgba(225, 48, 108, 0.5);
                transition: all 0.3s ease;
            ">
                @restaurant_im_grund
            </a>
            <p style="font-size: 16px; margin-top: 10px;">
                Exklusive Angebote für unsere Follower!
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
        st.subheader("WLAN-Zugangsdaten")
        st.code(f"SSID: {WLAN_SSID}\nPasswort: {WLAN_PASSWORD}")
        try:
            with st.spinner('QR-Code wird generiert...'):
                qr_img = generate_wifi_qr()
                st.image(qr_img, caption="Scan für WLAN")
        except Exception as e:
            st.error(f"QR-Code konnte nicht generiert werden: {e}")
            st.code("Bitte nutzen Sie die manuellen WLAN-Daten oben")
    
    # Schließe den content-container div
    st.markdown("</div>", unsafe_allow_html=True)

if __name__ == "__main__":
    main()