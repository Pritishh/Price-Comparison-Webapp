import streamlit as st

# Sample data
zomato_prices = {
    "Pizza": {"price": 10, "rating": 4.5, "reviews": ["Delicious!", "Best pizza in town!", "Great value for money."]},
    "Burger": {"price": 5, "rating": 4.0, "reviews": ["Juicy and flavorful.", "Good portion size.", "Could be more crispy."]},
    "Pasta": {"price": 8, "rating": 4.2, "reviews": ["Authentic Italian taste.", "Creamy and satisfying.", "A bit overcooked."]},
}

swiggy_prices = {
    "Pizza": {"price": 9, "rating": 4.3, "reviews": ["Tastes like heaven!", "Quick delivery.", "Slightly cold."]},
    "Burger": {"price": 4.5, "rating": 3.8, "reviews": ["Decent burger.", "Not as expected.", "Could be more filling."]},
    "Pasta": {"price": 7.5, "rating": 4.0, "reviews": ["Delicious sauce.", "Al dente perfection.", "Could use more cheese."]},
}

# Function to compare prices
def compare_prices(food_item):
    zomato_data = zomato_prices.get(food_item)
    swiggy_data = swiggy_prices.get(food_item)

    if zomato_data is None and swiggy_data is None:
        return f"Food item '{food_item}' not found on Zomato or Swiggy."
    elif zomato_data is None:
        return f"Food item '{food_item}' not found on Zomato."
    elif swiggy_data is None:
        return f"Food item '{food_item}' not found on Swiggy."
    else:
        return zomato_data, swiggy_data

# Streamlit app
def main():
    st.title('Food Price and Review Comparison')
    st.write("Welcome to the Food Price and Review Comparison App!")
    st.write("Enter a food item to compare its prices and reviews on Zomato and Swiggy.")
    
    food_item = st.text_input('Food Item')
    
    if st.button('Compare Prices and Reviews'):
        zomato_data, swiggy_data = compare_prices(food_item)
        if isinstance(zomato_data, str) or isinstance(swiggy_data, str):
            st.error("Error: " + zomato_data)
            st.error("Error: " + swiggy_data)
        else:
            st.write(f"Price and review comparison for '{food_item}':")
            st.write("Zomato:")
            st.image("zomato_logo.png", width=150)
            st.write(f"Price: {zomato_data['price']}")
            st.write(f"Rating: {zomato_data['rating']}")
            st.write("Reviews:")
            for review in zomato_data['reviews']:
                st.write(review)
            st.write("Swiggy:")
            st.image("swiggy_logo.png", width=150)
            st.write(f"Price: {swiggy_data['price']}")
            st.write(f"Rating: {swiggy_data['rating']}")
            st.write("Reviews:")
            for review in swiggy_data['reviews']:
                st.write(review)
    
    st.write("Not sure what to search? Check out these popular options:")
    popular_items = ["Pizza", "Burger", "Pasta"]
    for item in popular_items:
        st.write(f"- {item}")

if __name__ == "__main__":
    main()
