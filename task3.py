from flask import Flask, request, jsonify, render_template
import spacy

app = Flask(__name__)
nlp = spacy.load("en_core_web_sm")

# Enhanced intents
intents = [
    {
        "tag": "greeting",
        "patterns": ["hello", "hi", "hey", "good morning", "good afternoon", "greetings", "what's up"],
        "response": "Hello! 👋 Welcome to Vector Classes. How can I assist you today?"
    },
    {
        "tag": "courses",
        "patterns": [
            "what courses do you offer", "tell me about your courses", "which subjects are available",
            "classes available", "programs", "can you tell me your programs",
            "courses","course"
        ],
        "response": "We offer:\n- IIT-JEE (Mains & Advanced)\n- NEET (UG Medical)\n- CET\n- Olympiad/Foundation (Classes 6–10)\n- CBSE/State Boards (Class 10 & 12)"
    },
    {
        "tag": "fees",
        "patterns": [
            "what are the fees", "how much does it cost", "fee structure", "what is the price",
            "tuition fees", "cost of course","fees"
        ],
        "response": "Fees:\n- JEE/NEET: ₹50,000 – ₹75,000/year\n- Foundation: ₹30,000 – ₹40,000\n- Board exam coaching: ₹25,000 – ₹35,000\n💡 Installments and scholarships available!"
    },
    {
        "tag": "timings",
        "patterns": [
            "what are your class timings", "when are the classes", "class schedule", "batch timings",
            "what time are your classes", "class time","time","timings","timing"
        ],
        "response": "⏰ Class timings:\n- Morning: 8 AM – 12 PM\n- Afternoon: 1 PM – 4 PM\n- Evening: 5 PM – 7 PM\nChoose your preferred batch!"
    },
    {
        "tag": "location",
        "patterns": [
            "where are you located", "your address", "location of the center", "how to reach",
            "center address", "in which area is your institute","area","location"
        ],
        "response": "📍 Location:\nVector Classes, ABC Road, XYZ Nagar, near City Library, Pune.\n🗺️ Find us on Google Maps: 'Vector Classes Pune'"
    },
    {
        "tag": "admission",
        "patterns": [
            "how to enroll", "admission process", "register for course", "how to join", "enrollment steps", "admission","how to take admission","registration"
        ],
        "response": "📝 Admission Steps:\n1. Visit our center OR\n2. Call +91-9876543210 OR\n3. Register online at www.vectorclasses.in/admission\nWe'll guide you through everything!"
    },
    {
        "tag": "contact",
        "patterns": [
            "how can I contact you", "phone number", "email", "call you", "reach you","contact"
        ],
        "response": "📞 Phone: +91-9876543210\n📧 Email: info@vectorclasses.in\n🌐 Website: www.vectorclasses.in"
    },
    {
        "tag": "facilities",
        "patterns": [
            "what facilities do you provide", "infrastructure", "study material", "hostel",
            "library", "classroom environment","facility","facilities"
        ],
        "response": "🏫 Facilities:\n- AC Classrooms\n- Study Material & Library\n- Doubt Sessions\n- Test Series\n- Hostel for outstation students"
    },
    {
        "tag": "thanks",
        "patterns": ["thank you", "thanks", "thanks a lot", "thank you very much", "tysm"],
        "response": "You're welcome! 😊 Feel free to ask anything else!"
    },
    {
        "tag": "goodbye",
        "patterns": ["bye", "goodbye", "see you", "talk to you later", "bye bye"],
        "response": "Goodbye! 👋 Hope to see you at Vector Classes soon!"
    }
]

# Routes
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/get", methods=["POST"])
def chatbot_response():
    user_msg = request.form["msg"].strip().lower()
    response = generate_response(user_msg)
    return jsonify({"response": response})

# Matching logic
def generate_response(message):
    doc = nlp(message)
    for intent in intents:
        for pattern in intent["patterns"]:
            if pattern in message:
                return intent["response"]
    return "❓ Sorry, I didn't understand that. Could you rephrase?"

# Run the server
if __name__ == "__main__":
    app.run(debug=True)
