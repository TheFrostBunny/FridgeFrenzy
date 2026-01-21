import customtkinter as ctk
import random

Cooking_Styles = [
    "Grilled",
    "Baked",
    "Fried",
    "Steamed",
    "Roasted"
]

Flavor_Twists = [
    "with a spicy kick",
    "drizzled with honey",
    "topped with fresh herbs",
    "served with a tangy sauce",
    "garnished with citrus zest"
]

Dish_Names = [
    "Supreme Chicken",
    "Veggie Delight",
    "Seafood Platter",
    "Pasta Primavera",
    "Hearty Beef Stew"
]

app = ctk.CTk()
app.geometry("400x300")
app.title("Bizarre Recipe GUI")
app.iconbitmap("logo.ico")


label = ctk.CTkLabel(app, text="Welcome to the Bizarre Recipe Generator!")
label.pack(pady=20)

ctk.CTkLabel(app, text="Enter ingredients (comma-separated):").pack()
entry = ctk.CTkEntry(app, width=300)
entry.pack(pady=10)

text_box = ctk.CTkTextbox(app, width=350, height=100)
text_box.pack(pady=10)

def generate_recipe(ingredients):
    style = random.choice(Cooking_Styles)
    twist = random.choice(Flavor_Twists)
    dish = random.choice(Dish_Names)
    chosen = random.sample(ingredients, k=min(3, len(ingredients)))

    return (
        f"🍽️ Today's Recipe: {dish}\n\n"
        f"Take your {', '.join(chosen)} and prepare them in a {style} style, {twist}.\n"
        f"Then serve hot and enjoy your meal!\n"
        f"Happy Cooking! 🍳"
    )

def generate():
    ingredients = [item.strip() for item in entry.get().split(",") if item.strip()]
    text_box.delete("0.0", "end")

    if not ingredients:
        text_box.insert("0.0", "⚠️ Please enter at least one ingredient!")
        return

    recipe = generate_recipe(ingredients)
    text_box.insert("0.0", recipe)

def setup_gui():
    app = ctk.CTk()
    app.geometry("450x400")
    app.title("🥪 Bizarre Recipe Generator")
    app.resizable(False, False)
    try:
        app.iconbitmap("logo.ico")
    except:
        pass

    title_label = ctk.CTkLabel(app, text="Welcome to the Bizarre Recipe Generator!", font=("Arial", 16, "bold"))
    title_label.pack(pady=(20,10))

    ctk.CTkLabel(app, text="Enter ingredients (comma-separated):").pack(pady=(5,0))
    global entry
    entry = ctk.CTkEntry(app, width=350)
    entry.pack(pady=10)

    global text_box
    text_box = ctk.CTkTextbox(app, width=400, height=150)
    text_box.pack(pady=10)

    generate_btn = ctk.CTkButton(app, text="Generate Recipe 🤪", command=generate)
    generate_btn.pack(pady=10)

    return app

if __name__ == "__main__":
    app = setup_gui()
    app.mainloop()

