import tkinter as tk
import random

# Sample data for flashcards
flashcards = [
    {"English": "Hello", "French": "Bonjour"},
    {"English": "Thank you", "French": "Merci"},
    {"English": "Apple", "French": "Pomme"},
    {"English": "Cat", "French": "Chat"},
    {"English": "House", "French": "Maison"},
    {"English": "Dog", "French": "Chien"},
    {"English": "Flower", "French": "Fleur"},
    {"English": "Book", "French": "Livre"},
    {"English": "Car", "French": "Voiture"},
    {"English": "Tree", "French": "Arbre"},
    {"English": "School", "French": "École"},
    {"English": "Chair", "French": "Chaise"},
    {"English": "Table", "French": "Table"},
    {"English": "Sun", "French": "Soleil"},
    {"English": "Moon", "French": "Lune"},
    {"English": "Star", "French": "Étoile"},
    {"English": "Sky", "French": "Ciel"},
    {"English": "Sea", "French": "Mer"},
    {"English": "Mountain", "French": "Montagne"},
    {"English": "River", "French": "Rivière"},
    {"English": "Forest", "French": "Forêt"},
    {"English": "City", "French": "Ville"},
    {"English": "Village", "French": "Village"},
    {"English": "Bridge", "French": "Pont"},
    {"English": "Street", "French": "Rue"},
    {"English": "Road", "French": "Route"},
    {"English": "Airport", "French": "Aéroport"},
    {"English": "Train station", "French": "Gare"},
    {"English": "Boat", "French": "Bateau"},
    {"English": "Plane", "French": "Avion"},
    {"English": "Bicycle", "French": "Bicyclette"},
    {"English": "Engine", "French": "Moteur"},
    {"English": "Computer", "French": "Ordinateur"},
    {"English": "Phone", "French": "Téléphone"},
    {"English": "Television", "French": "Télévision"},
    {"English": "Radio", "French": "Radio"},
    {"English": "Music", "French": "Musique"},
    {"English": "Movie", "French": "Film"},
    {"English": "Song", "French": "Chanson"},
    {"English": "Art", "French": "Art"},
    {"English": "Painting", "French": "Peinture"},
    {"English": "Photo", "French": "Photo"},
    {"English": "Book", "French": "Livre"},
    {"English": "Magazine", "French": "Magazine"},
    {"English": "Newspaper", "French": "Journal"},
    {"English": "Pen", "French": "Stylo"},
    {"English": "Pencil", "French": "Crayon"},
    {"English": "Paper", "French": "Papier"},
    {"English": "Letter", "French": "Lettre"},
    {"English": "Card", "French": "Carte"},
    {"English": "Gift", "French": "Cadeau"},
    {"English": "Box", "French": "Boîte"},
    {"English": "Bag", "French": "Sac"},
    {"English": "Suitcase", "French": "Valise"},
    {"English": "Clothes", "French": "Vêtements"},
    {"English": "Hat", "French": "Chapeau"},
    {"English": "Shoes", "French": "Chaussures"},
    {"English": "Pants", "French": "Pantalon"},
    {"English": "Shirt", "French": "Chemise"},
    {"English": "Dress", "French": "Robe"},
    {"English": "Skirt", "French": "Jupe"},
    {"English": "Coat", "French": "Manteau"},
    {"English": "Gloves", "French": "Gants"},
    {"English": "Scarf", "French": "Écharpe"},
    {"English": "Socks", "French": "Chaussettes"},
    {"English": "Glasses", "French": "Lunettes"},
    {"English": "Watch", "French": "Montre"},
    {"English": "Jewelry", "French": "Bijoux"},
    {"English": "Ring", "French": "Bague"},
    {"English": "Bracelet", "French": "Bracelet"},
    {"English": "Necklace", "French": "Collier"},
    {"English": "Earrings", "French": "Boucles d'oreilles"},
    {"English": "Food", "French": "Aliments"},
    {"English": "Water", "French": "Eau"},
    {"English": "Bread", "French": "Pain"},
    {"English": "Cheese", "French": "Fromage"},
    {"English": "Wine", "French": "Vin"},
    {"English": "Beer", "French": "Bière"},
    {"English": "Coffee", "French": "Café"},
    {"English": "Tea", "French": "Thé"},
    {"English": "Juice", "French": "Jus"},
    {"English": "Milk", "French": "Lait"},
    {"English": "Meat", "French": "Viande"},
    {"English": "Fish", "French": "Poisson"},
    {"English": "Chicken", "French": "Poulet"},
    {"English": "Vegetables", "French": "Légumes"},
    {"English": "Fruits", "French": "Fruits"},
    {"English": "Dessert", "French": "Dessert"},
    {"English": "Cake", "French": "Gâteau"},
    {"English": "Chocolate", "French": "Chocolat"},
    {"English": "Ice cream", "French": "Glace"},
    {"English": "Candy", "French": "Bonbon"},
    {"English": "Cookies", "French": "Biscuits"},
    {"English": "Pizza", "French": "Pizza"},
    {"English": "Hamburger", "French": "Hamburger"},
    {"English": "Fries", "French": "Frites"},
]

class FlashcardApp:
    def __init__(self, root):
        self.root = root
        self.root.title("English to French Flashcards")
        self.root.configure(bg="#add8e6")  # Light blue background
        self.root.attributes('-fullscreen', True)

        self.current_index = 0
        self.correct_answers = 0
        self.words_learned = 0

        self.main_frame = tk.Frame(root, bg="#add8e6")
        self.main_frame.pack(expand=True, fill=tk.BOTH)

        self.question_frame = tk.Frame(self.main_frame, bg="#add8e6")
        self.question_frame.pack(pady=20)

        self.english_label = tk.Label(self.question_frame, text="", font=("Helvetica", 36), bg="#add8e6")
        self.english_label.pack(pady=20)

        self.buttons_frame = tk.Frame(self.main_frame, bg="#add8e6")
        self.buttons_frame.pack(pady=20)

        self.buttons = []
        for i in range(4):
            button = tk.Button(self.buttons_frame, text="", font=("Helvetica", 20), bg="#ffffff", command=lambda i=i: self.check_answer(i))
            button.grid(row=i//2, column=i%2, padx=20, pady=20, ipadx=20, ipady=20)
            self.buttons.append(button)

        self.result_label = tk.Label(self.main_frame, text="", font=("Helvetica", 20), bg="#add8e6")
        self.result_label.pack(pady=20)

        self.stats_frame = tk.Frame(self.main_frame, bg="#add8e6")
        self.stats_frame.pack(pady=20)

        self.correct_label = tk.Label(self.stats_frame, text=f"Correct Answers: {self.correct_answers}", font=("Helvetica", 20), bg="#add8e6")
        self.correct_label.pack(side=tk.LEFT, padx=20)

        self.learned_label = tk.Label(self.stats_frame, text=f"Words Learned: {self.words_learned}", font=("Helvetica", 20), bg="#add8e6")
        self.learned_label.pack(side=tk.LEFT, padx=20)

        self.left_label = tk.Label(self.stats_frame, text=f"Words Left: {len(flashcards)}", font=("Helvetica", 20), bg="#add8e6")
        self.left_label.pack(side=tk.LEFT, padx=20)

        self.next_button = tk.Button(self.main_frame, text="Next", font=("Helvetica", 20), bg="#ffffff", command=self.next_card)
        self.next_button.pack(pady=20)

        self.next_card()

    def next_card(self):
        if not flashcards:
            self.english_label.config(text="All words learned!", font=("Helvetica", 36))
            for button in self.buttons:
                button.pack_forget()
            self.result_label.config(text="")
            self.next_button.pack_forget()
            return

        self.current_index = random.randint(0, len(flashcards) - 1)
        self.correct_answer = flashcards[self.current_index]["French"]

        self.english_label.config(text=flashcards[self.current_index]["English"])
        self.result_label.config(text="")

        answers = [flashcards[self.current_index]["French"]]
        while len(answers) < 4:
            option = random.choice(flashcards)["French"]
            if option not in answers:
                answers.append(option)

        random.shuffle(answers)
        for i in range(4):
            self.buttons[i].config(text=answers[i], state=tk.NORMAL)

    def check_answer(self, index):
        selected_answer = self.buttons[index].cget("text")
        if selected_answer == self.correct_answer:
            self.result_label.config(text="Correct!", fg="green")
            self.correct_answers += 1
            self.words_learned += 1
            flashcards.pop(self.current_index)
        else:
            self.result_label.config(text=f"Incorrect! The correct answer is {self.correct_answer}", fg="red")

        self.update_stats()

        for button in self.buttons:
            button.config(state=tk.DISABLED)

    def update_stats(self):
        self.correct_label.config(text=f"Correct Answers: {self.correct_answers}")
        self.learned_label.config(text=f"Words Learned: {self.words_learned}")
        self.left_label.config(text=f"Words Left: {len(flashcards)}")

if __name__ == "__main__":
    root = tk.Tk()
    app = FlashcardApp(root)
    root.mainloop()
