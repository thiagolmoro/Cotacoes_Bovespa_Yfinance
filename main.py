# pip install yfinance

import yfinance as yf
import time
import os

# Lista de papéis a monitorar
tickers = [
    "ABEV3.SA", "ALPA4.SA", "AMER3.SA", "ASAI3.SA", "AZUL4.SA", "B3SA3.SA", "BBAS3.SA", "BBDC3.SA", "BBDC4.SA",
    "BBSE3.SA", "BEEF3.SA", "BPAC11.SA", "BPAN4.SA", "BRAP4.SA", "BRFS3.SA", "BRKM5.SA", "CASH3.SA", "CCRO3.SA",
    "CMIG4.SA", "CMIN3.SA", "COGN3.SA", "CPFE3.SA", "CPLE6.SA", "CRFB3.SA", "CSAN3.SA", "CSNA3.SA", "CVCB3.SA",
    "CYRE3.SA", "DXCO3.SA", "ECOR3.SA", "EGIE3.SA", "ELET3.SA", "ELET6.SA", "EMBR3.SA", "ENEV3.SA", "ENGI11.SA",
    "EQTL3.SA", "EZTC3.SA", "FLRY3.SA", "GGBR4.SA", "GOAU4.SA", "GOLL4.SA", "HAPV3.SA", "HYPE3.SA", "IGTI11.SA",
    "IRBR3.SA", "ITSA4.SA", "ITUB4.SA", "JBSS3.SA", "JHSF3.SA", "KLBN11.SA", "LREN3.SA", "LWSA3.SA", "MGLU3.SA",
    "MRFG3.SA", "MRVE3.SA", "MULT3.SA", "NTCO3.SA", "PCAR3.SA", "PETR3.SA", "PETR4.SA", "PETZ3.SA", "POSI3.SA",
    "PRIO3.SA", "QUAL3.SA", "RADL3.SA", "RAIL3.SA", "RDOR3.SA", "RENT3.SA", "SANB11.SA", "SBSP3.SA", "SUZB3.SA",
    "TAEE11.SA", "TIMS3.SA", "TOTS3.SA", "UGPA3.SA", "USIM5.SA", "VALE3.SA", "VBBR3.SA", "VIVT3.SA", "WEGE3.SA",
    "YDUQ3.SA"
]

def fetch_quotes():
    """Função para buscar as cotações em tempo real."""
    data = yf.download(tickers, period="1d", interval="1m", group_by="ticker", progress=False)
    quotes = {}
    for ticker in tickers:
        if ticker in data:
            quotes[ticker] = data[ticker]["Close"].iloc[-1]
    return quotes

def display_quotes(quotes):
    """Exibe as cotações de forma formatada."""
    os.system("cls" if os.name == "nt" else "clear")  # Limpa o terminal (Windows: cls | Linux/Mac: clear)
    print("Cotações com atraso de 15 minutos:\n")
    for ticker, price in quotes.items():
        print(f"{ticker}: R$ {price:.2f}")

if __name__ == "__main__":
    print("Monitorando cotações (pressione Ctrl+C para parar)...")
    try:
        while True:
            quotes = fetch_quotes()
            display_quotes(quotes)
            time.sleep(2)  # Atualiza a cada 2 segundos
    except KeyboardInterrupt:
        print("\nMonitoramento encerrado.")