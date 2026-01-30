import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Movies & Web Series Ratings",
    layout="wide"
)

st.markdown(
    """
    <style>
    .stApp {
        background-color: #0E1117;
        color: white;
    }
    </style>
    """,
    unsafe_allow_html=True
)
data = [
# ================= MOVIES =================

# -------- HOLLYWOOD (30) --------
("Oppenheimer","Hollywood Movie",8.6),
("Barbie","Hollywood Movie",7.0),
("Dune: Part Two","Hollywood Movie",8.7),
("Avatar: The Way of Water","Hollywood Movie",7.6),
("John Wick 4","Hollywood Movie",7.8),
("The Batman","Hollywood Movie",7.9),
("Top Gun: Maverick","Hollywood Movie",8.3),
("Spider-Man: No Way Home","Hollywood Movie",8.2),
("Everything Everywhere All at Once","Hollywood Movie",8.0),
("Interstellar","Hollywood Movie",8.6),
("Joker","Hollywood Movie",8.4),
("Tenet","Hollywood Movie",7.4),
("Killers of the Flower Moon","Hollywood Movie",8.1),
("Mission Impossible Dead Reckoning","Hollywood Movie",7.7),
("Guardians of the Galaxy Vol.3","Hollywood Movie",8.1),
("No Time To Die","Hollywood Movie",7.3),
("Bullet Train","Hollywood Movie",7.3),
("Glass Onion","Hollywood Movie",7.4),
("Elvis","Hollywood Movie",7.4),
("Wonka","Hollywood Movie",7.1),
("The Menu","Hollywood Movie",7.3),
("A Quiet Place Part II","Hollywood Movie",7.2),
("Dunkirk","Hollywood Movie",7.9),
("1917","Hollywood Movie",8.2),
("Ford vs Ferrari","Hollywood Movie",8.1),
("Free Guy","Hollywood Movie",7.1),
("Smile","Hollywood Movie",6.5),
("The Creator","Hollywood Movie",7.2),
("Napoleon","Hollywood Movie",6.9),
("The Whale","Hollywood Movie",7.8),

# -------- BOLLYWOOD (30) --------
("12th Fail","Bollywood Movie",8.9),
("Jawan","Bollywood Movie",7.0),
("Animal","Bollywood Movie",6.7),
("Dunki","Bollywood Movie",6.8),
("Pathaan","Bollywood Movie",5.9),
("Drishyam 2","Bollywood Movie",8.2),
("KGF Chapter 2","Bollywood Movie",8.3),
("Shershaah","Bollywood Movie",8.4),
("Gangubai Kathiawadi","Bollywood Movie",7.0),
("Tiger 3","Bollywood Movie",6.4),
("Rocky Aur Rani","Bollywood Movie",6.9),
("Gadar 2","Bollywood Movie",6.1),
("83","Bollywood Movie",7.5),
("Uri","Bollywood Movie",8.2),
("Sardar Udham","Bollywood Movie",8.4),
("Ludo","Bollywood Movie",7.6),
("Chhichhore","Bollywood Movie",8.0),
("Andhadhun","Bollywood Movie",8.3),
("Kabir Singh","Bollywood Movie",7.1),
("Dangal","Bollywood Movie",8.4),
("Kesari","Bollywood Movie",7.4),
("Tanhaji","Bollywood Movie",7.6),
("OMG 2","Bollywood Movie",7.6),
("Brahmastra","Bollywood Movie",5.6),
("Bhool Bhulaiyaa 2","Bollywood Movie",6.3),
("Raazi","Bollywood Movie",7.8),
("Article 15","Bollywood Movie",8.1),
("Pink","Bollywood Movie",8.1),
("Queen","Bollywood Movie",8.1),
("Sanju","Bollywood Movie",7.7),

# -------- TOLLYWOOD (30) --------
("RRR","Tollywood Movie",8.8),
("Baahubali: The Beginning","Tollywood Movie",8.0),
("Baahubali 2","Tollywood Movie",8.2),
("Pushpa: The Rise","Tollywood Movie",7.6),
("Salaar","Tollywood Movie",6.6),
("Kalki 2898 AD","Tollywood Movie",7.5),
("Sita Ramam","Tollywood Movie",8.6),
("Jersey","Tollywood Movie",8.5),
("Rangasthalam","Tollywood Movie",8.4),
("Major","Tollywood Movie",8.1),
("Hi Nanna","Tollywood Movie",8.2),
("Eega","Tollywood Movie",7.8),
("Ala Vaikunta Puramulo","Tollywood Movie",7.3),
("Athadu","Tollywood Movie",8.2),
("Pokiri","Tollywood Movie",7.9),
("Arjun Reddy","Tollywood Movie",8.0),
("Goodachari","Tollywood Movie",7.9),
("Agent Sai Srinivasa Athreya","Tollywood Movie",8.4),
("Ye Maaya Chesave","Tollywood Movie",7.7),
("Bichagadu","Tollywood Movie",8.0),
("Leader","Tollywood Movie",7.9),
("Tagore","Tollywood Movie",7.4),
("Khaleja","Tollywood Movie",7.6),
("Gabbar Singh","Tollywood Movie",7.1),
("Dasara","Tollywood Movie",6.9),
("Brochevarevarura","Tollywood Movie",8.0),
("Evaru","Tollywood Movie",8.1),
("Maharshi","Tollywood Movie",7.1),
("Janatha Garage","Tollywood Movie",7.2),
("Magadheera","Tollywood Movie",7.7),

# ================= WEB SERIES (30) =================
("Breaking Bad","Web Series",9.5),
("Game of Thrones","Web Series",9.2),
("Stranger Things","Web Series",8.7),
("The Boys","Web Series",8.7),
("Money Heist","Web Series",8.2),
("The Last of Us","Web Series",8.8),
("Chernobyl","Web Series",9.4),
("Dark","Web Series",8.8),
("Peaky Blinders","Web Series",8.8),
("The Walking Dead","Web Series",8.1),
("House of the Dragon","Web Series",8.5),
("Narcos","Web Series",8.8),
("The Witcher","Web Series",8.0),
("Vikings","Web Series",8.5),
("Loki","Web Series",8.2),
("Wednesday","Web Series",8.1),
("Friends","Web Series",8.9),
("The Office","Web Series",9.0),
("Better Call Saul","Web Series",8.9),
("Squid Game","Web Series",8.0),
("The Mandalorian","Web Series",8.7),
("Sherlock","Web Series",9.1),
("Black Mirror","Web Series",8.8),
("Mirzapur","Web Series",8.4),
("Sacred Games","Web Series",8.6),
("Panchayat","Web Series",8.9),
("Asur","Web Series",8.5),
("The Crown","Web Series",8.6),
("Ozark","Web Series",8.5),
("The Night Manager","Web Series",8.6),
]

df = pd.DataFrame(data, columns=["Title", "Category", "Rating"])

st.title("🎬 Movies & Web Series Ratings")
st.dataframe(df)

st.subheader("📊 Ratings Chart")
st.bar_chart(df.set_index("Title")["Rating"])