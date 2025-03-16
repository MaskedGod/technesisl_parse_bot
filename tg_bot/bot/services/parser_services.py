import requests
from bs4 import BeautifulSoup
import sqlite3

DB_PATH = "db.sqlite"


def parse_price(url, xpath):
    """Парсинг цены с сайта."""
    try:
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.content, "lxml")
        price_element = soup.find(xpath)
        if price_element:
            price = price_element.text.strip()
            return clean_price(price)
        return None
    except Exception as e:
        print(f"Ошибка при парсинге {url}: {e}")
        return None


def clean_price(price_str):
    """Очистка цены от лишних символов."""
    import re

    return float(re.sub(r"[^\d.,]", "", price_str).replace(",", "."))


def parse_prices():
    """Вычисление средних цен."""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("SELECT title, url, xpath FROM products")
    rows = cursor.fetchall()
    conn.close()

    results = []
    for title, url, xpath in rows:
        price = parse_price(url, xpath)
        if price:
            results.append((title, price))

    if results:
        avg_prices = {}
        for title, price in results:
            if title not in avg_prices:
                avg_prices[title] = []
            avg_prices[title].append(price)

        response = "Средние цены:\n"
        for title, prices in avg_prices.items():
            avg_price = sum(prices) / len(prices)
            response += f"{title}: {avg_price:.2f}\n"
        return response
    else:
        return "Не удалось найти цены."
