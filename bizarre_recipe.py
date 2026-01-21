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

def generate_recipe(ingredients):
    style = random.choice(Cooking_Styles)
    twist = random.choice(Flavor_Twists)
    dish = random.choice(Dish_Names)

    chosen = random.sample(ingredients, k=min(3, len(ingredients)))

    recipe = f"""
🍽️ Today's Recipe: **{dish}**

Take your {', '.join(chosen)} and prepare them in a {style} style, {twist}.
Then serve hot and enjoy your meal!

Happy Cooking! 🍳
"""
    return recipe


def main():
    print("Welcome to the Bizarre Recipe Generator!")
    print("Enter what you have in your kitchen (comma-separated):")

    items = input("> ")
    ingredients = [item.strip() for item in items.split(",") if item.strip()]

    if not ingredients:
        print("You need to provide at least one ingredient!")
        return

    recipe = generate_recipe(ingredients)
    print(recipe)

if __name__ == "__main__":
    main()