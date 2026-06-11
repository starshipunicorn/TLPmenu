import streamlit as st

# 🛸 Menu based on Sightings image
menu = {
    "hot drinks": {
        "Earl Grey Tea": 50,
        "Peppermint Tea": 50,
        "Jasmine Green Tea": 50,
        "Orange Ginseng Oolong Tea": 50,
        "Vanilla Chai Latte": 50,
        "Honey Lavender Latter": 50,
        "Cozy Cappuccino": 50,
        "Hot Chocolate": 50
    },
    "cold drinks": {
       "berry hibiscus iced tea": 50,
       "saffron rose iced tea": 50,
       "violet’s colani": 50,
       "iced coffee": 50,
       "horchata": 50,
       "green smoothie": 50
    },
    "mains": {
        "avocado toast w/ fruit salad": 120,
        "steak & pepper omelet w/ hashbrowns": 120,
        "bacon, egg & cheese sandwich": 120,
        "chef salad & soup of the day": 120,
        "caprese sandwich & chips": 120,
        "chicken & waffles": 120
    },
    "dessert": {
       "caramel affogato ice cream": 100,
       "cranberry almond biscotti": 100,
       "tiramisu cheesecake": 100,
       "pie in the sky": 100
    },
    "special item": {
       "little teapot brownie": 250
    },
    "bundles": {
        "Number 1: 10 mains & 10 drinks": 1700,
        "Number 2: 20 mains & 20 drinks": 3400,
        "Number 3: 10 drinks, 6 mains, 4 desserts": 1620,
        "Number 4: 10 drinks, 6 mains, 4 specials": 2220,
        "donut box: cinnamon dolce cronut, strawberry glaze & boston cream": 600
    },
    "extras": {
        "Preservatives": 50
    }
}

# 🧮 Total Calculation Logic
def calculate_total(order, discount=0, fee=0):
    subtotal = sum(menu[cat][item] * qty for (cat, item), qty in order.items())
    discount_amt = subtotal * (discount / 100)
    fee_amt = (subtotal - discount_amt) * (fee / 100)
    total = subtotal - discount_amt + fee_amt
    return round(subtotal, 2), round(total, 2)

# 🌌 App Layout
st.set_page_config(page_title="Little Teapot Calculator", layout="centered")
st.title("☕ LTP Order Calculator 🍵")
st.markdown("_Little Teapot_")

st.sidebar.title("🛠️ Settings")
discount = st.sidebar.slider("Discount (%)", 0, 100, 0)
fee = st.sidebar.slider("Service Fee (%)", 0, 100, 0)

order = {}

# 📱 Mobile-Friendly Expandable Sections
sections_ordered = [
    ("hot drinks", "🥤"),
    ("cold drinks", "🍸"),
    ("mains", "🍲"),
    ("dessert", "🍪"),
    ("special item", "🍯"),
    ("bundles", "🍩"),
    ("extras", "🧪")
]

for section, icon in sections_ordered:
    with st.expander(f"{icon} {section}", expanded=True):
        for item, price in menu[section].items():
            qty = st.number_input(f"{item} (${price})", min_value=0, max_value=500, step=1, key=f"{section}_{item}")
            if qty > 0:
                order[(section, item)] = qty

# 🚀 Calculate Button
if st.button("🚀 Calculate Total"):
    subtotal, total = calculate_total(order, discount, fee)

    st.markdown("---")
    st.markdown(f"### 🌌 Subtotal: **${subtotal}**")
    st.markdown(f"### 💫 Total After Discounts/Fees: **${total}**")

    st.subheader("📦 Order Summary")
    for (cat, item), qty in order.items():
        st.markdown(f"- **{item}** ({cat}) × {qty} @ ${menu[cat][item]} each")
