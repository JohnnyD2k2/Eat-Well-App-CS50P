import gradio as gr
import pandas as pd

# Load data from csv file
dish = pd.read_csv("healthy_menu.csv")

cart = []

def main():
    display()

def get_appetizers():
    """Return the list of appetizer dish names"""
    return dish[dish["Category"] == "Appetizer"]["Dish Name"].tolist()

def get_main():
    """Return the list of main course dish names"""
    return dish[dish["Category"] == "Main Course"]["Dish Name"].tolist()

def get_desserts():
    """Return the list of dessert dish names"""
    return dish[dish["Category"] == "Dessert"]["Dish Name"].tolist()

def get_info(dish_name):
    """Get info of the dish"""

    item = dish[dish["Dish Name"] == dish_name]

    if item.empty:
        return "⚠ Dish not found :(( Please select a dish to discover more!!"
    item = item.iloc[0]

    return f"""
    ## 🥗 **{dish_name}**
    - **Calories:** {item['Calories (kcal)']} kcal
    - **Protein:** {item['Protein (g)']} g
    - **Price:** {item['Price (VND)']:,} VND
    - **Allergy Info:** {item['Allergy Info']}
    """

def add_to_cart(dish_name):

    """Add food to cart and update cart"""
    if not dish_name:
        return "⚠ Please select a dish to add to cart!!"

    item = dish[dish["Dish Name"] == dish_name]
    if item.empty:
        return "⚠ Dish not found :(( Please select a dish to discover more!!"
    item = item.iloc[0]

    cart.append((dish_name, item['Price (VND)'], item['Calories (kcal)'], item['Protein (g)']))

    total_price = sum(price for _, price, _, _ in cart)
    total_calo = sum(calories for _, _, calories, _ in cart)
    total_pro = sum(protein for _, _, _, protein in cart)

    cart_details = "\n".join([f"- {name}: {price:,} VND" for name, price, _, _ in cart])

    return f"""
## 🛍 **CART:**
{cart_details}

### 💰 Total price: {total_price:,} VND
### 🎯 Total calories: {total_calo:,} kcal
### 🎯 Total protein: {total_pro:,} g"""

def clear_cart():
    """Clear Cart"""
    global cart
    cart.clear()
    return "## 🛒 **EMPTY CART**"


def display():
    """Create interface using gradio"""
    with gr.Blocks() as demo:
        gr.Markdown("## 🍽 **EAT WELL APP**")

        with gr.Row():
            with gr.Column(scale=1):
                gr.Markdown("## ℹ **DETAILS**")
                dish_details = gr.Markdown("## 😋ᵞᵁᴹᴹᵞ😋 **EAT WELL**")
                cart_display = gr.Markdown("## 🛒 **YOUR CART**")
                clear_button = gr.Button("🗑 CLEAR CART")

            with gr.Column(scale=2):
                with gr.Row(scale=1):
                    gr.Markdown("## 𓌉◯𓇋 **MENU**")
                    add_button = gr.Button("➕ ADD TO CART")

                appe_list = gr.Radio(get_appetizers(), label="APPETIZERS")
                main_list = gr.Radio(get_main(), label="MAIN COURSE")
                dss_list = gr.Radio(get_desserts(), label="DESSERTS")

                selected_dish = gr.State()

        # Link function
        # Update selected_dish and dish_details when any radio button is changed
        for dish_list in [appe_list, main_list, dss_list]:
            dish_list.change(lambda x: [x,get_info(x)], dish_list, [selected_dish, dish_details])

        add_button.click(add_to_cart, selected_dish, cart_display)

        clear_button.click(clear_cart, [], cart_display)

    # Launch program
    demo.launch(share=True)


if __name__ == "__main__":
    main()

